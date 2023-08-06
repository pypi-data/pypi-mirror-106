from __future__ import division, unicode_literals

import os.path as osp
import sys
from datetime import datetime

import cv2
import numpy as np
import torch
from pybsc import pairwise
from torch import nn
from torch.nn import functional as F
from torchvision import models, transforms

from anet_tools.augmentation import RandomAugmentation
from anet_tools.features import BNInception, Resnet200
from anet_tools.video.video_proc import ImageSequenceProc, VideoProc

this_filepath = osp.dirname(__file__)
# sys.path.append(osp.join(this_filepath, 'features', 'flownet2'))
import os.path as osp

import gdown
# from models import FlowNet2

download_dir = osp.expanduser('~/.flownet')

flownets = {
    'FlowNet2': '1hF8vS6YeHkx3j2pfCeQqqZGwA_PJq_Da',
    'FlowNet2-CS': '1iBJ1_o7PloaINpa8m7u_7TsLCX0Dt_jS',
    'FlowNet2-S': '1V61dZjFomwlynwlYklJHC-TLfdFom3Lg',
}


def get_flownet_pretrainedmodel(split='FlowNet2-CS'):
    dst_path = osp.join(
            download_dir, '{}_checkpoint.pth.tar'.format(split))
    g_id = flownets[split]
    gdown.cached_download(
        url='https://drive.google.com/uc?id={}'.format(g_id),
        path=dst_path,
        quiet=True,
    )
    return dst_path


# def convert_flow_to_image(flow, low=-15.0, high=15.0):
#     return np.array(np.clip(255 * (flow - low) / (high - low), 0, 255),
#                     dtype=np.uint8)

def convert_flow_to_image(flow):
    high = flow.max()
    low = flow.min()
    return np.array(np.clip(255 * (flow - low) / (high - low), 0, 255),
                    dtype=np.uint8)



def centralize(img1, img2):
    b, c, h, w = img1.shape
    rgb_mean = torch.cat([img1, img2], dim=2).view(b, c, -1).mean(2).view(b, c, 1, 1)
    return img1 - rgb_mean, img2 - rgb_mean, rgb_mean


