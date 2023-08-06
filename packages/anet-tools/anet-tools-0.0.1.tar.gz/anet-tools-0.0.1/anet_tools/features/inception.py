# flake8: noqa

import torch
import torch.nn as nn
import torch.nn.functional as F

from anet_tools.features.data import get_bn_inception_pretrained_model


class BNInception(nn.Module):

    def __init__(self, pretrained_model=True):
        super(BNInception, self).__init__()
        self.conv1_7x7_s2 = nn.Conv2d(
            10, 64, kernel_size=(
                7, 7), stride=(
                2, 2), padding=(
                3, 3), dilation=1, groups=1, bias=True)
        self.conv1_7x7_s2_bn = nn.BatchNorm2d(64, momentum=0.1)
        self.conv1_relu_7x7 = nn.ReLU()
        self.pool1_3x3_s2 = nn.MaxPool2d(
            kernel_size=(
                3, 3), stride=(
                2, 2), padding=(
                0, 0), ceil_mode=True)
        self.conv2_3x3_reduce = nn.Conv2d(
            64, 64, kernel_size=(
                1, 1), stride=(
                1, 1), padding=(
                0, 0), dilation=1, groups=1, bias=True)
        self.conv2_3x3_reduce_bn = nn.BatchNorm2d(64, momentum=0.1)
        self.conv2_relu_3x3_reduce = nn.ReLU()
        self.conv2_3x3 = nn.Conv2d(
            64, 192, kernel_size=(
                3, 3), stride=(
                1, 1), padding=(
                1, 1), dilation=1, groups=1, bias=True)
        self.conv2_3x3_bn = nn.BatchNorm2d(192, momentum=0.1)
        self.conv2_relu_3x3 = nn.ReLU()
        self.pool2_3x3_s2 = nn.MaxPool2d(
            kernel_size=(
                3, 3), stride=(
                2, 2), padding=(
                0, 0), ceil_mode=True)
        self.inception_3a_1x1 = nn.Conv2d(
            192, 64, kernel_size=(
                1, 1), stride=(
                1, 1), padding=(
                0, 0), dilation=1, groups=1, bias=True)
        self.inception_3a_1x1_bn = nn.BatchNorm2d(64, momentum=0.1)
        self.inception_3a_relu_1x1 = nn.ReLU()
        self.inception_3a_3x3_reduce = nn.Conv2d(
            192, 64, kernel_size=(
                1, 1), stride=(
                1, 1), padding=(
                0, 0), dilation=1, groups=1, bias=True)
        self.inception_3a_3x3_reduce_bn = nn.BatchNorm2d(64, momentum=0.1)
        self.inception_3a_relu_3x3_reduce = nn.ReLU()
        self.inception_3a_3x3 = nn.Conv2d(
            64, 64, kernel_size=(
                3, 3), stride=(
                1, 1), padding=(
                1, 1), dilation=1, groups=1, bias=True)
        self.inception_3a_3x3_bn = nn.BatchNorm2d(64, momentum=0.1)
        self.inception_3a_relu_3x3 = nn.ReLU()
        self.inception_3a_double_3x3_reduce = nn.Conv2d(
            192, 64, kernel_size=(
                1, 1), stride=(
                1, 1), padding=(
                0, 0), dilation=1, groups=1, bias=True)
        self.inception_3a_double_3x3_reduce_bn = nn.BatchNorm2d(
            64, momentum=0.1)
        self.inception_3a_relu_double_3x3_reduce = nn.ReLU()
        self.inception_3a_double_3x3_1 = nn.Conv2d(
            64, 96, kernel_size=(
                3, 3), stride=(
                1, 1), padding=(
                1, 1), dilation=1, groups=1, bias=True)
        self.inception_3a_double_3x3_1_bn = nn.BatchNorm2d(96, momentum=0.1)
        self.inception_3a_relu_double_3x3_1 = nn.ReLU()
        self.inception_3a_double_3x3_2 = nn.Conv2d(
            96, 96, kernel_size=(
                3, 3), stride=(
                1, 1), padding=(
                1, 1), dilation=1, groups=1, bias=True)
        self.inception_3a_double_3x3_2_bn = nn.BatchNorm2d(96, momentum=0.1)
        self.inception_3a_relu_double_3x3_2 = nn.ReLU()
        self.inception_3a_pool = nn.AvgPool2d(
            kernel_size=(
                3, 3), stride=(
                1, 1), padding=(
                1, 1), ceil_mode=True)
        self.inception_3a_pool_proj = nn.Conv2d(
            192, 32, kernel_size=(
                1, 1), stride=(
                1, 1), padding=(
                0, 0), dilation=1, groups=1, bias=True)
        self.inception_3a_pool_proj_bn = nn.BatchNorm2d(32, momentum=0.1)
        self.inception_3a_relu_pool_proj = nn.ReLU()
        self.inception_3b_1x1 = nn.Conv2d(
            256, 64, kernel_size=(
                1, 1), stride=(
                1, 1), padding=(
                0, 0), dilation=1, groups=1, bias=True)
        self.inception_3b_1x1_bn = nn.BatchNorm2d(64, momentum=0.1)
        self.inception_3b_relu_1x1 = nn.ReLU()
        self.inception_3b_3x3_reduce = nn.Conv2d(
            256, 64, kernel_size=(
                1, 1), stride=(
                1, 1), padding=(
                0, 0), dilation=1, groups=1, bias=True)
        self.inception_3b_3x3_reduce_bn = nn.BatchNorm2d(64, momentum=0.1)
        self.inception_3b_relu_3x3_reduce = nn.ReLU()
        self.inception_3b_3x3 = nn.Conv2d(
            64, 96, kernel_size=(
                3, 3), stride=(
                1, 1), padding=(
                1, 1), dilation=1, groups=1, bias=True)
        self.inception_3b_3x3_bn = nn.BatchNorm2d(96, momentum=0.1)
        self.inception_3b_relu_3x3 = nn.ReLU()
        self.inception_3b_double_3x3_reduce = nn.Conv2d(
            256, 64, kernel_size=(
                1, 1), stride=(
                1, 1), padding=(
                0, 0), dilation=1, groups=1, bias=True)
        self.inception_3b_double_3x3_reduce_bn = nn.BatchNorm2d(
            64, momentum=0.1)
        self.inception_3b_relu_double_3x3_reduce = nn.ReLU()
        self.inception_3b_double_3x3_1 = nn.Conv2d(
            64, 96, kernel_size=(
                3, 3), stride=(
                1, 1), padding=(
                1, 1), dilation=1, groups=1, bias=True)
        self.inception_3b_double_3x3_1_bn = nn.BatchNorm2d(96, momentum=0.1)
        self.inception_3b_relu_double_3x3_1 = nn.ReLU()
        self.inception_3b_double_3x3_2 = nn.Conv2d(
            96, 96, kernel_size=(
                3, 3), stride=(
                1, 1), padding=(
                1, 1), dilation=1, groups=1, bias=True)
        self.inception_3b_double_3x3_2_bn = nn.BatchNorm2d(96, momentum=0.1)
        self.inception_3b_relu_double_3x3_2 = nn.ReLU()
        self.inception_3b_pool = nn.AvgPool2d(
            kernel_size=(
                3, 3), stride=(
                1, 1), padding=(
                1, 1), ceil_mode=True)
        self.inception_3b_pool_proj = nn.Conv2d(
            256, 64, kernel_size=(
                1, 1), stride=(
                1, 1), padding=(
                0, 0), dilation=1, groups=1, bias=True)
        self.inception_3b_pool_proj_bn = nn.BatchNorm2d(64, momentum=0.1)
        self.inception_3b_relu_pool_proj = nn.ReLU()
        self.inception_3c_3x3_reduce = nn.Conv2d(
            320, 128, kernel_size=(
                1, 1), stride=(
                1, 1), padding=(
                0, 0), dilation=1, groups=1, bias=True)
        self.inception_3c_3x3_reduce_bn = nn.BatchNorm2d(128, momentum=0.1)
        self.inception_3c_relu_3x3_reduce = nn.ReLU()
        self.inception_3c_3x3 = nn.Conv2d(
            128, 160, kernel_size=(
                3, 3), stride=(
                2, 2), padding=(
                1, 1), dilation=1, groups=1, bias=True)
        self.inception_3c_3x3_bn = nn.BatchNorm2d(160, momentum=0.1)
        self.inception_3c_relu_3x3 = nn.ReLU()
        self.inception_3c_double_3x3_reduce = nn.Conv2d(
            320, 64, kernel_size=(
                1, 1), stride=(
                1, 1), padding=(
                0, 0), dilation=1, groups=1, bias=True)
        self.inception_3c_double_3x3_reduce_bn = nn.BatchNorm2d(
            64, momentum=0.1)
        self.inception_3c_relu_double_3x3_reduce = nn.ReLU()
        self.inception_3c_double_3x3_1 = nn.Conv2d(
            64, 96, kernel_size=(
                3, 3), stride=(
                1, 1), padding=(
                1, 1), dilation=1, groups=1, bias=True)
        self.inception_3c_double_3x3_1_bn = nn.BatchNorm2d(96, momentum=0.1)
        self.inception_3c_relu_double_3x3_1 = nn.ReLU()
        self.inception_3c_double_3x3_2 = nn.Conv2d(
            96, 96, kernel_size=(
                3, 3), stride=(
                2, 2), padding=(
                1, 1), dilation=1, groups=1, bias=True)
        self.inception_3c_double_3x3_2_bn = nn.BatchNorm2d(96, momentum=0.1)
        self.inception_3c_relu_double_3x3_2 = nn.ReLU()
        self.inception_3c_pool = nn.MaxPool2d(
            kernel_size=(
                3, 3), stride=(
                2, 2), padding=(
                0, 0), ceil_mode=True)
        self.inception_4a_1x1 = nn.Conv2d(
            576, 224, kernel_size=(
                1, 1), stride=(
                1, 1), padding=(
                0, 0), dilation=1, groups=1, bias=True)
        self.inception_4a_1x1_bn = nn.BatchNorm2d(224, momentum=0.1)
        self.inception_4a_relu_1x1 = nn.ReLU()
        self.inception_4a_3x3_reduce = nn.Conv2d(
            576, 64, kernel_size=(
                1, 1), stride=(
                1, 1), padding=(
                0, 0), dilation=1, groups=1, bias=True)
        self.inception_4a_3x3_reduce_bn = nn.BatchNorm2d(64, momentum=0.1)
        self.inception_4a_relu_3x3_reduce = nn.ReLU()
        self.inception_4a_3x3 = nn.Conv2d(
            64, 96, kernel_size=(
                3, 3), stride=(
                1, 1), padding=(
                1, 1), dilation=1, groups=1, bias=True)
        self.inception_4a_3x3_bn = nn.BatchNorm2d(96, momentum=0.1)
        self.inception_4a_relu_3x3 = nn.ReLU()
        self.inception_4a_double_3x3_reduce = nn.Conv2d(
            576, 96, kernel_size=(
                1, 1), stride=(
                1, 1), padding=(
                0, 0), dilation=1, groups=1, bias=True)
        self.inception_4a_double_3x3_reduce_bn = nn.BatchNorm2d(
            96, momentum=0.1)
        self.inception_4a_relu_double_3x3_reduce = nn.ReLU()
        self.inception_4a_double_3x3_1 = nn.Conv2d(
            96, 128, kernel_size=(
                3, 3), stride=(
                1, 1), padding=(
                1, 1), dilation=1, groups=1, bias=True)
        self.inception_4a_double_3x3_1_bn = nn.BatchNorm2d(128, momentum=0.1)
        self.inception_4a_relu_double_3x3_1 = nn.ReLU()
        self.inception_4a_double_3x3_2 = nn.Conv2d(
            128, 128, kernel_size=(
                3, 3), stride=(
                1, 1), padding=(
                1, 1), dilation=1, groups=1, bias=True)
        self.inception_4a_double_3x3_2_bn = nn.BatchNorm2d(128, momentum=0.1)
        self.inception_4a_relu_double_3x3_2 = nn.ReLU()
        self.inception_4a_pool = nn.AvgPool2d(
            kernel_size=(
                3, 3), stride=(
                1, 1), padding=(
                1, 1), ceil_mode=True)
        self.inception_4a_pool_proj = nn.Conv2d(
            576, 128, kernel_size=(
                1, 1), stride=(
                1, 1), padding=(
                0, 0), dilation=1, groups=1, bias=True)
        self.inception_4a_pool_proj_bn = nn.BatchNorm2d(128, momentum=0.1)
        self.inception_4a_relu_pool_proj = nn.ReLU()
        self.inception_4b_1x1 = nn.Conv2d(
            576, 192, kernel_size=(
                1, 1), stride=(
                1, 1), padding=(
                0, 0), dilation=1, groups=1, bias=True)
        self.inception_4b_1x1_bn = nn.BatchNorm2d(192, momentum=0.1)
        self.inception_4b_relu_1x1 = nn.ReLU()
        self.inception_4b_3x3_reduce = nn.Conv2d(
            576, 96, kernel_size=(
                1, 1), stride=(
                1, 1), padding=(
                0, 0), dilation=1, groups=1, bias=True)
        self.inception_4b_3x3_reduce_bn = nn.BatchNorm2d(96, momentum=0.1)
        self.inception_4b_relu_3x3_reduce = nn.ReLU()
        self.inception_4b_3x3 = nn.Conv2d(
            96, 128, kernel_size=(
                3, 3), stride=(
                1, 1), padding=(
                1, 1), dilation=1, groups=1, bias=True)
        self.inception_4b_3x3_bn = nn.BatchNorm2d(128, momentum=0.1)
        self.inception_4b_relu_3x3 = nn.ReLU()
        self.inception_4b_double_3x3_reduce = nn.Conv2d(
            576, 96, kernel_size=(
                1, 1), stride=(
                1, 1), padding=(
                0, 0), dilation=1, groups=1, bias=True)
        self.inception_4b_double_3x3_reduce_bn = nn.BatchNorm2d(
            96, momentum=0.1)
        self.inception_4b_relu_double_3x3_reduce = nn.ReLU()
        self.inception_4b_double_3x3_1 = nn.Conv2d(
            96, 128, kernel_size=(
                3, 3), stride=(
                1, 1), padding=(
                1, 1), dilation=1, groups=1, bias=True)
        self.inception_4b_double_3x3_1_bn = nn.BatchNorm2d(128, momentum=0.1)
        self.inception_4b_relu_double_3x3_1 = nn.ReLU()
        self.inception_4b_double_3x3_2 = nn.Conv2d(
            128, 128, kernel_size=(
                3, 3), stride=(
                1, 1), padding=(
                1, 1), dilation=1, groups=1, bias=True)
        self.inception_4b_double_3x3_2_bn = nn.BatchNorm2d(128, momentum=0.1)
        self.inception_4b_relu_double_3x3_2 = nn.ReLU()
        self.inception_4b_pool = nn.AvgPool2d(
            kernel_size=(
                3, 3), stride=(
                1, 1), padding=(
                1, 1), ceil_mode=True)
        self.inception_4b_pool_proj = nn.Conv2d(
            576, 128, kernel_size=(
                1, 1), stride=(
                1, 1), padding=(
                0, 0), dilation=1, groups=1, bias=True)
        self.inception_4b_pool_proj_bn = nn.BatchNorm2d(128, momentum=0.1)
        self.inception_4b_relu_pool_proj = nn.ReLU()
        self.inception_4c_1x1 = nn.Conv2d(
            576, 160, kernel_size=(
                1, 1), stride=(
                1, 1), padding=(
                0, 0), dilation=1, groups=1, bias=True)
        self.inception_4c_1x1_bn = nn.BatchNorm2d(160, momentum=0.1)
        self.inception_4c_relu_1x1 = nn.ReLU()
        self.inception_4c_3x3_reduce = nn.Conv2d(
            576, 128, kernel_size=(
                1, 1), stride=(
                1, 1), padding=(
                0, 0), dilation=1, groups=1, bias=True)
        self.inception_4c_3x3_reduce_bn = nn.BatchNorm2d(128, momentum=0.1)
        self.inception_4c_relu_3x3_reduce = nn.ReLU()
        self.inception_4c_3x3 = nn.Conv2d(
            128, 160, kernel_size=(
                3, 3), stride=(
                1, 1), padding=(
                1, 1), dilation=1, groups=1, bias=True)
        self.inception_4c_3x3_bn = nn.BatchNorm2d(160, momentum=0.1)
        self.inception_4c_relu_3x3 = nn.ReLU()
        self.inception_4c_double_3x3_reduce = nn.Conv2d(
            576, 128, kernel_size=(
                1, 1), stride=(
                1, 1), padding=(
                0, 0), dilation=1, groups=1, bias=True)
        self.inception_4c_double_3x3_reduce_bn = nn.BatchNorm2d(
            128, momentum=0.1)
        self.inception_4c_relu_double_3x3_reduce = nn.ReLU()
        self.inception_4c_double_3x3_1 = nn.Conv2d(
            128, 160, kernel_size=(
                3, 3), stride=(
                1, 1), padding=(
                1, 1), dilation=1, groups=1, bias=True)
        self.inception_4c_double_3x3_1_bn = nn.BatchNorm2d(160, momentum=0.1)
        self.inception_4c_relu_double_3x3_1 = nn.ReLU()
        self.inception_4c_double_3x3_2 = nn.Conv2d(
            160, 160, kernel_size=(
                3, 3), stride=(
                1, 1), padding=(
                1, 1), dilation=1, groups=1, bias=True)
        self.inception_4c_double_3x3_2_bn = nn.BatchNorm2d(160, momentum=0.1)
        self.inception_4c_relu_double_3x3_2 = nn.ReLU()
        self.inception_4c_pool = nn.AvgPool2d(
            kernel_size=(
                3, 3), stride=(
                1, 1), padding=(
                1, 1), ceil_mode=True)
        self.inception_4c_pool_proj = nn.Conv2d(
            576, 128, kernel_size=(
                1, 1), stride=(
                1, 1), padding=(
                0, 0), dilation=1, groups=1, bias=True)
        self.inception_4c_pool_proj_bn = nn.BatchNorm2d(128, momentum=0.1)
        self.inception_4c_relu_pool_proj = nn.ReLU()
        self.inception_4d_1x1 = nn.Conv2d(
            608, 96, kernel_size=(
                1, 1), stride=(
                1, 1), padding=(
                0, 0), dilation=1, groups=1, bias=True)
        self.inception_4d_1x1_bn = nn.BatchNorm2d(96, momentum=0.1)
        self.inception_4d_relu_1x1 = nn.ReLU()
        self.inception_4d_3x3_reduce = nn.Conv2d(
            608, 128, kernel_size=(
                1, 1), stride=(
                1, 1), padding=(
                0, 0), dilation=1, groups=1, bias=True)
        self.inception_4d_3x3_reduce_bn = nn.BatchNorm2d(128, momentum=0.1)
        self.inception_4d_relu_3x3_reduce = nn.ReLU()
        self.inception_4d_3x3 = nn.Conv2d(
            128, 192, kernel_size=(
                3, 3), stride=(
                1, 1), padding=(
                1, 1), dilation=1, groups=1, bias=True)
        self.inception_4d_3x3_bn = nn.BatchNorm2d(192, momentum=0.1)
        self.inception_4d_relu_3x3 = nn.ReLU()
        self.inception_4d_double_3x3_reduce = nn.Conv2d(
            608, 160, kernel_size=(
                1, 1), stride=(
                1, 1), padding=(
                0, 0), dilation=1, groups=1, bias=True)
        self.inception_4d_double_3x3_reduce_bn = nn.BatchNorm2d(
            160, momentum=0.1)
        self.inception_4d_relu_double_3x3_reduce = nn.ReLU()
        self.inception_4d_double_3x3_1 = nn.Conv2d(
            160, 192, kernel_size=(
                3, 3), stride=(
                1, 1), padding=(
                1, 1), dilation=1, groups=1, bias=True)
        self.inception_4d_double_3x3_1_bn = nn.BatchNorm2d(192, momentum=0.1)
        self.inception_4d_relu_double_3x3_1 = nn.ReLU()
        self.inception_4d_double_3x3_2 = nn.Conv2d(
            192, 192, kernel_size=(
                3, 3), stride=(
                1, 1), padding=(
                1, 1), dilation=1, groups=1, bias=True)
        self.inception_4d_double_3x3_2_bn = nn.BatchNorm2d(192, momentum=0.1)
        self.inception_4d_relu_double_3x3_2 = nn.ReLU()
        self.inception_4d_pool = nn.AvgPool2d(
            kernel_size=(
                3, 3), stride=(
                1, 1), padding=(
                1, 1), ceil_mode=True)
        self.inception_4d_pool_proj = nn.Conv2d(
            608, 128, kernel_size=(
                1, 1), stride=(
                1, 1), padding=(
                0, 0), dilation=1, groups=1, bias=True)
        self.inception_4d_pool_proj_bn = nn.BatchNorm2d(128, momentum=0.1)
        self.inception_4d_relu_pool_proj = nn.ReLU()
        self.inception_4e_3x3_reduce = nn.Conv2d(
            608, 128, kernel_size=(
                1, 1), stride=(
                1, 1), padding=(
                0, 0), dilation=1, groups=1, bias=True)
        self.inception_4e_3x3_reduce_bn = nn.BatchNorm2d(128, momentum=0.1)
        self.inception_4e_relu_3x3_reduce = nn.ReLU()
        self.inception_4e_3x3 = nn.Conv2d(
            128, 192, kernel_size=(
                3, 3), stride=(
                2, 2), padding=(
                1, 1), dilation=1, groups=1, bias=True)
        self.inception_4e_3x3_bn = nn.BatchNorm2d(192, momentum=0.1)
        self.inception_4e_relu_3x3 = nn.ReLU()
        self.inception_4e_double_3x3_reduce = nn.Conv2d(
            608, 192, kernel_size=(
                1, 1), stride=(
                1, 1), padding=(
                0, 0), dilation=1, groups=1, bias=True)
        self.inception_4e_double_3x3_reduce_bn = nn.BatchNorm2d(
            192, momentum=0.1)
        self.inception_4e_relu_double_3x3_reduce = nn.ReLU()
        self.inception_4e_double_3x3_1 = nn.Conv2d(
            192, 256, kernel_size=(
                3, 3), stride=(
                1, 1), padding=(
                1, 1), dilation=1, groups=1, bias=True)
        self.inception_4e_double_3x3_1_bn = nn.BatchNorm2d(256, momentum=0.1)
        self.inception_4e_relu_double_3x3_1 = nn.ReLU()
        self.inception_4e_double_3x3_2 = nn.Conv2d(
            256, 256, kernel_size=(
                3, 3), stride=(
                2, 2), padding=(
                1, 1), dilation=1, groups=1, bias=True)
        self.inception_4e_double_3x3_2_bn = nn.BatchNorm2d(256, momentum=0.1)
        self.inception_4e_relu_double_3x3_2 = nn.ReLU()
        self.inception_4e_pool = nn.MaxPool2d(
            kernel_size=(
                3, 3), stride=(
                2, 2), padding=(
                0, 0), ceil_mode=True)
        self.inception_5a_1x1 = nn.Conv2d(
            1056, 352, kernel_size=(
                1, 1), stride=(
                1, 1), padding=(
                0, 0), dilation=1, groups=1, bias=True)
        self.inception_5a_1x1_bn = nn.BatchNorm2d(352, momentum=0.1)
        self.inception_5a_relu_1x1 = nn.ReLU()
        self.inception_5a_3x3_reduce = nn.Conv2d(
            1056, 192, kernel_size=(
                1, 1), stride=(
                1, 1), padding=(
                0, 0), dilation=1, groups=1, bias=True)
        self.inception_5a_3x3_reduce_bn = nn.BatchNorm2d(192, momentum=0.1)
        self.inception_5a_relu_3x3_reduce = nn.ReLU()
        self.inception_5a_3x3 = nn.Conv2d(
            192, 320, kernel_size=(
                3, 3), stride=(
                1, 1), padding=(
                1, 1), dilation=1, groups=1, bias=True)
        self.inception_5a_3x3_bn = nn.BatchNorm2d(320, momentum=0.1)
        self.inception_5a_relu_3x3 = nn.ReLU()
        self.inception_5a_double_3x3_reduce = nn.Conv2d(
            1056, 160, kernel_size=(
                1, 1), stride=(
                1, 1), padding=(
                0, 0), dilation=1, groups=1, bias=True)
        self.inception_5a_double_3x3_reduce_bn = nn.BatchNorm2d(
            160, momentum=0.1)
        self.inception_5a_relu_double_3x3_reduce = nn.ReLU()
        self.inception_5a_double_3x3_1 = nn.Conv2d(
            160, 224, kernel_size=(
                3, 3), stride=(
                1, 1), padding=(
                1, 1), dilation=1, groups=1, bias=True)
        self.inception_5a_double_3x3_1_bn = nn.BatchNorm2d(224, momentum=0.1)
        self.inception_5a_relu_double_3x3_1 = nn.ReLU()
        self.inception_5a_double_3x3_2 = nn.Conv2d(
            224, 224, kernel_size=(
                3, 3), stride=(
                1, 1), padding=(
                1, 1), dilation=1, groups=1, bias=True)
        self.inception_5a_double_3x3_2_bn = nn.BatchNorm2d(224, momentum=0.1)
        self.inception_5a_relu_double_3x3_2 = nn.ReLU()
        self.inception_5a_pool = nn.AvgPool2d(
            kernel_size=(
                3, 3), stride=(
                1, 1), padding=(
                1, 1), ceil_mode=True)
        self.inception_5a_pool_proj = nn.Conv2d(
            1056, 128, kernel_size=(
                1, 1), stride=(
                1, 1), padding=(
                0, 0), dilation=1, groups=1, bias=True)
        self.inception_5a_pool_proj_bn = nn.BatchNorm2d(128, momentum=0.1)
        self.inception_5a_relu_pool_proj = nn.ReLU()
        self.inception_5b_1x1 = nn.Conv2d(
            1024, 352, kernel_size=(
                1, 1), stride=(
                1, 1), padding=(
                0, 0), dilation=1, groups=1, bias=True)
        self.inception_5b_1x1_bn = nn.BatchNorm2d(352, momentum=0.1)
        self.inception_5b_relu_1x1 = nn.ReLU()
        self.inception_5b_3x3_reduce = nn.Conv2d(
            1024, 192, kernel_size=(
                1, 1), stride=(
                1, 1), padding=(
                0, 0), dilation=1, groups=1, bias=True)
        self.inception_5b_3x3_reduce_bn = nn.BatchNorm2d(192, momentum=0.1)
        self.inception_5b_relu_3x3_reduce = nn.ReLU()
        self.inception_5b_3x3 = nn.Conv2d(
            192, 320, kernel_size=(
                3, 3), stride=(
                1, 1), padding=(
                1, 1), dilation=1, groups=1, bias=True)
        self.inception_5b_3x3_bn = nn.BatchNorm2d(320, momentum=0.1)
        self.inception_5b_relu_3x3 = nn.ReLU()
        self.inception_5b_double_3x3_reduce = nn.Conv2d(
            1024, 192, kernel_size=(
                1, 1), stride=(
                1, 1), padding=(
                0, 0), dilation=1, groups=1, bias=True)
        self.inception_5b_double_3x3_reduce_bn = nn.BatchNorm2d(
            192, momentum=0.1)
        self.inception_5b_relu_double_3x3_reduce = nn.ReLU()
        self.inception_5b_double_3x3_1 = nn.Conv2d(
            192, 224, kernel_size=(
                3, 3), stride=(
                1, 1), padding=(
                1, 1), dilation=1, groups=1, bias=True)
        self.inception_5b_double_3x3_1_bn = nn.BatchNorm2d(224, momentum=0.1)
        self.inception_5b_relu_double_3x3_1 = nn.ReLU()
        self.inception_5b_double_3x3_2 = nn.Conv2d(
            224, 224, kernel_size=(
                3, 3), stride=(
                1, 1), padding=(
                1, 1), dilation=1, groups=1, bias=True)
        self.inception_5b_double_3x3_2_bn = nn.BatchNorm2d(224, momentum=0.1)
        self.inception_5b_relu_double_3x3_2 = nn.ReLU()
        self.inception_5b_pool = nn.MaxPool2d(
            kernel_size=(
                3, 3), stride=(
                1, 1), padding=(
                1, 1), ceil_mode=True)
        self.inception_5b_pool_proj = nn.Conv2d(
            1024, 128, kernel_size=(
                1, 1), stride=(
                1, 1), padding=(
                0, 0), dilation=1, groups=1, bias=True)
        self.inception_5b_pool_proj_bn = nn.BatchNorm2d(128, momentum=0.1)
        self.inception_5b_relu_pool_proj = nn.ReLU()
        # self.global_pool = nn.AvgPool2d(kernel_size=(1, 1), stride=(1, 1), padding=(0, 0), ceil_mode=True)
        self.dropout = nn.Dropout(0.699999988079)
        self.flatten = nn.Flatten()
        self.fc_action = nn.Linear(1024, 200)

        if pretrained_model:
            state_dict = torch.load(get_bn_inception_pretrained_model())
            self.load_state_dict(state_dict)

    def forward(self, data):
        conv1_7x7_s2 = self.conv1_7x7_s2(data)
        conv1_7x7_s2_bn = self.conv1_7x7_s2_bn(conv1_7x7_s2)
        conv1_7x7_s2_bn = self.conv1_relu_7x7(conv1_7x7_s2_bn)
        pool1_3x3_s2 = self.pool1_3x3_s2(conv1_7x7_s2_bn)
        conv2_3x3_reduce = self.conv2_3x3_reduce(pool1_3x3_s2)
        conv2_3x3_reduce_bn = self.conv2_3x3_reduce_bn(conv2_3x3_reduce)
        conv2_3x3_reduce_bn = self.conv2_relu_3x3_reduce(conv2_3x3_reduce_bn)
        conv2_3x3 = self.conv2_3x3(conv2_3x3_reduce_bn)
        conv2_3x3_bn = self.conv2_3x3_bn(conv2_3x3)
        conv2_3x3_bn = self.conv2_relu_3x3(conv2_3x3_bn)
        pool2_3x3_s2 = self.pool2_3x3_s2(conv2_3x3_bn)
        pool2_3x3_s2_pool2_3x3_s2_0_split_0 = pool2_3x3_s2
        pool2_3x3_s2_pool2_3x3_s2_0_split_1 = pool2_3x3_s2
        pool2_3x3_s2_pool2_3x3_s2_0_split_2 = pool2_3x3_s2
        pool2_3x3_s2_pool2_3x3_s2_0_split_3 = pool2_3x3_s2
        inception_3a_1x1 = self.inception_3a_1x1(
            pool2_3x3_s2_pool2_3x3_s2_0_split_0)
        inception_3a_1x1_bn = self.inception_3a_1x1_bn(inception_3a_1x1)
        inception_3a_1x1_bn = self.inception_3a_relu_1x1(inception_3a_1x1_bn)
        inception_3a_3x3_reduce = self.inception_3a_3x3_reduce(
            pool2_3x3_s2_pool2_3x3_s2_0_split_1)
        inception_3a_3x3_reduce_bn = self.inception_3a_3x3_reduce_bn(
            inception_3a_3x3_reduce)
        inception_3a_3x3_reduce_bn = self.inception_3a_relu_3x3_reduce(
            inception_3a_3x3_reduce_bn)
        inception_3a_3x3 = self.inception_3a_3x3(inception_3a_3x3_reduce_bn)
        inception_3a_3x3_bn = self.inception_3a_3x3_bn(inception_3a_3x3)
        inception_3a_3x3_bn = self.inception_3a_relu_3x3(inception_3a_3x3_bn)
        inception_3a_double_3x3_reduce = self.inception_3a_double_3x3_reduce(
            pool2_3x3_s2_pool2_3x3_s2_0_split_2)
        inception_3a_double_3x3_reduce_bn = self.inception_3a_double_3x3_reduce_bn(
            inception_3a_double_3x3_reduce)
        inception_3a_double_3x3_reduce_bn = self.inception_3a_relu_double_3x3_reduce(
            inception_3a_double_3x3_reduce_bn)
        inception_3a_double_3x3_1 = self.inception_3a_double_3x3_1(
            inception_3a_double_3x3_reduce_bn)
        inception_3a_double_3x3_1_bn = self.inception_3a_double_3x3_1_bn(
            inception_3a_double_3x3_1)
        inception_3a_double_3x3_1_bn = self.inception_3a_relu_double_3x3_1(
            inception_3a_double_3x3_1_bn)
        inception_3a_double_3x3_2 = self.inception_3a_double_3x3_2(
            inception_3a_double_3x3_1_bn)
        inception_3a_double_3x3_2_bn = self.inception_3a_double_3x3_2_bn(
            inception_3a_double_3x3_2)
        inception_3a_double_3x3_2_bn = self.inception_3a_relu_double_3x3_2(
            inception_3a_double_3x3_2_bn)
        inception_3a_pool = self.inception_3a_pool(
            pool2_3x3_s2_pool2_3x3_s2_0_split_3)
        inception_3a_pool_proj = self.inception_3a_pool_proj(inception_3a_pool)
        inception_3a_pool_proj_bn = self.inception_3a_pool_proj_bn(
            inception_3a_pool_proj)
        inception_3a_pool_proj_bn = self.inception_3a_relu_pool_proj(
            inception_3a_pool_proj_bn)
        inception_3a_output = torch.cat(
            (inception_3a_1x1_bn,
             inception_3a_3x3_bn,
             inception_3a_double_3x3_2_bn,
             inception_3a_pool_proj_bn),
            dim=1)
        inception_3a_output_inception_3a_output_0_split_0 = inception_3a_output
        inception_3a_output_inception_3a_output_0_split_1 = inception_3a_output
        inception_3a_output_inception_3a_output_0_split_2 = inception_3a_output
        inception_3a_output_inception_3a_output_0_split_3 = inception_3a_output
        inception_3b_1x1 = self.inception_3b_1x1(
            inception_3a_output_inception_3a_output_0_split_0)
        inception_3b_1x1_bn = self.inception_3b_1x1_bn(inception_3b_1x1)
        inception_3b_1x1_bn = self.inception_3b_relu_1x1(inception_3b_1x1_bn)
        inception_3b_3x3_reduce = self.inception_3b_3x3_reduce(
            inception_3a_output_inception_3a_output_0_split_1)
        inception_3b_3x3_reduce_bn = self.inception_3b_3x3_reduce_bn(
            inception_3b_3x3_reduce)
        inception_3b_3x3_reduce_bn = self.inception_3b_relu_3x3_reduce(
            inception_3b_3x3_reduce_bn)
        inception_3b_3x3 = self.inception_3b_3x3(inception_3b_3x3_reduce_bn)
        inception_3b_3x3_bn = self.inception_3b_3x3_bn(inception_3b_3x3)
        inception_3b_3x3_bn = self.inception_3b_relu_3x3(inception_3b_3x3_bn)
        inception_3b_double_3x3_reduce = self.inception_3b_double_3x3_reduce(
            inception_3a_output_inception_3a_output_0_split_2)
        inception_3b_double_3x3_reduce_bn = self.inception_3b_double_3x3_reduce_bn(
            inception_3b_double_3x3_reduce)
        inception_3b_double_3x3_reduce_bn = self.inception_3b_relu_double_3x3_reduce(
            inception_3b_double_3x3_reduce_bn)
        inception_3b_double_3x3_1 = self.inception_3b_double_3x3_1(
            inception_3b_double_3x3_reduce_bn)
        inception_3b_double_3x3_1_bn = self.inception_3b_double_3x3_1_bn(
            inception_3b_double_3x3_1)
        inception_3b_double_3x3_1_bn = self.inception_3b_relu_double_3x3_1(
            inception_3b_double_3x3_1_bn)
        inception_3b_double_3x3_2 = self.inception_3b_double_3x3_2(
            inception_3b_double_3x3_1_bn)
        inception_3b_double_3x3_2_bn = self.inception_3b_double_3x3_2_bn(
            inception_3b_double_3x3_2)
        inception_3b_double_3x3_2_bn = self.inception_3b_relu_double_3x3_2(
            inception_3b_double_3x3_2_bn)
        inception_3b_pool = self.inception_3b_pool(
            inception_3a_output_inception_3a_output_0_split_3)
        inception_3b_pool_proj = self.inception_3b_pool_proj(inception_3b_pool)
        inception_3b_pool_proj_bn = self.inception_3b_pool_proj_bn(
            inception_3b_pool_proj)
        inception_3b_pool_proj_bn = self.inception_3b_relu_pool_proj(
            inception_3b_pool_proj_bn)
        inception_3b_output = torch.cat(
            (inception_3b_1x1_bn,
             inception_3b_3x3_bn,
             inception_3b_double_3x3_2_bn,
             inception_3b_pool_proj_bn),
            dim=1)
        inception_3b_output_inception_3b_output_0_split_0 = inception_3b_output
        inception_3b_output_inception_3b_output_0_split_1 = inception_3b_output
        inception_3b_output_inception_3b_output_0_split_2 = inception_3b_output
        inception_3c_3x3_reduce = self.inception_3c_3x3_reduce(
            inception_3b_output_inception_3b_output_0_split_0)
        inception_3c_3x3_reduce_bn = self.inception_3c_3x3_reduce_bn(
            inception_3c_3x3_reduce)
        inception_3c_3x3_reduce_bn = self.inception_3c_relu_3x3_reduce(
            inception_3c_3x3_reduce_bn)
        inception_3c_3x3 = self.inception_3c_3x3(inception_3c_3x3_reduce_bn)
        inception_3c_3x3_bn = self.inception_3c_3x3_bn(inception_3c_3x3)
        inception_3c_3x3_bn = self.inception_3c_relu_3x3(inception_3c_3x3_bn)
        inception_3c_double_3x3_reduce = self.inception_3c_double_3x3_reduce(
            inception_3b_output_inception_3b_output_0_split_1)
        inception_3c_double_3x3_reduce_bn = self.inception_3c_double_3x3_reduce_bn(
            inception_3c_double_3x3_reduce)
        inception_3c_double_3x3_reduce_bn = self.inception_3c_relu_double_3x3_reduce(
            inception_3c_double_3x3_reduce_bn)
        inception_3c_double_3x3_1 = self.inception_3c_double_3x3_1(
            inception_3c_double_3x3_reduce_bn)
        inception_3c_double_3x3_1_bn = self.inception_3c_double_3x3_1_bn(
            inception_3c_double_3x3_1)
        inception_3c_double_3x3_1_bn = self.inception_3c_relu_double_3x3_1(
            inception_3c_double_3x3_1_bn)
        inception_3c_double_3x3_2 = self.inception_3c_double_3x3_2(
            inception_3c_double_3x3_1_bn)
        inception_3c_double_3x3_2_bn = self.inception_3c_double_3x3_2_bn(
            inception_3c_double_3x3_2)
        inception_3c_double_3x3_2_bn = self.inception_3c_relu_double_3x3_2(
            inception_3c_double_3x3_2_bn)
        inception_3c_pool = self.inception_3c_pool(
            inception_3b_output_inception_3b_output_0_split_2)
        inception_3c_output = torch.cat(
            (inception_3c_3x3_bn,
             inception_3c_double_3x3_2_bn,
             inception_3c_pool),
            dim=1)
        inception_3c_output_inception_3c_output_0_split_0 = inception_3c_output
        inception_3c_output_inception_3c_output_0_split_1 = inception_3c_output
        inception_3c_output_inception_3c_output_0_split_2 = inception_3c_output
        inception_3c_output_inception_3c_output_0_split_3 = inception_3c_output
        inception_4a_1x1 = self.inception_4a_1x1(
            inception_3c_output_inception_3c_output_0_split_0)
        inception_4a_1x1_bn = self.inception_4a_1x1_bn(inception_4a_1x1)
        inception_4a_1x1_bn = self.inception_4a_relu_1x1(inception_4a_1x1_bn)
        inception_4a_3x3_reduce = self.inception_4a_3x3_reduce(
            inception_3c_output_inception_3c_output_0_split_1)
        inception_4a_3x3_reduce_bn = self.inception_4a_3x3_reduce_bn(
            inception_4a_3x3_reduce)
        inception_4a_3x3_reduce_bn = self.inception_4a_relu_3x3_reduce(
            inception_4a_3x3_reduce_bn)
        inception_4a_3x3 = self.inception_4a_3x3(inception_4a_3x3_reduce_bn)
        inception_4a_3x3_bn = self.inception_4a_3x3_bn(inception_4a_3x3)
        inception_4a_3x3_bn = self.inception_4a_relu_3x3(inception_4a_3x3_bn)
        inception_4a_double_3x3_reduce = self.inception_4a_double_3x3_reduce(
            inception_3c_output_inception_3c_output_0_split_2)
        inception_4a_double_3x3_reduce_bn = self.inception_4a_double_3x3_reduce_bn(
            inception_4a_double_3x3_reduce)
        inception_4a_double_3x3_reduce_bn = self.inception_4a_relu_double_3x3_reduce(
            inception_4a_double_3x3_reduce_bn)
        inception_4a_double_3x3_1 = self.inception_4a_double_3x3_1(
            inception_4a_double_3x3_reduce_bn)
        inception_4a_double_3x3_1_bn = self.inception_4a_double_3x3_1_bn(
            inception_4a_double_3x3_1)
        inception_4a_double_3x3_1_bn = self.inception_4a_relu_double_3x3_1(
            inception_4a_double_3x3_1_bn)
        inception_4a_double_3x3_2 = self.inception_4a_double_3x3_2(
            inception_4a_double_3x3_1_bn)
        inception_4a_double_3x3_2_bn = self.inception_4a_double_3x3_2_bn(
            inception_4a_double_3x3_2)
        inception_4a_double_3x3_2_bn = self.inception_4a_relu_double_3x3_2(
            inception_4a_double_3x3_2_bn)
        inception_4a_pool = self.inception_4a_pool(
            inception_3c_output_inception_3c_output_0_split_3)
        inception_4a_pool_proj = self.inception_4a_pool_proj(inception_4a_pool)
        inception_4a_pool_proj_bn = self.inception_4a_pool_proj_bn(
            inception_4a_pool_proj)
        inception_4a_pool_proj_bn = self.inception_4a_relu_pool_proj(
            inception_4a_pool_proj_bn)
        inception_4a_output = torch.cat(
            (inception_4a_1x1_bn,
             inception_4a_3x3_bn,
             inception_4a_double_3x3_2_bn,
             inception_4a_pool_proj_bn),
            dim=1)
        inception_4a_output_inception_4a_output_0_split_0 = inception_4a_output
        inception_4a_output_inception_4a_output_0_split_1 = inception_4a_output
        inception_4a_output_inception_4a_output_0_split_2 = inception_4a_output
        inception_4a_output_inception_4a_output_0_split_3 = inception_4a_output
        inception_4b_1x1 = self.inception_4b_1x1(
            inception_4a_output_inception_4a_output_0_split_0)
        inception_4b_1x1_bn = self.inception_4b_1x1_bn(inception_4b_1x1)
        inception_4b_1x1_bn = self.inception_4b_relu_1x1(inception_4b_1x1_bn)
        inception_4b_3x3_reduce = self.inception_4b_3x3_reduce(
            inception_4a_output_inception_4a_output_0_split_1)
        inception_4b_3x3_reduce_bn = self.inception_4b_3x3_reduce_bn(
            inception_4b_3x3_reduce)
        inception_4b_3x3_reduce_bn = self.inception_4b_relu_3x3_reduce(
            inception_4b_3x3_reduce_bn)
        inception_4b_3x3 = self.inception_4b_3x3(inception_4b_3x3_reduce_bn)
        inception_4b_3x3_bn = self.inception_4b_3x3_bn(inception_4b_3x3)
        inception_4b_3x3_bn = self.inception_4b_relu_3x3(inception_4b_3x3_bn)
        inception_4b_double_3x3_reduce = self.inception_4b_double_3x3_reduce(
            inception_4a_output_inception_4a_output_0_split_2)
        inception_4b_double_3x3_reduce_bn = self.inception_4b_double_3x3_reduce_bn(
            inception_4b_double_3x3_reduce)
        inception_4b_double_3x3_reduce_bn = self.inception_4b_relu_double_3x3_reduce(
            inception_4b_double_3x3_reduce_bn)
        inception_4b_double_3x3_1 = self.inception_4b_double_3x3_1(
            inception_4b_double_3x3_reduce_bn)
        inception_4b_double_3x3_1_bn = self.inception_4b_double_3x3_1_bn(
            inception_4b_double_3x3_1)
        inception_4b_double_3x3_1_bn = self.inception_4b_relu_double_3x3_1(
            inception_4b_double_3x3_1_bn)
        inception_4b_double_3x3_2 = self.inception_4b_double_3x3_2(
            inception_4b_double_3x3_1_bn)
        inception_4b_double_3x3_2_bn = self.inception_4b_double_3x3_2_bn(
            inception_4b_double_3x3_2)
        inception_4b_double_3x3_2_bn = self.inception_4b_relu_double_3x3_2(
            inception_4b_double_3x3_2_bn)
        inception_4b_pool = self.inception_4b_pool(
            inception_4a_output_inception_4a_output_0_split_3)
        inception_4b_pool_proj = self.inception_4b_pool_proj(inception_4b_pool)
        inception_4b_pool_proj_bn = self.inception_4b_pool_proj_bn(
            inception_4b_pool_proj)
        inception_4b_pool_proj_bn = self.inception_4b_relu_pool_proj(
            inception_4b_pool_proj_bn)
        inception_4b_output = torch.cat(
            (inception_4b_1x1_bn,
             inception_4b_3x3_bn,
             inception_4b_double_3x3_2_bn,
             inception_4b_pool_proj_bn),
            dim=1)
        inception_4b_output_inception_4b_output_0_split_0 = inception_4b_output
        inception_4b_output_inception_4b_output_0_split_1 = inception_4b_output
        inception_4b_output_inception_4b_output_0_split_2 = inception_4b_output
        inception_4b_output_inception_4b_output_0_split_3 = inception_4b_output
        inception_4c_1x1 = self.inception_4c_1x1(
            inception_4b_output_inception_4b_output_0_split_0)
        inception_4c_1x1_bn = self.inception_4c_1x1_bn(inception_4c_1x1)
        inception_4c_1x1_bn = self.inception_4c_relu_1x1(inception_4c_1x1_bn)
        inception_4c_3x3_reduce = self.inception_4c_3x3_reduce(
            inception_4b_output_inception_4b_output_0_split_1)
        inception_4c_3x3_reduce_bn = self.inception_4c_3x3_reduce_bn(
            inception_4c_3x3_reduce)
        inception_4c_3x3_reduce_bn = self.inception_4c_relu_3x3_reduce(
            inception_4c_3x3_reduce_bn)
        inception_4c_3x3 = self.inception_4c_3x3(inception_4c_3x3_reduce_bn)
        inception_4c_3x3_bn = self.inception_4c_3x3_bn(inception_4c_3x3)
        inception_4c_3x3_bn = self.inception_4c_relu_3x3(inception_4c_3x3_bn)
        inception_4c_double_3x3_reduce = self.inception_4c_double_3x3_reduce(
            inception_4b_output_inception_4b_output_0_split_2)
        inception_4c_double_3x3_reduce_bn = self.inception_4c_double_3x3_reduce_bn(
            inception_4c_double_3x3_reduce)
        inception_4c_double_3x3_reduce_bn = self.inception_4c_relu_double_3x3_reduce(
            inception_4c_double_3x3_reduce_bn)
        inception_4c_double_3x3_1 = self.inception_4c_double_3x3_1(
            inception_4c_double_3x3_reduce_bn)
        inception_4c_double_3x3_1_bn = self.inception_4c_double_3x3_1_bn(
            inception_4c_double_3x3_1)
        inception_4c_double_3x3_1_bn = self.inception_4c_relu_double_3x3_1(
            inception_4c_double_3x3_1_bn)
        inception_4c_double_3x3_2 = self.inception_4c_double_3x3_2(
            inception_4c_double_3x3_1_bn)
        inception_4c_double_3x3_2_bn = self.inception_4c_double_3x3_2_bn(
            inception_4c_double_3x3_2)
        inception_4c_double_3x3_2_bn = self.inception_4c_relu_double_3x3_2(
            inception_4c_double_3x3_2_bn)
        inception_4c_pool = self.inception_4c_pool(
            inception_4b_output_inception_4b_output_0_split_3)
        inception_4c_pool_proj = self.inception_4c_pool_proj(inception_4c_pool)
        inception_4c_pool_proj_bn = self.inception_4c_pool_proj_bn(
            inception_4c_pool_proj)
        inception_4c_pool_proj_bn = self.inception_4c_relu_pool_proj(
            inception_4c_pool_proj_bn)
        inception_4c_output = torch.cat(
            (inception_4c_1x1_bn,
             inception_4c_3x3_bn,
             inception_4c_double_3x3_2_bn,
             inception_4c_pool_proj_bn),
            dim=1)
        inception_4c_output_inception_4c_output_0_split_0 = inception_4c_output
        inception_4c_output_inception_4c_output_0_split_1 = inception_4c_output
        inception_4c_output_inception_4c_output_0_split_2 = inception_4c_output
        inception_4c_output_inception_4c_output_0_split_3 = inception_4c_output
        inception_4d_1x1 = self.inception_4d_1x1(
            inception_4c_output_inception_4c_output_0_split_0)
        inception_4d_1x1_bn = self.inception_4d_1x1_bn(inception_4d_1x1)
        inception_4d_1x1_bn = self.inception_4d_relu_1x1(inception_4d_1x1_bn)
        inception_4d_3x3_reduce = self.inception_4d_3x3_reduce(
            inception_4c_output_inception_4c_output_0_split_1)
        inception_4d_3x3_reduce_bn = self.inception_4d_3x3_reduce_bn(
            inception_4d_3x3_reduce)
        inception_4d_3x3_reduce_bn = self.inception_4d_relu_3x3_reduce(
            inception_4d_3x3_reduce_bn)
        inception_4d_3x3 = self.inception_4d_3x3(inception_4d_3x3_reduce_bn)
        inception_4d_3x3_bn = self.inception_4d_3x3_bn(inception_4d_3x3)
        inception_4d_3x3_bn = self.inception_4d_relu_3x3(inception_4d_3x3_bn)
        inception_4d_double_3x3_reduce = self.inception_4d_double_3x3_reduce(
            inception_4c_output_inception_4c_output_0_split_2)
        inception_4d_double_3x3_reduce_bn = self.inception_4d_double_3x3_reduce_bn(
            inception_4d_double_3x3_reduce)
        inception_4d_double_3x3_reduce_bn = self.inception_4d_relu_double_3x3_reduce(
            inception_4d_double_3x3_reduce_bn)
        inception_4d_double_3x3_1 = self.inception_4d_double_3x3_1(
            inception_4d_double_3x3_reduce_bn)
        inception_4d_double_3x3_1_bn = self.inception_4d_double_3x3_1_bn(
            inception_4d_double_3x3_1)
        inception_4d_double_3x3_1_bn = self.inception_4d_relu_double_3x3_1(
            inception_4d_double_3x3_1_bn)
        inception_4d_double_3x3_2 = self.inception_4d_double_3x3_2(
            inception_4d_double_3x3_1_bn)
        inception_4d_double_3x3_2_bn = self.inception_4d_double_3x3_2_bn(
            inception_4d_double_3x3_2)
        inception_4d_double_3x3_2_bn = self.inception_4d_relu_double_3x3_2(
            inception_4d_double_3x3_2_bn)
        inception_4d_pool = self.inception_4d_pool(
            inception_4c_output_inception_4c_output_0_split_3)
        inception_4d_pool_proj = self.inception_4d_pool_proj(inception_4d_pool)
        inception_4d_pool_proj_bn = self.inception_4d_pool_proj_bn(
            inception_4d_pool_proj)
        inception_4d_pool_proj_bn = self.inception_4d_relu_pool_proj(
            inception_4d_pool_proj_bn)
        inception_4d_output = torch.cat(
            (inception_4d_1x1_bn,
             inception_4d_3x3_bn,
             inception_4d_double_3x3_2_bn,
             inception_4d_pool_proj_bn),
            dim=1)
        inception_4d_output_inception_4d_output_0_split_0 = inception_4d_output
        inception_4d_output_inception_4d_output_0_split_1 = inception_4d_output
        inception_4d_output_inception_4d_output_0_split_2 = inception_4d_output
        inception_4e_3x3_reduce = self.inception_4e_3x3_reduce(
            inception_4d_output_inception_4d_output_0_split_0)
        inception_4e_3x3_reduce_bn = self.inception_4e_3x3_reduce_bn(
            inception_4e_3x3_reduce)
        inception_4e_3x3_reduce_bn = self.inception_4e_relu_3x3_reduce(
            inception_4e_3x3_reduce_bn)
        inception_4e_3x3 = self.inception_4e_3x3(inception_4e_3x3_reduce_bn)
        inception_4e_3x3_bn = self.inception_4e_3x3_bn(inception_4e_3x3)
        inception_4e_3x3_bn = self.inception_4e_relu_3x3(inception_4e_3x3_bn)
        inception_4e_double_3x3_reduce = self.inception_4e_double_3x3_reduce(
            inception_4d_output_inception_4d_output_0_split_1)
        inception_4e_double_3x3_reduce_bn = self.inception_4e_double_3x3_reduce_bn(
            inception_4e_double_3x3_reduce)
        inception_4e_double_3x3_reduce_bn = self.inception_4e_relu_double_3x3_reduce(
            inception_4e_double_3x3_reduce_bn)
        inception_4e_double_3x3_1 = self.inception_4e_double_3x3_1(
            inception_4e_double_3x3_reduce_bn)
        inception_4e_double_3x3_1_bn = self.inception_4e_double_3x3_1_bn(
            inception_4e_double_3x3_1)
        inception_4e_double_3x3_1_bn = self.inception_4e_relu_double_3x3_1(
            inception_4e_double_3x3_1_bn)
        inception_4e_double_3x3_2 = self.inception_4e_double_3x3_2(
            inception_4e_double_3x3_1_bn)
        inception_4e_double_3x3_2_bn = self.inception_4e_double_3x3_2_bn(
            inception_4e_double_3x3_2)
        inception_4e_double_3x3_2_bn = self.inception_4e_relu_double_3x3_2(
            inception_4e_double_3x3_2_bn)
        inception_4e_pool = self.inception_4e_pool(
            inception_4d_output_inception_4d_output_0_split_2)
        inception_4e_output = torch.cat(
            (inception_4e_3x3_bn,
             inception_4e_double_3x3_2_bn,
             inception_4e_pool),
            dim=1)
        inception_4e_output_inception_4e_output_0_split_0 = inception_4e_output
        inception_4e_output_inception_4e_output_0_split_1 = inception_4e_output
        inception_4e_output_inception_4e_output_0_split_2 = inception_4e_output
        inception_4e_output_inception_4e_output_0_split_3 = inception_4e_output
        inception_5a_1x1 = self.inception_5a_1x1(
            inception_4e_output_inception_4e_output_0_split_0)
        inception_5a_1x1_bn = self.inception_5a_1x1_bn(inception_5a_1x1)
        inception_5a_1x1_bn = self.inception_5a_relu_1x1(inception_5a_1x1_bn)
        inception_5a_3x3_reduce = self.inception_5a_3x3_reduce(
            inception_4e_output_inception_4e_output_0_split_1)
        inception_5a_3x3_reduce_bn = self.inception_5a_3x3_reduce_bn(
            inception_5a_3x3_reduce)
        inception_5a_3x3_reduce_bn = self.inception_5a_relu_3x3_reduce(
            inception_5a_3x3_reduce_bn)
        inception_5a_3x3 = self.inception_5a_3x3(inception_5a_3x3_reduce_bn)
        inception_5a_3x3_bn = self.inception_5a_3x3_bn(inception_5a_3x3)
        inception_5a_3x3_bn = self.inception_5a_relu_3x3(inception_5a_3x3_bn)
        inception_5a_double_3x3_reduce = self.inception_5a_double_3x3_reduce(
            inception_4e_output_inception_4e_output_0_split_2)
        inception_5a_double_3x3_reduce_bn = self.inception_5a_double_3x3_reduce_bn(
            inception_5a_double_3x3_reduce)
        inception_5a_double_3x3_reduce_bn = self.inception_5a_relu_double_3x3_reduce(
            inception_5a_double_3x3_reduce_bn)
        inception_5a_double_3x3_1 = self.inception_5a_double_3x3_1(
            inception_5a_double_3x3_reduce_bn)
        inception_5a_double_3x3_1_bn = self.inception_5a_double_3x3_1_bn(
            inception_5a_double_3x3_1)
        inception_5a_double_3x3_1_bn = self.inception_5a_relu_double_3x3_1(
            inception_5a_double_3x3_1_bn)
        inception_5a_double_3x3_2 = self.inception_5a_double_3x3_2(
            inception_5a_double_3x3_1_bn)
        inception_5a_double_3x3_2_bn = self.inception_5a_double_3x3_2_bn(
            inception_5a_double_3x3_2)
        inception_5a_double_3x3_2_bn = self.inception_5a_relu_double_3x3_2(
            inception_5a_double_3x3_2_bn)
        inception_5a_pool = self.inception_5a_pool(
            inception_4e_output_inception_4e_output_0_split_3)
        inception_5a_pool_proj = self.inception_5a_pool_proj(inception_5a_pool)
        inception_5a_pool_proj_bn = self.inception_5a_pool_proj_bn(
            inception_5a_pool_proj)
        inception_5a_pool_proj_bn = self.inception_5a_relu_pool_proj(
            inception_5a_pool_proj_bn)
        inception_5a_output = torch.cat(
            (inception_5a_1x1_bn,
             inception_5a_3x3_bn,
             inception_5a_double_3x3_2_bn,
             inception_5a_pool_proj_bn),
            dim=1)
        inception_5a_output_inception_5a_output_0_split_0 = inception_5a_output
        inception_5a_output_inception_5a_output_0_split_1 = inception_5a_output
        inception_5a_output_inception_5a_output_0_split_2 = inception_5a_output
        inception_5a_output_inception_5a_output_0_split_3 = inception_5a_output
        inception_5b_1x1 = self.inception_5b_1x1(
            inception_5a_output_inception_5a_output_0_split_0)
        inception_5b_1x1_bn = self.inception_5b_1x1_bn(inception_5b_1x1)
        inception_5b_1x1_bn = self.inception_5b_relu_1x1(inception_5b_1x1_bn)
        inception_5b_3x3_reduce = self.inception_5b_3x3_reduce(
            inception_5a_output_inception_5a_output_0_split_1)
        inception_5b_3x3_reduce_bn = self.inception_5b_3x3_reduce_bn(
            inception_5b_3x3_reduce)
        inception_5b_3x3_reduce_bn = self.inception_5b_relu_3x3_reduce(
            inception_5b_3x3_reduce_bn)
        inception_5b_3x3 = self.inception_5b_3x3(inception_5b_3x3_reduce_bn)
        inception_5b_3x3_bn = self.inception_5b_3x3_bn(inception_5b_3x3)
        inception_5b_3x3_bn = self.inception_5b_relu_3x3(inception_5b_3x3_bn)
        inception_5b_double_3x3_reduce = self.inception_5b_double_3x3_reduce(
            inception_5a_output_inception_5a_output_0_split_2)
        inception_5b_double_3x3_reduce_bn = self.inception_5b_double_3x3_reduce_bn(
            inception_5b_double_3x3_reduce)
        inception_5b_double_3x3_reduce_bn = self.inception_5b_relu_double_3x3_reduce(
            inception_5b_double_3x3_reduce_bn)
        inception_5b_double_3x3_1 = self.inception_5b_double_3x3_1(
            inception_5b_double_3x3_reduce_bn)
        inception_5b_double_3x3_1_bn = self.inception_5b_double_3x3_1_bn(
            inception_5b_double_3x3_1)
        inception_5b_double_3x3_1_bn = self.inception_5b_relu_double_3x3_1(
            inception_5b_double_3x3_1_bn)
        inception_5b_double_3x3_2 = self.inception_5b_double_3x3_2(
            inception_5b_double_3x3_1_bn)
        inception_5b_double_3x3_2_bn = self.inception_5b_double_3x3_2_bn(
            inception_5b_double_3x3_2)
        inception_5b_double_3x3_2_bn = self.inception_5b_relu_double_3x3_2(
            inception_5b_double_3x3_2_bn)
        inception_5b_pool = self.inception_5b_pool(
            inception_5a_output_inception_5a_output_0_split_3)
        inception_5b_pool_proj = self.inception_5b_pool_proj(inception_5b_pool)
        inception_5b_pool_proj_bn = self.inception_5b_pool_proj_bn(
            inception_5b_pool_proj)
        inception_5b_pool_proj_bn = self.inception_5b_relu_pool_proj(
            inception_5b_pool_proj_bn)
        inception_5b_output = torch.cat(
            (inception_5b_1x1_bn,
             inception_5b_3x3_bn,
             inception_5b_double_3x3_2_bn,
             inception_5b_pool_proj_bn),
            dim=1)
        global_pool = F.avg_pool2d(
            inception_5b_output,
            kernel_size=(
                inception_5b_output.shape[2],
                inception_5b_output.shape[3]),
            padding=0)
        global_pool = self.dropout(global_pool)
        global_pool = self.flatten(global_pool)
        return global_pool
        # fc_action = self.fc_action(global_pool)
        # return fc_action
