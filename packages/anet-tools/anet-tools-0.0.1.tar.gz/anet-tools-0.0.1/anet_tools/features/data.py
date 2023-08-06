import os.path as osp

import gdown
from eos import makedirs

download_dir = osp.expanduser('~/.anet_tools')


def get_resnet200_pretrained_model():
    makedirs(download_dir)
    target_path = osp.join(download_dir, 'resnet200_anet_2016.pt')
    if not osp.exists(target_path):
        gdown.cached_download(
            'https://drive.google.com/uc?id=1Xin1jzNNle_R-O-E9nVQDgv086eoj0qs',
            path=target_path,
            md5='010cd5bbccddc90c9a6e3fbed258eeb4')
    return target_path


def get_bn_inception_pretrained_model():
    makedirs(download_dir)
    target_path = osp.join(
        download_dir, 'bn_inception_anet_2016_temporal.v5.pt')
    if not osp.exists(target_path):
        gdown.cached_download(
            'https://drive.google.com/uc?id=1NJ9u10jrqFQwe3AJoKLm7oY-Rf0leKoV',
            path=target_path,
            md5='c4c2bf46584b651e19a6e41df67f4a27')
    return target_path