class ActionFeatureExtractor(object):

    """
    This class provides and end-to-end interface to classifying videos into activity classes
    """

    def __init__(self, device=-1, use_torch_resnet=False):
        """
        Contruct an action classifier
        Args:
            models: list of tuples in the form of
                    (model_proto, model_params, model_fusion_weight, input_type, conv_support, input_size).
                    input_type is: 0-RGB, 1-Optical flow.
                    conv_support indicates whether the network supports convolution testing, which is faster. If this is
                    not supported, we will use oversampling instead
            total_norm_weights: sum of all model_fusion_weights when normalization is wanted, otherwise use None
        """
        if device >= 0:
            self.device = torch.device(device)
        else:
            self.device = torch.device('cpu')

        self.use_torch_resnet = use_torch_resnet
        if use_torch_resnet:
            self.resnet = models.resnet152(pretrained=True)
            self.resnet.fc = nn.Identity()
            normalize = transforms.Normalize(
                mean=[0.485, 0.456, 0.406],
                std=[0.229, 0.224, 0.225])
            self.transform = transforms.Compose(
                [transforms.ToTensor(), normalize])
        else:
            self.resnet = Resnet200(pretrained_model=True)
        self.resnet.eval()
        self.resnet = self.resnet.to(self.device)

        self.bn_inception = BNInception(pretrained_model=True)
        self.bn_inception.eval()
        self.bn_inception = self.bn_inception.to(self.device)

        # import argparse
        # parser = argparse.ArgumentParser()
        # parser.add_argument('--fp16', action='store_true', help='Run model in pseudo-fp16 mode (fp16 storage fp32 math).')
        # parser.add_argument("--rgb_max", type=float, default=255.)
        # args = parser.parse_args(['--rgb_max', '255'])
        # net = FlowNet2(args).to(self.device)
        # state_dict = torch.load(get_flownet_pretrainedmodel('FlowNet2'))
        # net.load_state_dict(state_dict["state_dict"])
        # net.eval()
        from fastflownet import FastFlowNet
        net = FastFlowNet().to(self.device).eval()
        self.flownet = net

    def _process(self, frm_it, debug=False, augmentation=False):
        if debug:
            print('Feature Extraction Processing')
            func_start = datetime.now()

        all_features = {'resnet': np.empty(shape=(0, 2048)),
                        'bn': np.empty(shape=(0, 1024))}

        if augmentation:
            ra = RandomAugmentation(30)

        for i_frame, frm_stack in enumerate(frm_it):
            if debug:
                start = datetime.now()

            if augmentation:
                frm_stack = [ra(img) for img in frm_stack]

            bgr_img = frm_stack[0]

            with torch.no_grad():
                if self.use_torch_resnet:
                    rgb_img = cv2.resize(bgr_img[..., ::-1], (224, 224))
                    torch_rgb_img = self.transform(
                        np.array(rgb_img, 'f'))[None, ]
                    torch_rgb_img = torch_rgb_img.to(self.device)
                    resnet_feat = self.resnet(
                        torch_rgb_img).detach().cpu().numpy()
                else:
                    chw_img = np.array(bgr_img.transpose(2, 0, 1), 'f')
                    chw_img -= np.array([104, 117, 123], 'f').reshape(3, 1, 1)
                    torch_bgr_img = torch.from_numpy(chw_img[None, ])
                    torch_bgr_img = torch_bgr_img.to(self.device)
                    resnet_feat = self.resnet(
                        torch_bgr_img).detach().cpu().numpy()

            # flownet2
            # batch_imgs = np.zeros((5, 3, 2, 256, 256), dtype=np.float32)
            # for j_frame, (prev_frame, cur_frame) in enumerate(pairwise(frm_stack)):
            #     pim1 = cv2.resize(prev_frame, (256, 256))
            #     pim2 = cv2.resize(cur_frame, (256, 256))
            #     images = [pim1, pim2]
            #     images = np.array(images).transpose(3, 0, 1, 2)
            #     batch_imgs[j_frame] = images

            # fastflownet
            batch_img1 = np.zeros((5, 256, 256, 3), dtype=np.float32)
            batch_img2 = np.zeros((5, 256, 256, 3), dtype=np.float32)
            for j_frame, (prev_frame, cur_frame) in enumerate(pairwise(frm_stack)):
                pim1 = cv2.resize(prev_frame, (256, 256))
                pim2 = cv2.resize(cur_frame, (256, 256))
                batch_img1[j_frame] = pim1
                batch_img2[j_frame] = pim2

            div_flow = 20.0
            input_size = (256, 256)
            with torch.no_grad():
                img1 = torch.from_numpy(batch_img1)
                img2 = torch.from_numpy(batch_img2)
                img1 = img1.float().permute(0, 3, 1, 2) / 255.0
                img2 = img2.float().permute(0, 3, 1, 2) / 255.0
                img1, img2, _ = centralize(img1, img2)
                input_t = torch.cat([img1, img2], 1).to(self.device)
                tmp_flows = div_flow * F.interpolate(
                    self.flownet(input_t).data, size=input_size, mode='bilinear',
                    align_corners=False)
                flows = tmp_flows.cpu().permute(0, 2, 3, 1).numpy()
                del tmp_flows

            flow_stack = np.zeros((5 * 2, 224, 224), 'f')
            for j_frame, flow in enumerate(flows):
                flow_stack[j_frame * 2] = cv2.resize(convert_flow_to_image(flow[..., 0]), (224, 224))
                flow_stack[j_frame * 2 + 1] = cv2.resize(convert_flow_to_image(flow[..., 1]), (224, 224))
            flow_stack -= 128.0

            with torch.no_grad():
                torch_flow_stack = torch.from_numpy(flow_stack.reshape(1, 10, 224, 224)).to(self.device)
                bn_feat = self.bn_inception(
                    torch_flow_stack).detach().cpu().numpy()[0]

            all_features['resnet'] = np.concatenate(
                (all_features['resnet'], resnet_feat), axis=0)

            bn_feat = np.reshape(bn_feat, (1, bn_feat.shape[0]))
            all_features['bn'] = np.concatenate((all_features['bn'], bn_feat), axis=0)

            if debug:
                end = datetime.now()
                elapsed = end - start
                print("frame sample {}: {} second".format(i_frame, elapsed))

        if debug:
            func_end = datetime.now()
            elapsed = func_end - func_start
            print("Process video : {} second".format(elapsed))

        return all_features

    def extract_from_file(self, filename, debug=False, augmentation=False,
                          interval=1 / 6.0):
        """
        Input a file on harddisk
        Args:
            filename:

        Returns:
            cls: classification scores
            all_features: RGB ResNet feature and Optical flow BN Inception feature in a list
        """
        video_proc = VideoProc.from_file(filename)

        # here we use interval of 30, roughly 1FPS
        frm_it = video_proc.frame_iter(
            timely=True, ignore_err=True, interval=interval,
            length=6, new_size=(340, 256))
        return self._process(frm_it, debug=debug, augmentation=augmentation)

    def extract_from_imgs(self, imgs, timestamps, debug=False,
                          augmentation=False, interval=1 / 6.0):
        video_proc = ImageSequenceProc(imgs, timestamps)
        frm_it = video_proc.frame_iter(
            interval=interval,
            length=6, new_size=(340, 256))
        return self._process(frm_it, debug=debug, augmentation=augmentation)


if __name__ == '__main__':
    extractor = ActionFeatureExtractor(device=0)
    from eos import measure
    with measure('time'):
        all_features = extractor.extract_from_file(
            osp.join(this_filepath, 'data', 'motions', 'wiping.mp4'),
            debug=True)
