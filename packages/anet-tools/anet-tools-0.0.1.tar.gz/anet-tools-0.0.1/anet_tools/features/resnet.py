import torch
import torch.nn as nn
import torch.nn.functional as F

from anet_tools.features.data import get_resnet200_pretrained_model


class Resnet200(nn.Module):

    def __init__(self, pretrained_model=True):
        super(Resnet200, self).__init__()
        self.caffe_SpatialConvolution_0 = nn.Conv2d(
            3, 64, kernel_size=(
                7, 7), stride=(
                2, 2), padding=(
                3, 3), dilation=1, groups=1, bias=False)
        self.caffe_Pooling_1 = nn.MaxPool2d(
            kernel_size=(
                3, 3), stride=(
                2, 2), padding=(
                0, 0), ceil_mode=True)
        self.caffe_BN_2 = nn.BatchNorm2d(64, momentum=0.1)
        self.caffe_ReLU_3 = nn.ReLU()
        self.caffe_SpatialConvolution_4 = nn.Conv2d(
            64, 64, kernel_size=(
                1, 1), stride=(
                1, 1), padding=(
                0, 0), dilation=1, groups=1, bias=False)
        self.caffe_BN_5 = nn.BatchNorm2d(64, momentum=0.1)
        self.caffe_ReLU_6 = nn.ReLU()
        self.caffe_SpatialConvolution_7 = nn.Conv2d(
            64, 64, kernel_size=(
                3, 3), stride=(
                1, 1), padding=(
                1, 1), dilation=1, groups=1, bias=False)
        self.caffe_BN_8 = nn.BatchNorm2d(64, momentum=0.1)
        self.caffe_ReLU_9 = nn.ReLU()
        self.caffe_SpatialConvolution_10 = nn.Conv2d(
            64, 256, kernel_size=(
                1, 1), stride=(
                1, 1), padding=(
                0, 0), dilation=1, groups=1, bias=False)
        self.caffe_SpatialConvolution_11 = nn.Conv2d(
            64, 256, kernel_size=(
                1, 1), stride=(
                1, 1), padding=(
                0, 0), dilation=1, groups=1, bias=False)
        self.caffe_BN_12 = nn.BatchNorm2d(256, momentum=0.1)
        self.caffe_BN_14 = nn.BatchNorm2d(256, momentum=0.1)
        self.caffe_ReLU_15 = nn.ReLU()
        self.caffe_SpatialConvolution_16 = nn.Conv2d(
            256, 64, kernel_size=(
                1, 1), stride=(
                1, 1), padding=(
                0, 0), dilation=1, groups=1, bias=False)
        self.caffe_BN_17 = nn.BatchNorm2d(64, momentum=0.1)
        self.caffe_ReLU_18 = nn.ReLU()
        self.caffe_SpatialConvolution_19 = nn.Conv2d(
            64, 64, kernel_size=(
                3, 3), stride=(
                1, 1), padding=(
                1, 1), dilation=1, groups=1, bias=False)
        self.caffe_BN_20 = nn.BatchNorm2d(64, momentum=0.1)
        self.caffe_ReLU_21 = nn.ReLU()
        self.caffe_SpatialConvolution_22 = nn.Conv2d(
            64, 256, kernel_size=(
                1, 1), stride=(
                1, 1), padding=(
                0, 0), dilation=1, groups=1, bias=False)
        self.caffe_BN_24 = nn.BatchNorm2d(256, momentum=0.1)
        self.caffe_ReLU_25 = nn.ReLU()
        self.caffe_SpatialConvolution_26 = nn.Conv2d(
            256, 64, kernel_size=(
                1, 1), stride=(
                1, 1), padding=(
                0, 0), dilation=1, groups=1, bias=False)
        self.caffe_BN_27 = nn.BatchNorm2d(64, momentum=0.1)
        self.caffe_ReLU_28 = nn.ReLU()
        self.caffe_SpatialConvolution_29 = nn.Conv2d(
            64, 64, kernel_size=(
                3, 3), stride=(
                1, 1), padding=(
                1, 1), dilation=1, groups=1, bias=False)
        self.caffe_BN_30 = nn.BatchNorm2d(64, momentum=0.1)
        self.caffe_ReLU_31 = nn.ReLU()
        self.caffe_SpatialConvolution_32 = nn.Conv2d(
            64, 256, kernel_size=(
                1, 1), stride=(
                1, 1), padding=(
                0, 0), dilation=1, groups=1, bias=False)
        self.caffe_BN_34 = nn.BatchNorm2d(256, momentum=0.1)
        self.caffe_ReLU_35 = nn.ReLU()
        self.caffe_SpatialConvolution_36 = nn.Conv2d(
            256, 128, kernel_size=(
                1, 1), stride=(
                1, 1), padding=(
                0, 0), dilation=1, groups=1, bias=False)
        self.caffe_BN_37 = nn.BatchNorm2d(128, momentum=0.1)
        self.caffe_ReLU_38 = nn.ReLU()
        self.caffe_SpatialConvolution_39 = nn.Conv2d(
            128, 128, kernel_size=(
                3, 3), stride=(
                2, 2), padding=(
                1, 1), dilation=1, groups=1, bias=False)
        self.caffe_BN_40 = nn.BatchNorm2d(128, momentum=0.1)
        self.caffe_ReLU_41 = nn.ReLU()
        self.caffe_SpatialConvolution_42 = nn.Conv2d(
            128, 512, kernel_size=(
                1, 1), stride=(
                1, 1), padding=(
                0, 0), dilation=1, groups=1, bias=False)
        self.caffe_SpatialConvolution_43 = nn.Conv2d(
            256, 512, kernel_size=(
                1, 1), stride=(
                2, 2), padding=(
                0, 0), dilation=1, groups=1, bias=False)
        self.caffe_BN_44 = nn.BatchNorm2d(512, momentum=0.1)
        self.caffe_BN_46 = nn.BatchNorm2d(512, momentum=0.1)
        self.caffe_ReLU_47 = nn.ReLU()
        self.caffe_SpatialConvolution_48 = nn.Conv2d(
            512, 128, kernel_size=(
                1, 1), stride=(
                1, 1), padding=(
                0, 0), dilation=1, groups=1, bias=False)
        self.caffe_BN_49 = nn.BatchNorm2d(128, momentum=0.1)
        self.caffe_ReLU_50 = nn.ReLU()
        self.caffe_SpatialConvolution_51 = nn.Conv2d(
            128, 128, kernel_size=(
                3, 3), stride=(
                1, 1), padding=(
                1, 1), dilation=1, groups=1, bias=False)
        self.caffe_BN_52 = nn.BatchNorm2d(128, momentum=0.1)
        self.caffe_ReLU_53 = nn.ReLU()
        self.caffe_SpatialConvolution_54 = nn.Conv2d(
            128, 512, kernel_size=(
                1, 1), stride=(
                1, 1), padding=(
                0, 0), dilation=1, groups=1, bias=False)
        self.caffe_BN_56 = nn.BatchNorm2d(512, momentum=0.1)
        self.caffe_ReLU_57 = nn.ReLU()
        self.caffe_SpatialConvolution_58 = nn.Conv2d(
            512, 128, kernel_size=(
                1, 1), stride=(
                1, 1), padding=(
                0, 0), dilation=1, groups=1, bias=False)
        self.caffe_BN_59 = nn.BatchNorm2d(128, momentum=0.1)
        self.caffe_ReLU_60 = nn.ReLU()
        self.caffe_SpatialConvolution_61 = nn.Conv2d(
            128, 128, kernel_size=(
                3, 3), stride=(
                1, 1), padding=(
                1, 1), dilation=1, groups=1, bias=False)
        self.caffe_BN_62 = nn.BatchNorm2d(128, momentum=0.1)
        self.caffe_ReLU_63 = nn.ReLU()
        self.caffe_SpatialConvolution_64 = nn.Conv2d(
            128, 512, kernel_size=(
                1, 1), stride=(
                1, 1), padding=(
                0, 0), dilation=1, groups=1, bias=False)
        self.caffe_BN_66 = nn.BatchNorm2d(512, momentum=0.1)
        self.caffe_ReLU_67 = nn.ReLU()
        self.caffe_SpatialConvolution_68 = nn.Conv2d(
            512, 128, kernel_size=(
                1, 1), stride=(
                1, 1), padding=(
                0, 0), dilation=1, groups=1, bias=False)
        self.caffe_BN_69 = nn.BatchNorm2d(128, momentum=0.1)
        self.caffe_ReLU_70 = nn.ReLU()
        self.caffe_SpatialConvolution_71 = nn.Conv2d(
            128, 128, kernel_size=(
                3, 3), stride=(
                1, 1), padding=(
                1, 1), dilation=1, groups=1, bias=False)
        self.caffe_BN_72 = nn.BatchNorm2d(128, momentum=0.1)
        self.caffe_ReLU_73 = nn.ReLU()
        self.caffe_SpatialConvolution_74 = nn.Conv2d(
            128, 512, kernel_size=(
                1, 1), stride=(
                1, 1), padding=(
                0, 0), dilation=1, groups=1, bias=False)
        self.caffe_BN_76 = nn.BatchNorm2d(512, momentum=0.1)
        self.caffe_ReLU_77 = nn.ReLU()
        self.caffe_SpatialConvolution_78 = nn.Conv2d(
            512, 128, kernel_size=(
                1, 1), stride=(
                1, 1), padding=(
                0, 0), dilation=1, groups=1, bias=False)
        self.caffe_BN_79 = nn.BatchNorm2d(128, momentum=0.1)
        self.caffe_ReLU_80 = nn.ReLU()
        self.caffe_SpatialConvolution_81 = nn.Conv2d(
            128, 128, kernel_size=(
                3, 3), stride=(
                1, 1), padding=(
                1, 1), dilation=1, groups=1, bias=False)
        self.caffe_BN_82 = nn.BatchNorm2d(128, momentum=0.1)
        self.caffe_ReLU_83 = nn.ReLU()
        self.caffe_SpatialConvolution_84 = nn.Conv2d(
            128, 512, kernel_size=(
                1, 1), stride=(
                1, 1), padding=(
                0, 0), dilation=1, groups=1, bias=False)
        self.caffe_BN_86 = nn.BatchNorm2d(512, momentum=0.1)
        self.caffe_ReLU_87 = nn.ReLU()
        self.caffe_SpatialConvolution_88 = nn.Conv2d(
            512, 128, kernel_size=(
                1, 1), stride=(
                1, 1), padding=(
                0, 0), dilation=1, groups=1, bias=False)
        self.caffe_BN_89 = nn.BatchNorm2d(128, momentum=0.1)
        self.caffe_ReLU_90 = nn.ReLU()
        self.caffe_SpatialConvolution_91 = nn.Conv2d(
            128, 128, kernel_size=(
                3, 3), stride=(
                1, 1), padding=(
                1, 1), dilation=1, groups=1, bias=False)
        self.caffe_BN_92 = nn.BatchNorm2d(128, momentum=0.1)
        self.caffe_ReLU_93 = nn.ReLU()
        self.caffe_SpatialConvolution_94 = nn.Conv2d(
            128, 512, kernel_size=(
                1, 1), stride=(
                1, 1), padding=(
                0, 0), dilation=1, groups=1, bias=False)
        self.caffe_BN_96 = nn.BatchNorm2d(512, momentum=0.1)
        self.caffe_ReLU_97 = nn.ReLU()
        self.caffe_SpatialConvolution_98 = nn.Conv2d(
            512, 128, kernel_size=(
                1, 1), stride=(
                1, 1), padding=(
                0, 0), dilation=1, groups=1, bias=False)
        self.caffe_BN_99 = nn.BatchNorm2d(128, momentum=0.1)
        self.caffe_ReLU_100 = nn.ReLU()
        self.caffe_SpatialConvolution_101 = nn.Conv2d(
            128, 128, kernel_size=(
                3, 3), stride=(
                1, 1), padding=(
                1, 1), dilation=1, groups=1, bias=False)
        self.caffe_BN_102 = nn.BatchNorm2d(128, momentum=0.1)
        self.caffe_ReLU_103 = nn.ReLU()
        self.caffe_SpatialConvolution_104 = nn.Conv2d(
            128, 512, kernel_size=(
                1, 1), stride=(
                1, 1), padding=(
                0, 0), dilation=1, groups=1, bias=False)
        self.caffe_BN_106 = nn.BatchNorm2d(512, momentum=0.1)
        self.caffe_ReLU_107 = nn.ReLU()
        self.caffe_SpatialConvolution_108 = nn.Conv2d(
            512, 128, kernel_size=(
                1, 1), stride=(
                1, 1), padding=(
                0, 0), dilation=1, groups=1, bias=False)
        self.caffe_BN_109 = nn.BatchNorm2d(128, momentum=0.1)
        self.caffe_ReLU_110 = nn.ReLU()
        self.caffe_SpatialConvolution_111 = nn.Conv2d(
            128, 128, kernel_size=(
                3, 3), stride=(
                1, 1), padding=(
                1, 1), dilation=1, groups=1, bias=False)
        self.caffe_BN_112 = nn.BatchNorm2d(128, momentum=0.1)
        self.caffe_ReLU_113 = nn.ReLU()
        self.caffe_SpatialConvolution_114 = nn.Conv2d(
            128, 512, kernel_size=(
                1, 1), stride=(
                1, 1), padding=(
                0, 0), dilation=1, groups=1, bias=False)
        self.caffe_BN_116 = nn.BatchNorm2d(512, momentum=0.1)
        self.caffe_ReLU_117 = nn.ReLU()
        self.caffe_SpatialConvolution_118 = nn.Conv2d(
            512, 128, kernel_size=(
                1, 1), stride=(
                1, 1), padding=(
                0, 0), dilation=1, groups=1, bias=False)
        self.caffe_BN_119 = nn.BatchNorm2d(128, momentum=0.1)
        self.caffe_ReLU_120 = nn.ReLU()
        self.caffe_SpatialConvolution_121 = nn.Conv2d(
            128, 128, kernel_size=(
                3, 3), stride=(
                1, 1), padding=(
                1, 1), dilation=1, groups=1, bias=False)
        self.caffe_BN_122 = nn.BatchNorm2d(128, momentum=0.1)
        self.caffe_ReLU_123 = nn.ReLU()
        self.caffe_SpatialConvolution_124 = nn.Conv2d(
            128, 512, kernel_size=(
                1, 1), stride=(
                1, 1), padding=(
                0, 0), dilation=1, groups=1, bias=False)
        self.caffe_BN_126 = nn.BatchNorm2d(512, momentum=0.1)
        self.caffe_ReLU_127 = nn.ReLU()
        self.caffe_SpatialConvolution_128 = nn.Conv2d(
            512, 128, kernel_size=(
                1, 1), stride=(
                1, 1), padding=(
                0, 0), dilation=1, groups=1, bias=False)
        self.caffe_BN_129 = nn.BatchNorm2d(128, momentum=0.1)
        self.caffe_ReLU_130 = nn.ReLU()
        self.caffe_SpatialConvolution_131 = nn.Conv2d(
            128, 128, kernel_size=(
                3, 3), stride=(
                1, 1), padding=(
                1, 1), dilation=1, groups=1, bias=False)
        self.caffe_BN_132 = nn.BatchNorm2d(128, momentum=0.1)
        self.caffe_ReLU_133 = nn.ReLU()
        self.caffe_SpatialConvolution_134 = nn.Conv2d(
            128, 512, kernel_size=(
                1, 1), stride=(
                1, 1), padding=(
                0, 0), dilation=1, groups=1, bias=False)
        self.caffe_BN_136 = nn.BatchNorm2d(512, momentum=0.1)
        self.caffe_ReLU_137 = nn.ReLU()
        self.caffe_SpatialConvolution_138 = nn.Conv2d(
            512, 128, kernel_size=(
                1, 1), stride=(
                1, 1), padding=(
                0, 0), dilation=1, groups=1, bias=False)
        self.caffe_BN_139 = nn.BatchNorm2d(128, momentum=0.1)
        self.caffe_ReLU_140 = nn.ReLU()
        self.caffe_SpatialConvolution_141 = nn.Conv2d(
            128, 128, kernel_size=(
                3, 3), stride=(
                1, 1), padding=(
                1, 1), dilation=1, groups=1, bias=False)
        self.caffe_BN_142 = nn.BatchNorm2d(128, momentum=0.1)
        self.caffe_ReLU_143 = nn.ReLU()
        self.caffe_SpatialConvolution_144 = nn.Conv2d(
            128, 512, kernel_size=(
                1, 1), stride=(
                1, 1), padding=(
                0, 0), dilation=1, groups=1, bias=False)
        self.caffe_BN_146 = nn.BatchNorm2d(512, momentum=0.1)
        self.caffe_ReLU_147 = nn.ReLU()
        self.caffe_SpatialConvolution_148 = nn.Conv2d(
            512, 128, kernel_size=(
                1, 1), stride=(
                1, 1), padding=(
                0, 0), dilation=1, groups=1, bias=False)
        self.caffe_BN_149 = nn.BatchNorm2d(128, momentum=0.1)
        self.caffe_ReLU_150 = nn.ReLU()
        self.caffe_SpatialConvolution_151 = nn.Conv2d(
            128, 128, kernel_size=(
                3, 3), stride=(
                1, 1), padding=(
                1, 1), dilation=1, groups=1, bias=False)
        self.caffe_BN_152 = nn.BatchNorm2d(128, momentum=0.1)
        self.caffe_ReLU_153 = nn.ReLU()
        self.caffe_SpatialConvolution_154 = nn.Conv2d(
            128, 512, kernel_size=(
                1, 1), stride=(
                1, 1), padding=(
                0, 0), dilation=1, groups=1, bias=False)
        self.caffe_BN_156 = nn.BatchNorm2d(512, momentum=0.1)
        self.caffe_ReLU_157 = nn.ReLU()
        self.caffe_SpatialConvolution_158 = nn.Conv2d(
            512, 128, kernel_size=(
                1, 1), stride=(
                1, 1), padding=(
                0, 0), dilation=1, groups=1, bias=False)
        self.caffe_BN_159 = nn.BatchNorm2d(128, momentum=0.1)
        self.caffe_ReLU_160 = nn.ReLU()
        self.caffe_SpatialConvolution_161 = nn.Conv2d(
            128, 128, kernel_size=(
                3, 3), stride=(
                1, 1), padding=(
                1, 1), dilation=1, groups=1, bias=False)
        self.caffe_BN_162 = nn.BatchNorm2d(128, momentum=0.1)
        self.caffe_ReLU_163 = nn.ReLU()
        self.caffe_SpatialConvolution_164 = nn.Conv2d(
            128, 512, kernel_size=(
                1, 1), stride=(
                1, 1), padding=(
                0, 0), dilation=1, groups=1, bias=False)
        self.caffe_BN_166 = nn.BatchNorm2d(512, momentum=0.1)
        self.caffe_ReLU_167 = nn.ReLU()
        self.caffe_SpatialConvolution_168 = nn.Conv2d(
            512, 128, kernel_size=(
                1, 1), stride=(
                1, 1), padding=(
                0, 0), dilation=1, groups=1, bias=False)
        self.caffe_BN_169 = nn.BatchNorm2d(128, momentum=0.1)
        self.caffe_ReLU_170 = nn.ReLU()
        self.caffe_SpatialConvolution_171 = nn.Conv2d(
            128, 128, kernel_size=(
                3, 3), stride=(
                1, 1), padding=(
                1, 1), dilation=1, groups=1, bias=False)
        self.caffe_BN_172 = nn.BatchNorm2d(128, momentum=0.1)
        self.caffe_ReLU_173 = nn.ReLU()
        self.caffe_SpatialConvolution_174 = nn.Conv2d(
            128, 512, kernel_size=(
                1, 1), stride=(
                1, 1), padding=(
                0, 0), dilation=1, groups=1, bias=False)
        self.caffe_BN_176 = nn.BatchNorm2d(512, momentum=0.1)
        self.caffe_ReLU_177 = nn.ReLU()
        self.caffe_SpatialConvolution_178 = nn.Conv2d(
            512, 128, kernel_size=(
                1, 1), stride=(
                1, 1), padding=(
                0, 0), dilation=1, groups=1, bias=False)
        self.caffe_BN_179 = nn.BatchNorm2d(128, momentum=0.1)
        self.caffe_ReLU_180 = nn.ReLU()
        self.caffe_SpatialConvolution_181 = nn.Conv2d(
            128, 128, kernel_size=(
                3, 3), stride=(
                1, 1), padding=(
                1, 1), dilation=1, groups=1, bias=False)
        self.caffe_BN_182 = nn.BatchNorm2d(128, momentum=0.1)
        self.caffe_ReLU_183 = nn.ReLU()
        self.caffe_SpatialConvolution_184 = nn.Conv2d(
            128, 512, kernel_size=(
                1, 1), stride=(
                1, 1), padding=(
                0, 0), dilation=1, groups=1, bias=False)
        self.caffe_BN_186 = nn.BatchNorm2d(512, momentum=0.1)
        self.caffe_ReLU_187 = nn.ReLU()
        self.caffe_SpatialConvolution_188 = nn.Conv2d(
            512, 128, kernel_size=(
                1, 1), stride=(
                1, 1), padding=(
                0, 0), dilation=1, groups=1, bias=False)
        self.caffe_BN_189 = nn.BatchNorm2d(128, momentum=0.1)
        self.caffe_ReLU_190 = nn.ReLU()
        self.caffe_SpatialConvolution_191 = nn.Conv2d(
            128, 128, kernel_size=(
                3, 3), stride=(
                1, 1), padding=(
                1, 1), dilation=1, groups=1, bias=False)
        self.caffe_BN_192 = nn.BatchNorm2d(128, momentum=0.1)
        self.caffe_ReLU_193 = nn.ReLU()
        self.caffe_SpatialConvolution_194 = nn.Conv2d(
            128, 512, kernel_size=(
                1, 1), stride=(
                1, 1), padding=(
                0, 0), dilation=1, groups=1, bias=False)
        self.caffe_BN_196 = nn.BatchNorm2d(512, momentum=0.1)
        self.caffe_ReLU_197 = nn.ReLU()
        self.caffe_SpatialConvolution_198 = nn.Conv2d(
            512, 128, kernel_size=(
                1, 1), stride=(
                1, 1), padding=(
                0, 0), dilation=1, groups=1, bias=False)
        self.caffe_BN_199 = nn.BatchNorm2d(128, momentum=0.1)
        self.caffe_ReLU_200 = nn.ReLU()
        self.caffe_SpatialConvolution_201 = nn.Conv2d(
            128, 128, kernel_size=(
                3, 3), stride=(
                1, 1), padding=(
                1, 1), dilation=1, groups=1, bias=False)
        self.caffe_BN_202 = nn.BatchNorm2d(128, momentum=0.1)
        self.caffe_ReLU_203 = nn.ReLU()
        self.caffe_SpatialConvolution_204 = nn.Conv2d(
            128, 512, kernel_size=(
                1, 1), stride=(
                1, 1), padding=(
                0, 0), dilation=1, groups=1, bias=False)
        self.caffe_BN_206 = nn.BatchNorm2d(512, momentum=0.1)
        self.caffe_ReLU_207 = nn.ReLU()
        self.caffe_SpatialConvolution_208 = nn.Conv2d(
            512, 128, kernel_size=(
                1, 1), stride=(
                1, 1), padding=(
                0, 0), dilation=1, groups=1, bias=False)
        self.caffe_BN_209 = nn.BatchNorm2d(128, momentum=0.1)
        self.caffe_ReLU_210 = nn.ReLU()
        self.caffe_SpatialConvolution_211 = nn.Conv2d(
            128, 128, kernel_size=(
                3, 3), stride=(
                1, 1), padding=(
                1, 1), dilation=1, groups=1, bias=False)
        self.caffe_BN_212 = nn.BatchNorm2d(128, momentum=0.1)
        self.caffe_ReLU_213 = nn.ReLU()
        self.caffe_SpatialConvolution_214 = nn.Conv2d(
            128, 512, kernel_size=(
                1, 1), stride=(
                1, 1), padding=(
                0, 0), dilation=1, groups=1, bias=False)
        self.caffe_BN_216 = nn.BatchNorm2d(512, momentum=0.1)
        self.caffe_ReLU_217 = nn.ReLU()
        self.caffe_SpatialConvolution_218 = nn.Conv2d(
            512, 128, kernel_size=(
                1, 1), stride=(
                1, 1), padding=(
                0, 0), dilation=1, groups=1, bias=False)
        self.caffe_BN_219 = nn.BatchNorm2d(128, momentum=0.1)
        self.caffe_ReLU_220 = nn.ReLU()
        self.caffe_SpatialConvolution_221 = nn.Conv2d(
            128, 128, kernel_size=(
                3, 3), stride=(
                1, 1), padding=(
                1, 1), dilation=1, groups=1, bias=False)
        self.caffe_BN_222 = nn.BatchNorm2d(128, momentum=0.1)
        self.caffe_ReLU_223 = nn.ReLU()
        self.caffe_SpatialConvolution_224 = nn.Conv2d(
            128, 512, kernel_size=(
                1, 1), stride=(
                1, 1), padding=(
                0, 0), dilation=1, groups=1, bias=False)
        self.caffe_BN_226 = nn.BatchNorm2d(512, momentum=0.1)
        self.caffe_ReLU_227 = nn.ReLU()
        self.caffe_SpatialConvolution_228 = nn.Conv2d(
            512, 128, kernel_size=(
                1, 1), stride=(
                1, 1), padding=(
                0, 0), dilation=1, groups=1, bias=False)
        self.caffe_BN_229 = nn.BatchNorm2d(128, momentum=0.1)
        self.caffe_ReLU_230 = nn.ReLU()
        self.caffe_SpatialConvolution_231 = nn.Conv2d(
            128, 128, kernel_size=(
                3, 3), stride=(
                1, 1), padding=(
                1, 1), dilation=1, groups=1, bias=False)
        self.caffe_BN_232 = nn.BatchNorm2d(128, momentum=0.1)
        self.caffe_ReLU_233 = nn.ReLU()
        self.caffe_SpatialConvolution_234 = nn.Conv2d(
            128, 512, kernel_size=(
                1, 1), stride=(
                1, 1), padding=(
                0, 0), dilation=1, groups=1, bias=False)
        self.caffe_BN_236 = nn.BatchNorm2d(512, momentum=0.1)
        self.caffe_ReLU_237 = nn.ReLU()
        self.caffe_SpatialConvolution_238 = nn.Conv2d(
            512, 128, kernel_size=(
                1, 1), stride=(
                1, 1), padding=(
                0, 0), dilation=1, groups=1, bias=False)
        self.caffe_BN_239 = nn.BatchNorm2d(128, momentum=0.1)
        self.caffe_ReLU_240 = nn.ReLU()
        self.caffe_SpatialConvolution_241 = nn.Conv2d(
            128, 128, kernel_size=(
                3, 3), stride=(
                1, 1), padding=(
                1, 1), dilation=1, groups=1, bias=False)
        self.caffe_BN_242 = nn.BatchNorm2d(128, momentum=0.1)
        self.caffe_ReLU_243 = nn.ReLU()
        self.caffe_SpatialConvolution_244 = nn.Conv2d(
            128, 512, kernel_size=(
                1, 1), stride=(
                1, 1), padding=(
                0, 0), dilation=1, groups=1, bias=False)
        self.caffe_BN_246 = nn.BatchNorm2d(512, momentum=0.1)
        self.caffe_ReLU_247 = nn.ReLU()
        self.caffe_SpatialConvolution_248 = nn.Conv2d(
            512, 128, kernel_size=(
                1, 1), stride=(
                1, 1), padding=(
                0, 0), dilation=1, groups=1, bias=False)
        self.caffe_BN_249 = nn.BatchNorm2d(128, momentum=0.1)
        self.caffe_ReLU_250 = nn.ReLU()
        self.caffe_SpatialConvolution_251 = nn.Conv2d(
            128, 128, kernel_size=(
                3, 3), stride=(
                1, 1), padding=(
                1, 1), dilation=1, groups=1, bias=False)
        self.caffe_BN_252 = nn.BatchNorm2d(128, momentum=0.1)
        self.caffe_ReLU_253 = nn.ReLU()
        self.caffe_SpatialConvolution_254 = nn.Conv2d(
            128, 512, kernel_size=(
                1, 1), stride=(
                1, 1), padding=(
                0, 0), dilation=1, groups=1, bias=False)
        self.caffe_BN_256 = nn.BatchNorm2d(512, momentum=0.1)
        self.caffe_ReLU_257 = nn.ReLU()
        self.caffe_SpatialConvolution_258 = nn.Conv2d(
            512, 128, kernel_size=(
                1, 1), stride=(
                1, 1), padding=(
                0, 0), dilation=1, groups=1, bias=False)
        self.caffe_BN_259 = nn.BatchNorm2d(128, momentum=0.1)
        self.caffe_ReLU_260 = nn.ReLU()
        self.caffe_SpatialConvolution_261 = nn.Conv2d(
            128, 128, kernel_size=(
                3, 3), stride=(
                1, 1), padding=(
                1, 1), dilation=1, groups=1, bias=False)
        self.caffe_BN_262 = nn.BatchNorm2d(128, momentum=0.1)
        self.caffe_ReLU_263 = nn.ReLU()
        self.caffe_SpatialConvolution_264 = nn.Conv2d(
            128, 512, kernel_size=(
                1, 1), stride=(
                1, 1), padding=(
                0, 0), dilation=1, groups=1, bias=False)
        self.caffe_BN_266 = nn.BatchNorm2d(512, momentum=0.1)
        self.caffe_ReLU_267 = nn.ReLU()
        self.caffe_SpatialConvolution_268 = nn.Conv2d(
            512, 128, kernel_size=(
                1, 1), stride=(
                1, 1), padding=(
                0, 0), dilation=1, groups=1, bias=False)
        self.caffe_BN_269 = nn.BatchNorm2d(128, momentum=0.1)
        self.caffe_ReLU_270 = nn.ReLU()
        self.caffe_SpatialConvolution_271 = nn.Conv2d(
            128, 128, kernel_size=(
                3, 3), stride=(
                1, 1), padding=(
                1, 1), dilation=1, groups=1, bias=False)
        self.caffe_BN_272 = nn.BatchNorm2d(128, momentum=0.1)
        self.caffe_ReLU_273 = nn.ReLU()
        self.caffe_SpatialConvolution_274 = nn.Conv2d(
            128, 512, kernel_size=(
                1, 1), stride=(
                1, 1), padding=(
                0, 0), dilation=1, groups=1, bias=False)
        self.caffe_BN_276 = nn.BatchNorm2d(512, momentum=0.1)
        self.caffe_ReLU_277 = nn.ReLU()
        self.caffe_SpatialConvolution_278 = nn.Conv2d(
            512, 256, kernel_size=(
                1, 1), stride=(
                1, 1), padding=(
                0, 0), dilation=1, groups=1, bias=False)
        self.caffe_BN_279 = nn.BatchNorm2d(256, momentum=0.1)
        self.caffe_ReLU_280 = nn.ReLU()
        self.caffe_SpatialConvolution_281 = nn.Conv2d(
            256, 256, kernel_size=(
                3, 3), stride=(
                2, 2), padding=(
                1, 1), dilation=1, groups=1, bias=False)
        self.caffe_BN_282 = nn.BatchNorm2d(256, momentum=0.1)
        self.caffe_ReLU_283 = nn.ReLU()
        self.caffe_SpatialConvolution_284 = nn.Conv2d(
            256, 1024, kernel_size=(
                1, 1), stride=(
                1, 1), padding=(
                0, 0), dilation=1, groups=1, bias=False)
        self.caffe_SpatialConvolution_285 = nn.Conv2d(
            512, 1024, kernel_size=(
                1, 1), stride=(
                2, 2), padding=(
                0, 0), dilation=1, groups=1, bias=False)
        self.caffe_BN_286 = nn.BatchNorm2d(1024, momentum=0.1)
        self.caffe_BN_288 = nn.BatchNorm2d(1024, momentum=0.1)
        self.caffe_ReLU_289 = nn.ReLU()
        self.caffe_SpatialConvolution_290 = nn.Conv2d(
            1024, 256, kernel_size=(
                1, 1), stride=(
                1, 1), padding=(
                0, 0), dilation=1, groups=1, bias=False)
        self.caffe_BN_291 = nn.BatchNorm2d(256, momentum=0.1)
        self.caffe_ReLU_292 = nn.ReLU()
        self.caffe_SpatialConvolution_293 = nn.Conv2d(
            256, 256, kernel_size=(
                3, 3), stride=(
                1, 1), padding=(
                1, 1), dilation=1, groups=1, bias=False)
        self.caffe_BN_294 = nn.BatchNorm2d(256, momentum=0.1)
        self.caffe_ReLU_295 = nn.ReLU()
        self.caffe_SpatialConvolution_296 = nn.Conv2d(
            256, 1024, kernel_size=(
                1, 1), stride=(
                1, 1), padding=(
                0, 0), dilation=1, groups=1, bias=False)
        self.caffe_BN_298 = nn.BatchNorm2d(1024, momentum=0.1)
        self.caffe_ReLU_299 = nn.ReLU()
        self.caffe_SpatialConvolution_300 = nn.Conv2d(
            1024, 256, kernel_size=(
                1, 1), stride=(
                1, 1), padding=(
                0, 0), dilation=1, groups=1, bias=False)
        self.caffe_BN_301 = nn.BatchNorm2d(256, momentum=0.1)
        self.caffe_ReLU_302 = nn.ReLU()
        self.caffe_SpatialConvolution_303 = nn.Conv2d(
            256, 256, kernel_size=(
                3, 3), stride=(
                1, 1), padding=(
                1, 1), dilation=1, groups=1, bias=False)
        self.caffe_BN_304 = nn.BatchNorm2d(256, momentum=0.1)
        self.caffe_ReLU_305 = nn.ReLU()
        self.caffe_SpatialConvolution_306 = nn.Conv2d(
            256, 1024, kernel_size=(
                1, 1), stride=(
                1, 1), padding=(
                0, 0), dilation=1, groups=1, bias=False)
        self.caffe_BN_308 = nn.BatchNorm2d(1024, momentum=0.1)
        self.caffe_ReLU_309 = nn.ReLU()
        self.caffe_SpatialConvolution_310 = nn.Conv2d(
            1024, 256, kernel_size=(
                1, 1), stride=(
                1, 1), padding=(
                0, 0), dilation=1, groups=1, bias=False)
        self.caffe_BN_311 = nn.BatchNorm2d(256, momentum=0.1)
        self.caffe_ReLU_312 = nn.ReLU()
        self.caffe_SpatialConvolution_313 = nn.Conv2d(
            256, 256, kernel_size=(
                3, 3), stride=(
                1, 1), padding=(
                1, 1), dilation=1, groups=1, bias=False)
        self.caffe_BN_314 = nn.BatchNorm2d(256, momentum=0.1)
        self.caffe_ReLU_315 = nn.ReLU()
        self.caffe_SpatialConvolution_316 = nn.Conv2d(
            256, 1024, kernel_size=(
                1, 1), stride=(
                1, 1), padding=(
                0, 0), dilation=1, groups=1, bias=False)
        self.caffe_BN_318 = nn.BatchNorm2d(1024, momentum=0.1)
        self.caffe_ReLU_319 = nn.ReLU()
        self.caffe_SpatialConvolution_320 = nn.Conv2d(
            1024, 256, kernel_size=(
                1, 1), stride=(
                1, 1), padding=(
                0, 0), dilation=1, groups=1, bias=False)
        self.caffe_BN_321 = nn.BatchNorm2d(256, momentum=0.1)
        self.caffe_ReLU_322 = nn.ReLU()
        self.caffe_SpatialConvolution_323 = nn.Conv2d(
            256, 256, kernel_size=(
                3, 3), stride=(
                1, 1), padding=(
                1, 1), dilation=1, groups=1, bias=False)
        self.caffe_BN_324 = nn.BatchNorm2d(256, momentum=0.1)
        self.caffe_ReLU_325 = nn.ReLU()
        self.caffe_SpatialConvolution_326 = nn.Conv2d(
            256, 1024, kernel_size=(
                1, 1), stride=(
                1, 1), padding=(
                0, 0), dilation=1, groups=1, bias=False)
        self.caffe_BN_328 = nn.BatchNorm2d(1024, momentum=0.1)
        self.caffe_ReLU_329 = nn.ReLU()
        self.caffe_SpatialConvolution_330 = nn.Conv2d(
            1024, 256, kernel_size=(
                1, 1), stride=(
                1, 1), padding=(
                0, 0), dilation=1, groups=1, bias=False)
        self.caffe_BN_331 = nn.BatchNorm2d(256, momentum=0.1)
        self.caffe_ReLU_332 = nn.ReLU()
        self.caffe_SpatialConvolution_333 = nn.Conv2d(
            256, 256, kernel_size=(
                3, 3), stride=(
                1, 1), padding=(
                1, 1), dilation=1, groups=1, bias=False)
        self.caffe_BN_334 = nn.BatchNorm2d(256, momentum=0.1)
        self.caffe_ReLU_335 = nn.ReLU()
        self.caffe_SpatialConvolution_336 = nn.Conv2d(
            256, 1024, kernel_size=(
                1, 1), stride=(
                1, 1), padding=(
                0, 0), dilation=1, groups=1, bias=False)
        self.caffe_BN_338 = nn.BatchNorm2d(1024, momentum=0.1)
        self.caffe_ReLU_339 = nn.ReLU()
        self.caffe_SpatialConvolution_340 = nn.Conv2d(
            1024, 256, kernel_size=(
                1, 1), stride=(
                1, 1), padding=(
                0, 0), dilation=1, groups=1, bias=False)
        self.caffe_BN_341 = nn.BatchNorm2d(256, momentum=0.1)
        self.caffe_ReLU_342 = nn.ReLU()
        self.caffe_SpatialConvolution_343 = nn.Conv2d(
            256, 256, kernel_size=(
                3, 3), stride=(
                1, 1), padding=(
                1, 1), dilation=1, groups=1, bias=False)
        self.caffe_BN_344 = nn.BatchNorm2d(256, momentum=0.1)
        self.caffe_ReLU_345 = nn.ReLU()
        self.caffe_SpatialConvolution_346 = nn.Conv2d(
            256, 1024, kernel_size=(
                1, 1), stride=(
                1, 1), padding=(
                0, 0), dilation=1, groups=1, bias=False)
        self.caffe_BN_348 = nn.BatchNorm2d(1024, momentum=0.1)
        self.caffe_ReLU_349 = nn.ReLU()
        self.caffe_SpatialConvolution_350 = nn.Conv2d(
            1024, 256, kernel_size=(
                1, 1), stride=(
                1, 1), padding=(
                0, 0), dilation=1, groups=1, bias=False)
        self.caffe_BN_351 = nn.BatchNorm2d(256, momentum=0.1)
        self.caffe_ReLU_352 = nn.ReLU()
        self.caffe_SpatialConvolution_353 = nn.Conv2d(
            256, 256, kernel_size=(
                3, 3), stride=(
                1, 1), padding=(
                1, 1), dilation=1, groups=1, bias=False)
        self.caffe_BN_354 = nn.BatchNorm2d(256, momentum=0.1)
        self.caffe_ReLU_355 = nn.ReLU()
        self.caffe_SpatialConvolution_356 = nn.Conv2d(
            256, 1024, kernel_size=(
                1, 1), stride=(
                1, 1), padding=(
                0, 0), dilation=1, groups=1, bias=False)
        self.caffe_BN_358 = nn.BatchNorm2d(1024, momentum=0.1)
        self.caffe_ReLU_359 = nn.ReLU()
        self.caffe_SpatialConvolution_360 = nn.Conv2d(
            1024, 256, kernel_size=(
                1, 1), stride=(
                1, 1), padding=(
                0, 0), dilation=1, groups=1, bias=False)
        self.caffe_BN_361 = nn.BatchNorm2d(256, momentum=0.1)
        self.caffe_ReLU_362 = nn.ReLU()
        self.caffe_SpatialConvolution_363 = nn.Conv2d(
            256, 256, kernel_size=(
                3, 3), stride=(
                1, 1), padding=(
                1, 1), dilation=1, groups=1, bias=False)
        self.caffe_BN_364 = nn.BatchNorm2d(256, momentum=0.1)
        self.caffe_ReLU_365 = nn.ReLU()
        self.caffe_SpatialConvolution_366 = nn.Conv2d(
            256, 1024, kernel_size=(
                1, 1), stride=(
                1, 1), padding=(
                0, 0), dilation=1, groups=1, bias=False)
        self.caffe_BN_368 = nn.BatchNorm2d(1024, momentum=0.1)
        self.caffe_ReLU_369 = nn.ReLU()
        self.caffe_SpatialConvolution_370 = nn.Conv2d(
            1024, 256, kernel_size=(
                1, 1), stride=(
                1, 1), padding=(
                0, 0), dilation=1, groups=1, bias=False)
        self.caffe_BN_371 = nn.BatchNorm2d(256, momentum=0.1)
        self.caffe_ReLU_372 = nn.ReLU()
        self.caffe_SpatialConvolution_373 = nn.Conv2d(
            256, 256, kernel_size=(
                3, 3), stride=(
                1, 1), padding=(
                1, 1), dilation=1, groups=1, bias=False)
        self.caffe_BN_374 = nn.BatchNorm2d(256, momentum=0.1)
        self.caffe_ReLU_375 = nn.ReLU()
        self.caffe_SpatialConvolution_376 = nn.Conv2d(
            256, 1024, kernel_size=(
                1, 1), stride=(
                1, 1), padding=(
                0, 0), dilation=1, groups=1, bias=False)
        self.caffe_BN_378 = nn.BatchNorm2d(1024, momentum=0.1)
        self.caffe_ReLU_379 = nn.ReLU()
        self.caffe_SpatialConvolution_380 = nn.Conv2d(
            1024, 256, kernel_size=(
                1, 1), stride=(
                1, 1), padding=(
                0, 0), dilation=1, groups=1, bias=False)
        self.caffe_BN_381 = nn.BatchNorm2d(256, momentum=0.1)
        self.caffe_ReLU_382 = nn.ReLU()
        self.caffe_SpatialConvolution_383 = nn.Conv2d(
            256, 256, kernel_size=(
                3, 3), stride=(
                1, 1), padding=(
                1, 1), dilation=1, groups=1, bias=False)
        self.caffe_BN_384 = nn.BatchNorm2d(256, momentum=0.1)
        self.caffe_ReLU_385 = nn.ReLU()
        self.caffe_SpatialConvolution_386 = nn.Conv2d(
            256, 1024, kernel_size=(
                1, 1), stride=(
                1, 1), padding=(
                0, 0), dilation=1, groups=1, bias=False)
        self.caffe_BN_388 = nn.BatchNorm2d(1024, momentum=0.1)
        self.caffe_ReLU_389 = nn.ReLU()
        self.caffe_SpatialConvolution_390 = nn.Conv2d(
            1024, 256, kernel_size=(
                1, 1), stride=(
                1, 1), padding=(
                0, 0), dilation=1, groups=1, bias=False)
        self.caffe_BN_391 = nn.BatchNorm2d(256, momentum=0.1)
        self.caffe_ReLU_392 = nn.ReLU()
        self.caffe_SpatialConvolution_393 = nn.Conv2d(
            256, 256, kernel_size=(
                3, 3), stride=(
                1, 1), padding=(
                1, 1), dilation=1, groups=1, bias=False)
        self.caffe_BN_394 = nn.BatchNorm2d(256, momentum=0.1)
        self.caffe_ReLU_395 = nn.ReLU()
        self.caffe_SpatialConvolution_396 = nn.Conv2d(
            256, 1024, kernel_size=(
                1, 1), stride=(
                1, 1), padding=(
                0, 0), dilation=1, groups=1, bias=False)
        self.caffe_BN_398 = nn.BatchNorm2d(1024, momentum=0.1)
        self.caffe_ReLU_399 = nn.ReLU()
        self.caffe_SpatialConvolution_400 = nn.Conv2d(
            1024, 256, kernel_size=(
                1, 1), stride=(
                1, 1), padding=(
                0, 0), dilation=1, groups=1, bias=False)
        self.caffe_BN_401 = nn.BatchNorm2d(256, momentum=0.1)
        self.caffe_ReLU_402 = nn.ReLU()
        self.caffe_SpatialConvolution_403 = nn.Conv2d(
            256, 256, kernel_size=(
                3, 3), stride=(
                1, 1), padding=(
                1, 1), dilation=1, groups=1, bias=False)
        self.caffe_BN_404 = nn.BatchNorm2d(256, momentum=0.1)
        self.caffe_ReLU_405 = nn.ReLU()
        self.caffe_SpatialConvolution_406 = nn.Conv2d(
            256, 1024, kernel_size=(
                1, 1), stride=(
                1, 1), padding=(
                0, 0), dilation=1, groups=1, bias=False)
        self.caffe_BN_408 = nn.BatchNorm2d(1024, momentum=0.1)
        self.caffe_ReLU_409 = nn.ReLU()
        self.caffe_SpatialConvolution_410 = nn.Conv2d(
            1024, 256, kernel_size=(
                1, 1), stride=(
                1, 1), padding=(
                0, 0), dilation=1, groups=1, bias=False)
        self.caffe_BN_411 = nn.BatchNorm2d(256, momentum=0.1)
        self.caffe_ReLU_412 = nn.ReLU()
        self.caffe_SpatialConvolution_413 = nn.Conv2d(
            256, 256, kernel_size=(
                3, 3), stride=(
                1, 1), padding=(
                1, 1), dilation=1, groups=1, bias=False)
        self.caffe_BN_414 = nn.BatchNorm2d(256, momentum=0.1)
        self.caffe_ReLU_415 = nn.ReLU()
        self.caffe_SpatialConvolution_416 = nn.Conv2d(
            256, 1024, kernel_size=(
                1, 1), stride=(
                1, 1), padding=(
                0, 0), dilation=1, groups=1, bias=False)
        self.caffe_BN_418 = nn.BatchNorm2d(1024, momentum=0.1)
        self.caffe_ReLU_419 = nn.ReLU()
        self.caffe_SpatialConvolution_420 = nn.Conv2d(
            1024, 256, kernel_size=(
                1, 1), stride=(
                1, 1), padding=(
                0, 0), dilation=1, groups=1, bias=False)
        self.caffe_BN_421 = nn.BatchNorm2d(256, momentum=0.1)
        self.caffe_ReLU_422 = nn.ReLU()
        self.caffe_SpatialConvolution_423 = nn.Conv2d(
            256, 256, kernel_size=(
                3, 3), stride=(
                1, 1), padding=(
                1, 1), dilation=1, groups=1, bias=False)
        self.caffe_BN_424 = nn.BatchNorm2d(256, momentum=0.1)
        self.caffe_ReLU_425 = nn.ReLU()
        self.caffe_SpatialConvolution_426 = nn.Conv2d(
            256, 1024, kernel_size=(
                1, 1), stride=(
                1, 1), padding=(
                0, 0), dilation=1, groups=1, bias=False)
        self.caffe_BN_428 = nn.BatchNorm2d(1024, momentum=0.1)
        self.caffe_ReLU_429 = nn.ReLU()
        self.caffe_SpatialConvolution_430 = nn.Conv2d(
            1024, 256, kernel_size=(
                1, 1), stride=(
                1, 1), padding=(
                0, 0), dilation=1, groups=1, bias=False)
        self.caffe_BN_431 = nn.BatchNorm2d(256, momentum=0.1)
        self.caffe_ReLU_432 = nn.ReLU()
        self.caffe_SpatialConvolution_433 = nn.Conv2d(
            256, 256, kernel_size=(
                3, 3), stride=(
                1, 1), padding=(
                1, 1), dilation=1, groups=1, bias=False)
        self.caffe_BN_434 = nn.BatchNorm2d(256, momentum=0.1)
        self.caffe_ReLU_435 = nn.ReLU()
        self.caffe_SpatialConvolution_436 = nn.Conv2d(
            256, 1024, kernel_size=(
                1, 1), stride=(
                1, 1), padding=(
                0, 0), dilation=1, groups=1, bias=False)
        self.caffe_BN_438 = nn.BatchNorm2d(1024, momentum=0.1)
        self.caffe_ReLU_439 = nn.ReLU()
        self.caffe_SpatialConvolution_440 = nn.Conv2d(
            1024, 256, kernel_size=(
                1, 1), stride=(
                1, 1), padding=(
                0, 0), dilation=1, groups=1, bias=False)
        self.caffe_BN_441 = nn.BatchNorm2d(256, momentum=0.1)
        self.caffe_ReLU_442 = nn.ReLU()
        self.caffe_SpatialConvolution_443 = nn.Conv2d(
            256, 256, kernel_size=(
                3, 3), stride=(
                1, 1), padding=(
                1, 1), dilation=1, groups=1, bias=False)
        self.caffe_BN_444 = nn.BatchNorm2d(256, momentum=0.1)
        self.caffe_ReLU_445 = nn.ReLU()
        self.caffe_SpatialConvolution_446 = nn.Conv2d(
            256, 1024, kernel_size=(
                1, 1), stride=(
                1, 1), padding=(
                0, 0), dilation=1, groups=1, bias=False)
        self.caffe_BN_448 = nn.BatchNorm2d(1024, momentum=0.1)
        self.caffe_ReLU_449 = nn.ReLU()
        self.caffe_SpatialConvolution_450 = nn.Conv2d(
            1024, 256, kernel_size=(
                1, 1), stride=(
                1, 1), padding=(
                0, 0), dilation=1, groups=1, bias=False)
        self.caffe_BN_451 = nn.BatchNorm2d(256, momentum=0.1)
        self.caffe_ReLU_452 = nn.ReLU()
        self.caffe_SpatialConvolution_453 = nn.Conv2d(
            256, 256, kernel_size=(
                3, 3), stride=(
                1, 1), padding=(
                1, 1), dilation=1, groups=1, bias=False)
        self.caffe_BN_454 = nn.BatchNorm2d(256, momentum=0.1)
        self.caffe_ReLU_455 = nn.ReLU()
        self.caffe_SpatialConvolution_456 = nn.Conv2d(
            256, 1024, kernel_size=(
                1, 1), stride=(
                1, 1), padding=(
                0, 0), dilation=1, groups=1, bias=False)
        self.caffe_BN_458 = nn.BatchNorm2d(1024, momentum=0.1)
        self.caffe_ReLU_459 = nn.ReLU()
        self.caffe_SpatialConvolution_460 = nn.Conv2d(
            1024, 256, kernel_size=(
                1, 1), stride=(
                1, 1), padding=(
                0, 0), dilation=1, groups=1, bias=False)
        self.caffe_BN_461 = nn.BatchNorm2d(256, momentum=0.1)
        self.caffe_ReLU_462 = nn.ReLU()
        self.caffe_SpatialConvolution_463 = nn.Conv2d(
            256, 256, kernel_size=(
                3, 3), stride=(
                1, 1), padding=(
                1, 1), dilation=1, groups=1, bias=False)
        self.caffe_BN_464 = nn.BatchNorm2d(256, momentum=0.1)
        self.caffe_ReLU_465 = nn.ReLU()
        self.caffe_SpatialConvolution_466 = nn.Conv2d(
            256, 1024, kernel_size=(
                1, 1), stride=(
                1, 1), padding=(
                0, 0), dilation=1, groups=1, bias=False)
        self.caffe_BN_468 = nn.BatchNorm2d(1024, momentum=0.1)
        self.caffe_ReLU_469 = nn.ReLU()
        self.caffe_SpatialConvolution_470 = nn.Conv2d(
            1024, 256, kernel_size=(
                1, 1), stride=(
                1, 1), padding=(
                0, 0), dilation=1, groups=1, bias=False)
        self.caffe_BN_471 = nn.BatchNorm2d(256, momentum=0.1)
        self.caffe_ReLU_472 = nn.ReLU()
        self.caffe_SpatialConvolution_473 = nn.Conv2d(
            256, 256, kernel_size=(
                3, 3), stride=(
                1, 1), padding=(
                1, 1), dilation=1, groups=1, bias=False)
        self.caffe_BN_474 = nn.BatchNorm2d(256, momentum=0.1)
        self.caffe_ReLU_475 = nn.ReLU()
        self.caffe_SpatialConvolution_476 = nn.Conv2d(
            256, 1024, kernel_size=(
                1, 1), stride=(
                1, 1), padding=(
                0, 0), dilation=1, groups=1, bias=False)
        self.caffe_BN_478 = nn.BatchNorm2d(1024, momentum=0.1)
        self.caffe_ReLU_479 = nn.ReLU()
        self.caffe_SpatialConvolution_480 = nn.Conv2d(
            1024, 256, kernel_size=(
                1, 1), stride=(
                1, 1), padding=(
                0, 0), dilation=1, groups=1, bias=False)
        self.caffe_BN_481 = nn.BatchNorm2d(256, momentum=0.1)
        self.caffe_ReLU_482 = nn.ReLU()
        self.caffe_SpatialConvolution_483 = nn.Conv2d(
            256, 256, kernel_size=(
                3, 3), stride=(
                1, 1), padding=(
                1, 1), dilation=1, groups=1, bias=False)
        self.caffe_BN_484 = nn.BatchNorm2d(256, momentum=0.1)
        self.caffe_ReLU_485 = nn.ReLU()
        self.caffe_SpatialConvolution_486 = nn.Conv2d(
            256, 1024, kernel_size=(
                1, 1), stride=(
                1, 1), padding=(
                0, 0), dilation=1, groups=1, bias=False)
        self.caffe_BN_488 = nn.BatchNorm2d(1024, momentum=0.1)
        self.caffe_ReLU_489 = nn.ReLU()
        self.caffe_SpatialConvolution_490 = nn.Conv2d(
            1024, 256, kernel_size=(
                1, 1), stride=(
                1, 1), padding=(
                0, 0), dilation=1, groups=1, bias=False)
        self.caffe_BN_491 = nn.BatchNorm2d(256, momentum=0.1)
        self.caffe_ReLU_492 = nn.ReLU()
        self.caffe_SpatialConvolution_493 = nn.Conv2d(
            256, 256, kernel_size=(
                3, 3), stride=(
                1, 1), padding=(
                1, 1), dilation=1, groups=1, bias=False)
        self.caffe_BN_494 = nn.BatchNorm2d(256, momentum=0.1)
        self.caffe_ReLU_495 = nn.ReLU()
        self.caffe_SpatialConvolution_496 = nn.Conv2d(
            256, 1024, kernel_size=(
                1, 1), stride=(
                1, 1), padding=(
                0, 0), dilation=1, groups=1, bias=False)
        self.caffe_BN_498 = nn.BatchNorm2d(1024, momentum=0.1)
        self.caffe_ReLU_499 = nn.ReLU()
        self.caffe_SpatialConvolution_500 = nn.Conv2d(
            1024, 256, kernel_size=(
                1, 1), stride=(
                1, 1), padding=(
                0, 0), dilation=1, groups=1, bias=False)
        self.caffe_BN_501 = nn.BatchNorm2d(256, momentum=0.1)
        self.caffe_ReLU_502 = nn.ReLU()
        self.caffe_SpatialConvolution_503 = nn.Conv2d(
            256, 256, kernel_size=(
                3, 3), stride=(
                1, 1), padding=(
                1, 1), dilation=1, groups=1, bias=False)
        self.caffe_BN_504 = nn.BatchNorm2d(256, momentum=0.1)
        self.caffe_ReLU_505 = nn.ReLU()
        self.caffe_SpatialConvolution_506 = nn.Conv2d(
            256, 1024, kernel_size=(
                1, 1), stride=(
                1, 1), padding=(
                0, 0), dilation=1, groups=1, bias=False)
        self.caffe_BN_508 = nn.BatchNorm2d(1024, momentum=0.1)
        self.caffe_ReLU_509 = nn.ReLU()
        self.caffe_SpatialConvolution_510 = nn.Conv2d(
            1024, 256, kernel_size=(
                1, 1), stride=(
                1, 1), padding=(
                0, 0), dilation=1, groups=1, bias=False)
        self.caffe_BN_511 = nn.BatchNorm2d(256, momentum=0.1)
        self.caffe_ReLU_512 = nn.ReLU()
        self.caffe_SpatialConvolution_513 = nn.Conv2d(
            256, 256, kernel_size=(
                3, 3), stride=(
                1, 1), padding=(
                1, 1), dilation=1, groups=1, bias=False)
        self.caffe_BN_514 = nn.BatchNorm2d(256, momentum=0.1)
        self.caffe_ReLU_515 = nn.ReLU()
        self.caffe_SpatialConvolution_516 = nn.Conv2d(
            256, 1024, kernel_size=(
                1, 1), stride=(
                1, 1), padding=(
                0, 0), dilation=1, groups=1, bias=False)
        self.caffe_BN_518 = nn.BatchNorm2d(1024, momentum=0.1)
        self.caffe_ReLU_519 = nn.ReLU()
        self.caffe_SpatialConvolution_520 = nn.Conv2d(
            1024, 256, kernel_size=(
                1, 1), stride=(
                1, 1), padding=(
                0, 0), dilation=1, groups=1, bias=False)
        self.caffe_BN_521 = nn.BatchNorm2d(256, momentum=0.1)
        self.caffe_ReLU_522 = nn.ReLU()
        self.caffe_SpatialConvolution_523 = nn.Conv2d(
            256, 256, kernel_size=(
                3, 3), stride=(
                1, 1), padding=(
                1, 1), dilation=1, groups=1, bias=False)
        self.caffe_BN_524 = nn.BatchNorm2d(256, momentum=0.1)
        self.caffe_ReLU_525 = nn.ReLU()
        self.caffe_SpatialConvolution_526 = nn.Conv2d(
            256, 1024, kernel_size=(
                1, 1), stride=(
                1, 1), padding=(
                0, 0), dilation=1, groups=1, bias=False)
        self.caffe_BN_528 = nn.BatchNorm2d(1024, momentum=0.1)
        self.caffe_ReLU_529 = nn.ReLU()
        self.caffe_SpatialConvolution_530 = nn.Conv2d(
            1024, 256, kernel_size=(
                1, 1), stride=(
                1, 1), padding=(
                0, 0), dilation=1, groups=1, bias=False)
        self.caffe_BN_531 = nn.BatchNorm2d(256, momentum=0.1)
        self.caffe_ReLU_532 = nn.ReLU()
        self.caffe_SpatialConvolution_533 = nn.Conv2d(
            256, 256, kernel_size=(
                3, 3), stride=(
                1, 1), padding=(
                1, 1), dilation=1, groups=1, bias=False)
        self.caffe_BN_534 = nn.BatchNorm2d(256, momentum=0.1)
        self.caffe_ReLU_535 = nn.ReLU()
        self.caffe_SpatialConvolution_536 = nn.Conv2d(
            256, 1024, kernel_size=(
                1, 1), stride=(
                1, 1), padding=(
                0, 0), dilation=1, groups=1, bias=False)
        self.caffe_BN_538 = nn.BatchNorm2d(1024, momentum=0.1)
        self.caffe_ReLU_539 = nn.ReLU()
        self.caffe_SpatialConvolution_540 = nn.Conv2d(
            1024, 256, kernel_size=(
                1, 1), stride=(
                1, 1), padding=(
                0, 0), dilation=1, groups=1, bias=False)
        self.caffe_BN_541 = nn.BatchNorm2d(256, momentum=0.1)
        self.caffe_ReLU_542 = nn.ReLU()
        self.caffe_SpatialConvolution_543 = nn.Conv2d(
            256, 256, kernel_size=(
                3, 3), stride=(
                1, 1), padding=(
                1, 1), dilation=1, groups=1, bias=False)
        self.caffe_BN_544 = nn.BatchNorm2d(256, momentum=0.1)
        self.caffe_ReLU_545 = nn.ReLU()
        self.caffe_SpatialConvolution_546 = nn.Conv2d(
            256, 1024, kernel_size=(
                1, 1), stride=(
                1, 1), padding=(
                0, 0), dilation=1, groups=1, bias=False)
        self.caffe_BN_548 = nn.BatchNorm2d(1024, momentum=0.1)
        self.caffe_ReLU_549 = nn.ReLU()
        self.caffe_SpatialConvolution_550 = nn.Conv2d(
            1024, 256, kernel_size=(
                1, 1), stride=(
                1, 1), padding=(
                0, 0), dilation=1, groups=1, bias=False)
        self.caffe_BN_551 = nn.BatchNorm2d(256, momentum=0.1)
        self.caffe_ReLU_552 = nn.ReLU()
        self.caffe_SpatialConvolution_553 = nn.Conv2d(
            256, 256, kernel_size=(
                3, 3), stride=(
                1, 1), padding=(
                1, 1), dilation=1, groups=1, bias=False)
        self.caffe_BN_554 = nn.BatchNorm2d(256, momentum=0.1)
        self.caffe_ReLU_555 = nn.ReLU()
        self.caffe_SpatialConvolution_556 = nn.Conv2d(
            256, 1024, kernel_size=(
                1, 1), stride=(
                1, 1), padding=(
                0, 0), dilation=1, groups=1, bias=False)
        self.caffe_BN_558 = nn.BatchNorm2d(1024, momentum=0.1)
        self.caffe_ReLU_559 = nn.ReLU()
        self.caffe_SpatialConvolution_560 = nn.Conv2d(
            1024, 256, kernel_size=(
                1, 1), stride=(
                1, 1), padding=(
                0, 0), dilation=1, groups=1, bias=False)
        self.caffe_BN_561 = nn.BatchNorm2d(256, momentum=0.1)
        self.caffe_ReLU_562 = nn.ReLU()
        self.caffe_SpatialConvolution_563 = nn.Conv2d(
            256, 256, kernel_size=(
                3, 3), stride=(
                1, 1), padding=(
                1, 1), dilation=1, groups=1, bias=False)
        self.caffe_BN_564 = nn.BatchNorm2d(256, momentum=0.1)
        self.caffe_ReLU_565 = nn.ReLU()
        self.caffe_SpatialConvolution_566 = nn.Conv2d(
            256, 1024, kernel_size=(
                1, 1), stride=(
                1, 1), padding=(
                0, 0), dilation=1, groups=1, bias=False)
        self.caffe_BN_568 = nn.BatchNorm2d(1024, momentum=0.1)
        self.caffe_ReLU_569 = nn.ReLU()
        self.caffe_SpatialConvolution_570 = nn.Conv2d(
            1024, 256, kernel_size=(
                1, 1), stride=(
                1, 1), padding=(
                0, 0), dilation=1, groups=1, bias=False)
        self.caffe_BN_571 = nn.BatchNorm2d(256, momentum=0.1)
        self.caffe_ReLU_572 = nn.ReLU()
        self.caffe_SpatialConvolution_573 = nn.Conv2d(
            256, 256, kernel_size=(
                3, 3), stride=(
                1, 1), padding=(
                1, 1), dilation=1, groups=1, bias=False)
        self.caffe_BN_574 = nn.BatchNorm2d(256, momentum=0.1)
        self.caffe_ReLU_575 = nn.ReLU()
        self.caffe_SpatialConvolution_576 = nn.Conv2d(
            256, 1024, kernel_size=(
                1, 1), stride=(
                1, 1), padding=(
                0, 0), dilation=1, groups=1, bias=False)
        self.caffe_BN_578 = nn.BatchNorm2d(1024, momentum=0.1)
        self.caffe_ReLU_579 = nn.ReLU()
        self.caffe_SpatialConvolution_580 = nn.Conv2d(
            1024, 256, kernel_size=(
                1, 1), stride=(
                1, 1), padding=(
                0, 0), dilation=1, groups=1, bias=False)
        self.caffe_BN_581 = nn.BatchNorm2d(256, momentum=0.1)
        self.caffe_ReLU_582 = nn.ReLU()
        self.caffe_SpatialConvolution_583 = nn.Conv2d(
            256, 256, kernel_size=(
                3, 3), stride=(
                1, 1), padding=(
                1, 1), dilation=1, groups=1, bias=False)
        self.caffe_BN_584 = nn.BatchNorm2d(256, momentum=0.1)
        self.caffe_ReLU_585 = nn.ReLU()
        self.caffe_SpatialConvolution_586 = nn.Conv2d(
            256, 1024, kernel_size=(
                1, 1), stride=(
                1, 1), padding=(
                0, 0), dilation=1, groups=1, bias=False)
        self.caffe_BN_588 = nn.BatchNorm2d(1024, momentum=0.1)
        self.caffe_ReLU_589 = nn.ReLU()
        self.caffe_SpatialConvolution_590 = nn.Conv2d(
            1024, 256, kernel_size=(
                1, 1), stride=(
                1, 1), padding=(
                0, 0), dilation=1, groups=1, bias=False)
        self.caffe_BN_591 = nn.BatchNorm2d(256, momentum=0.1)
        self.caffe_ReLU_592 = nn.ReLU()
        self.caffe_SpatialConvolution_593 = nn.Conv2d(
            256, 256, kernel_size=(
                3, 3), stride=(
                1, 1), padding=(
                1, 1), dilation=1, groups=1, bias=False)
        self.caffe_BN_594 = nn.BatchNorm2d(256, momentum=0.1)
        self.caffe_ReLU_595 = nn.ReLU()
        self.caffe_SpatialConvolution_596 = nn.Conv2d(
            256, 1024, kernel_size=(
                1, 1), stride=(
                1, 1), padding=(
                0, 0), dilation=1, groups=1, bias=False)
        self.caffe_BN_598 = nn.BatchNorm2d(1024, momentum=0.1)
        self.caffe_ReLU_599 = nn.ReLU()
        self.caffe_SpatialConvolution_600 = nn.Conv2d(
            1024, 256, kernel_size=(
                1, 1), stride=(
                1, 1), padding=(
                0, 0), dilation=1, groups=1, bias=False)
        self.caffe_BN_601 = nn.BatchNorm2d(256, momentum=0.1)
        self.caffe_ReLU_602 = nn.ReLU()
        self.caffe_SpatialConvolution_603 = nn.Conv2d(
            256, 256, kernel_size=(
                3, 3), stride=(
                1, 1), padding=(
                1, 1), dilation=1, groups=1, bias=False)
        self.caffe_BN_604 = nn.BatchNorm2d(256, momentum=0.1)
        self.caffe_ReLU_605 = nn.ReLU()
        self.caffe_SpatialConvolution_606 = nn.Conv2d(
            256, 1024, kernel_size=(
                1, 1), stride=(
                1, 1), padding=(
                0, 0), dilation=1, groups=1, bias=False)
        self.caffe_BN_608 = nn.BatchNorm2d(1024, momentum=0.1)
        self.caffe_ReLU_609 = nn.ReLU()
        self.caffe_SpatialConvolution_610 = nn.Conv2d(
            1024, 256, kernel_size=(
                1, 1), stride=(
                1, 1), padding=(
                0, 0), dilation=1, groups=1, bias=False)
        self.caffe_BN_611 = nn.BatchNorm2d(256, momentum=0.1)
        self.caffe_ReLU_612 = nn.ReLU()
        self.caffe_SpatialConvolution_613 = nn.Conv2d(
            256, 256, kernel_size=(
                3, 3), stride=(
                1, 1), padding=(
                1, 1), dilation=1, groups=1, bias=False)
        self.caffe_BN_614 = nn.BatchNorm2d(256, momentum=0.1)
        self.caffe_ReLU_615 = nn.ReLU()
        self.caffe_SpatialConvolution_616 = nn.Conv2d(
            256, 1024, kernel_size=(
                1, 1), stride=(
                1, 1), padding=(
                0, 0), dilation=1, groups=1, bias=False)
        self.caffe_BN_618 = nn.BatchNorm2d(1024, momentum=0.1)
        self.caffe_ReLU_619 = nn.ReLU()
        self.caffe_SpatialConvolution_620 = nn.Conv2d(
            1024, 256, kernel_size=(
                1, 1), stride=(
                1, 1), padding=(
                0, 0), dilation=1, groups=1, bias=False)
        self.caffe_BN_621 = nn.BatchNorm2d(256, momentum=0.1)
        self.caffe_ReLU_622 = nn.ReLU()
        self.caffe_SpatialConvolution_623 = nn.Conv2d(
            256, 256, kernel_size=(
                3, 3), stride=(
                1, 1), padding=(
                1, 1), dilation=1, groups=1, bias=False)
        self.caffe_BN_624 = nn.BatchNorm2d(256, momentum=0.1)
        self.caffe_ReLU_625 = nn.ReLU()
        self.caffe_SpatialConvolution_626 = nn.Conv2d(
            256, 1024, kernel_size=(
                1, 1), stride=(
                1, 1), padding=(
                0, 0), dilation=1, groups=1, bias=False)
        self.caffe_BN_628 = nn.BatchNorm2d(1024, momentum=0.1)
        self.caffe_ReLU_629 = nn.ReLU()
        self.caffe_SpatialConvolution_630 = nn.Conv2d(
            1024, 256, kernel_size=(
                1, 1), stride=(
                1, 1), padding=(
                0, 0), dilation=1, groups=1, bias=False)
        self.caffe_BN_631 = nn.BatchNorm2d(256, momentum=0.1)
        self.caffe_ReLU_632 = nn.ReLU()
        self.caffe_SpatialConvolution_633 = nn.Conv2d(
            256, 256, kernel_size=(
                3, 3), stride=(
                1, 1), padding=(
                1, 1), dilation=1, groups=1, bias=False)
        self.caffe_BN_634 = nn.BatchNorm2d(256, momentum=0.1)
        self.caffe_ReLU_635 = nn.ReLU()
        self.caffe_SpatialConvolution_636 = nn.Conv2d(
            256, 1024, kernel_size=(
                1, 1), stride=(
                1, 1), padding=(
                0, 0), dilation=1, groups=1, bias=False)
        self.caffe_BN_638 = nn.BatchNorm2d(1024, momentum=0.1)
        self.caffe_ReLU_639 = nn.ReLU()
        self.caffe_SpatialConvolution_640 = nn.Conv2d(
            1024, 512, kernel_size=(
                1, 1), stride=(
                1, 1), padding=(
                0, 0), dilation=1, groups=1, bias=False)
        self.caffe_BN_641 = nn.BatchNorm2d(512, momentum=0.1)
        self.caffe_ReLU_642 = nn.ReLU()
        self.caffe_SpatialConvolution_643 = nn.Conv2d(
            512, 512, kernel_size=(
                3, 3), stride=(
                2, 2), padding=(
                1, 1), dilation=1, groups=1, bias=False)
        self.caffe_BN_644 = nn.BatchNorm2d(512, momentum=0.1)
        self.caffe_ReLU_645 = nn.ReLU()
        self.caffe_SpatialConvolution_646 = nn.Conv2d(
            512, 2048, kernel_size=(
                1, 1), stride=(
                1, 1), padding=(
                0, 0), dilation=1, groups=1, bias=False)
        self.caffe_SpatialConvolution_647 = nn.Conv2d(
            1024, 2048, kernel_size=(
                1, 1), stride=(
                2, 2), padding=(
                0, 0), dilation=1, groups=1, bias=False)
        self.caffe_BN_648 = nn.BatchNorm2d(2048, momentum=0.1)
        self.caffe_BN_650 = nn.BatchNorm2d(2048, momentum=0.1)
        self.caffe_ReLU_651 = nn.ReLU()
        self.caffe_SpatialConvolution_652 = nn.Conv2d(
            2048, 512, kernel_size=(
                1, 1), stride=(
                1, 1), padding=(
                0, 0), dilation=1, groups=1, bias=False)
        self.caffe_BN_653 = nn.BatchNorm2d(512, momentum=0.1)
        self.caffe_ReLU_654 = nn.ReLU()
        self.caffe_SpatialConvolution_655 = nn.Conv2d(
            512, 512, kernel_size=(
                3, 3), stride=(
                1, 1), padding=(
                1, 1), dilation=1, groups=1, bias=False)
        self.caffe_BN_656 = nn.BatchNorm2d(512, momentum=0.1)
        self.caffe_ReLU_657 = nn.ReLU()
        self.caffe_SpatialConvolution_658 = nn.Conv2d(
            512, 2048, kernel_size=(
                1, 1), stride=(
                1, 1), padding=(
                0, 0), dilation=1, groups=1, bias=False)
        self.caffe_BN_660 = nn.BatchNorm2d(2048, momentum=0.1)
        self.caffe_ReLU_661 = nn.ReLU()
        self.caffe_SpatialConvolution_662 = nn.Conv2d(
            2048, 512, kernel_size=(
                1, 1), stride=(
                1, 1), padding=(
                0, 0), dilation=1, groups=1, bias=False)
        self.caffe_BN_663 = nn.BatchNorm2d(512, momentum=0.1)
        self.caffe_ReLU_664 = nn.ReLU()
        self.caffe_SpatialConvolution_665 = nn.Conv2d(
            512, 512, kernel_size=(
                3, 3), stride=(
                1, 1), padding=(
                1, 1), dilation=1, groups=1, bias=False)
        self.caffe_BN_666 = nn.BatchNorm2d(512, momentum=0.1)
        self.caffe_ReLU_667 = nn.ReLU()
        self.caffe_SpatialConvolution_668 = nn.Conv2d(
            512, 2048, kernel_size=(
                1, 1), stride=(
                1, 1), padding=(
                0, 0), dilation=1, groups=1, bias=False)
        self.caffe_BN_670 = nn.BatchNorm2d(2048, momentum=0.1)
        self.caffe_ReLU_671 = nn.ReLU()
        self.caffe_Flatten_673 = nn.Flatten()
        self.caffe_Dropout_674 = nn.Dropout(0.699999988079)
        self.caffe_InnerProduct_675 = nn.Linear(2048, 200)

        if pretrained_model is True:
            state_dict = torch.load(get_resnet200_pretrained_model())
            self.load_state_dict(state_dict)

    def forward(self, data):
        caffe_SpatialConvolution_0 = self.caffe_SpatialConvolution_0(data)
        # return caffe_SpatialConvolution_0
        caffe_Pooling_1 = self.caffe_Pooling_1(caffe_SpatialConvolution_0)
        # return caffe_Pooling_1
        caffe_BN_2 = self.caffe_BN_2(caffe_Pooling_1)
        caffe_BN_2 = self.caffe_ReLU_3(caffe_BN_2)
        caffe_SpatialConvolution_4 = self.caffe_SpatialConvolution_4(
            caffe_BN_2)
        caffe_BN_5 = self.caffe_BN_5(caffe_SpatialConvolution_4)
        caffe_BN_5 = self.caffe_ReLU_6(caffe_BN_5)
        caffe_SpatialConvolution_7 = self.caffe_SpatialConvolution_7(
            caffe_BN_5)
        caffe_BN_8 = self.caffe_BN_8(caffe_SpatialConvolution_7)
        caffe_BN_8 = self.caffe_ReLU_9(caffe_BN_8)
        caffe_SpatialConvolution_10 = self.caffe_SpatialConvolution_10(
            caffe_BN_8)
        caffe_SpatialConvolution_11 = self.caffe_SpatialConvolution_11(
            caffe_Pooling_1)
        caffe_BN_12 = self.caffe_BN_12(caffe_SpatialConvolution_11)
        caffe_Eltwise_13 = torch.add(caffe_SpatialConvolution_10, caffe_BN_12)
        caffe_BN_14 = self.caffe_BN_14(caffe_Eltwise_13)
        caffe_BN_14 = self.caffe_ReLU_15(caffe_BN_14)
        caffe_SpatialConvolution_16 = self.caffe_SpatialConvolution_16(
            caffe_BN_14)
        caffe_BN_17 = self.caffe_BN_17(caffe_SpatialConvolution_16)
        caffe_BN_17 = self.caffe_ReLU_18(caffe_BN_17)
        caffe_SpatialConvolution_19 = self.caffe_SpatialConvolution_19(
            caffe_BN_17)
        caffe_BN_20 = self.caffe_BN_20(caffe_SpatialConvolution_19)
        caffe_BN_20 = self.caffe_ReLU_21(caffe_BN_20)
        caffe_SpatialConvolution_22 = self.caffe_SpatialConvolution_22(
            caffe_BN_20)
        caffe_Eltwise_23 = torch.add(
            caffe_SpatialConvolution_22, caffe_Eltwise_13)
        caffe_BN_24 = self.caffe_BN_24(caffe_Eltwise_23)
        caffe_BN_24 = self.caffe_ReLU_25(caffe_BN_24)
        caffe_SpatialConvolution_26 = self.caffe_SpatialConvolution_26(
            caffe_BN_24)
        caffe_BN_27 = self.caffe_BN_27(caffe_SpatialConvolution_26)
        caffe_BN_27 = self.caffe_ReLU_28(caffe_BN_27)
        caffe_SpatialConvolution_29 = self.caffe_SpatialConvolution_29(
            caffe_BN_27)
        caffe_BN_30 = self.caffe_BN_30(caffe_SpatialConvolution_29)
        caffe_BN_30 = self.caffe_ReLU_31(caffe_BN_30)
        caffe_SpatialConvolution_32 = self.caffe_SpatialConvolution_32(
            caffe_BN_30)
        caffe_Eltwise_33 = torch.add(
            caffe_SpatialConvolution_32, caffe_Eltwise_23)
        caffe_BN_34 = self.caffe_BN_34(caffe_Eltwise_33)
        caffe_BN_34 = self.caffe_ReLU_35(caffe_BN_34)
        caffe_SpatialConvolution_36 = self.caffe_SpatialConvolution_36(
            caffe_BN_34)
        caffe_BN_37 = self.caffe_BN_37(caffe_SpatialConvolution_36)
        caffe_BN_37 = self.caffe_ReLU_38(caffe_BN_37)
        caffe_SpatialConvolution_39 = self.caffe_SpatialConvolution_39(
            caffe_BN_37)
        caffe_BN_40 = self.caffe_BN_40(caffe_SpatialConvolution_39)
        caffe_BN_40 = self.caffe_ReLU_41(caffe_BN_40)
        caffe_SpatialConvolution_42 = self.caffe_SpatialConvolution_42(
            caffe_BN_40)
        caffe_SpatialConvolution_43 = self.caffe_SpatialConvolution_43(
            caffe_Eltwise_33)
        caffe_BN_44 = self.caffe_BN_44(caffe_SpatialConvolution_43)
        caffe_Eltwise_45 = torch.add(caffe_SpatialConvolution_42, caffe_BN_44)
        caffe_BN_46 = self.caffe_BN_46(caffe_Eltwise_45)
        caffe_BN_46 = self.caffe_ReLU_47(caffe_BN_46)
        caffe_SpatialConvolution_48 = self.caffe_SpatialConvolution_48(
            caffe_BN_46)
        caffe_BN_49 = self.caffe_BN_49(caffe_SpatialConvolution_48)
        caffe_BN_49 = self.caffe_ReLU_50(caffe_BN_49)
        caffe_SpatialConvolution_51 = self.caffe_SpatialConvolution_51(
            caffe_BN_49)
        # return caffe_SpatialConvolution_51
        caffe_BN_52 = self.caffe_BN_52(caffe_SpatialConvolution_51)
        caffe_BN_52 = self.caffe_ReLU_53(caffe_BN_52)
        caffe_SpatialConvolution_54 = self.caffe_SpatialConvolution_54(
            caffe_BN_52)
        caffe_Eltwise_55 = torch.add(
            caffe_SpatialConvolution_54, caffe_Eltwise_45)
        caffe_BN_56 = self.caffe_BN_56(caffe_Eltwise_55)
        caffe_BN_56 = self.caffe_ReLU_57(caffe_BN_56)
        caffe_SpatialConvolution_58 = self.caffe_SpatialConvolution_58(
            caffe_BN_56)
        caffe_BN_59 = self.caffe_BN_59(caffe_SpatialConvolution_58)
        caffe_BN_59 = self.caffe_ReLU_60(caffe_BN_59)
        caffe_SpatialConvolution_61 = self.caffe_SpatialConvolution_61(
            caffe_BN_59)
        caffe_BN_62 = self.caffe_BN_62(caffe_SpatialConvolution_61)
        caffe_BN_62 = self.caffe_ReLU_63(caffe_BN_62)
        caffe_SpatialConvolution_64 = self.caffe_SpatialConvolution_64(
            caffe_BN_62)
        caffe_Eltwise_65 = torch.add(
            caffe_SpatialConvolution_64, caffe_Eltwise_55)
        caffe_BN_66 = self.caffe_BN_66(caffe_Eltwise_65)
        caffe_BN_66 = self.caffe_ReLU_67(caffe_BN_66)
        caffe_SpatialConvolution_68 = self.caffe_SpatialConvolution_68(
            caffe_BN_66)
        caffe_BN_69 = self.caffe_BN_69(caffe_SpatialConvolution_68)
        caffe_BN_69 = self.caffe_ReLU_70(caffe_BN_69)
        caffe_SpatialConvolution_71 = self.caffe_SpatialConvolution_71(
            caffe_BN_69)
        caffe_BN_72 = self.caffe_BN_72(caffe_SpatialConvolution_71)
        caffe_BN_72 = self.caffe_ReLU_73(caffe_BN_72)
        caffe_SpatialConvolution_74 = self.caffe_SpatialConvolution_74(
            caffe_BN_72)
        caffe_Eltwise_75 = torch.add(
            caffe_SpatialConvolution_74, caffe_Eltwise_65)
        caffe_BN_76 = self.caffe_BN_76(caffe_Eltwise_75)
        caffe_BN_76 = self.caffe_ReLU_77(caffe_BN_76)
        caffe_SpatialConvolution_78 = self.caffe_SpatialConvolution_78(
            caffe_BN_76)
        caffe_BN_79 = self.caffe_BN_79(caffe_SpatialConvolution_78)
        caffe_BN_79 = self.caffe_ReLU_80(caffe_BN_79)
        caffe_SpatialConvolution_81 = self.caffe_SpatialConvolution_81(
            caffe_BN_79)
        caffe_BN_82 = self.caffe_BN_82(caffe_SpatialConvolution_81)
        caffe_BN_82 = self.caffe_ReLU_83(caffe_BN_82)
        caffe_SpatialConvolution_84 = self.caffe_SpatialConvolution_84(
            caffe_BN_82)
        caffe_Eltwise_85 = torch.add(
            caffe_SpatialConvolution_84, caffe_Eltwise_75)
        caffe_BN_86 = self.caffe_BN_86(caffe_Eltwise_85)
        caffe_BN_86 = self.caffe_ReLU_87(caffe_BN_86)
        caffe_SpatialConvolution_88 = self.caffe_SpatialConvolution_88(
            caffe_BN_86)
        caffe_BN_89 = self.caffe_BN_89(caffe_SpatialConvolution_88)
        caffe_BN_89 = self.caffe_ReLU_90(caffe_BN_89)
        caffe_SpatialConvolution_91 = self.caffe_SpatialConvolution_91(
            caffe_BN_89)
        caffe_BN_92 = self.caffe_BN_92(caffe_SpatialConvolution_91)
        caffe_BN_92 = self.caffe_ReLU_93(caffe_BN_92)
        caffe_SpatialConvolution_94 = self.caffe_SpatialConvolution_94(
            caffe_BN_92)
        caffe_Eltwise_95 = torch.add(
            caffe_SpatialConvolution_94, caffe_Eltwise_85)
        caffe_BN_96 = self.caffe_BN_96(caffe_Eltwise_95)
        caffe_BN_96 = self.caffe_ReLU_97(caffe_BN_96)
        caffe_SpatialConvolution_98 = self.caffe_SpatialConvolution_98(
            caffe_BN_96)
        caffe_BN_99 = self.caffe_BN_99(caffe_SpatialConvolution_98)
        caffe_BN_99 = self.caffe_ReLU_100(caffe_BN_99)
        caffe_SpatialConvolution_101 = self.caffe_SpatialConvolution_101(
            caffe_BN_99)
        caffe_BN_102 = self.caffe_BN_102(caffe_SpatialConvolution_101)
        caffe_BN_102 = self.caffe_ReLU_103(caffe_BN_102)
        caffe_SpatialConvolution_104 = self.caffe_SpatialConvolution_104(
            caffe_BN_102)
        caffe_Eltwise_105 = torch.add(
            caffe_SpatialConvolution_104, caffe_Eltwise_95)
        caffe_BN_106 = self.caffe_BN_106(caffe_Eltwise_105)
        caffe_BN_106 = self.caffe_ReLU_107(caffe_BN_106)
        caffe_SpatialConvolution_108 = self.caffe_SpatialConvolution_108(
            caffe_BN_106)
        caffe_BN_109 = self.caffe_BN_109(caffe_SpatialConvolution_108)
        caffe_BN_109 = self.caffe_ReLU_110(caffe_BN_109)
        caffe_SpatialConvolution_111 = self.caffe_SpatialConvolution_111(
            caffe_BN_109)
        caffe_BN_112 = self.caffe_BN_112(caffe_SpatialConvolution_111)
        caffe_BN_112 = self.caffe_ReLU_113(caffe_BN_112)
        caffe_SpatialConvolution_114 = self.caffe_SpatialConvolution_114(
            caffe_BN_112)
        caffe_Eltwise_115 = torch.add(
            caffe_SpatialConvolution_114,
            caffe_Eltwise_105)
        caffe_BN_116 = self.caffe_BN_116(caffe_Eltwise_115)
        caffe_BN_116 = self.caffe_ReLU_117(caffe_BN_116)
        caffe_SpatialConvolution_118 = self.caffe_SpatialConvolution_118(
            caffe_BN_116)
        caffe_BN_119 = self.caffe_BN_119(caffe_SpatialConvolution_118)
        caffe_BN_119 = self.caffe_ReLU_120(caffe_BN_119)
        caffe_SpatialConvolution_121 = self.caffe_SpatialConvolution_121(
            caffe_BN_119)
        caffe_BN_122 = self.caffe_BN_122(caffe_SpatialConvolution_121)
        caffe_BN_122 = self.caffe_ReLU_123(caffe_BN_122)
        caffe_SpatialConvolution_124 = self.caffe_SpatialConvolution_124(
            caffe_BN_122)
        caffe_Eltwise_125 = torch.add(
            caffe_SpatialConvolution_124,
            caffe_Eltwise_115)
        caffe_BN_126 = self.caffe_BN_126(caffe_Eltwise_125)
        caffe_BN_126 = self.caffe_ReLU_127(caffe_BN_126)
        caffe_SpatialConvolution_128 = self.caffe_SpatialConvolution_128(
            caffe_BN_126)
        caffe_BN_129 = self.caffe_BN_129(caffe_SpatialConvolution_128)
        caffe_BN_129 = self.caffe_ReLU_130(caffe_BN_129)
        caffe_SpatialConvolution_131 = self.caffe_SpatialConvolution_131(
            caffe_BN_129)
        caffe_BN_132 = self.caffe_BN_132(caffe_SpatialConvolution_131)
        caffe_BN_132 = self.caffe_ReLU_133(caffe_BN_132)
        caffe_SpatialConvolution_134 = self.caffe_SpatialConvolution_134(
            caffe_BN_132)
        caffe_Eltwise_135 = torch.add(
            caffe_SpatialConvolution_134,
            caffe_Eltwise_125)
        caffe_BN_136 = self.caffe_BN_136(caffe_Eltwise_135)
        caffe_BN_136 = self.caffe_ReLU_137(caffe_BN_136)
        caffe_SpatialConvolution_138 = self.caffe_SpatialConvolution_138(
            caffe_BN_136)
        caffe_BN_139 = self.caffe_BN_139(caffe_SpatialConvolution_138)
        caffe_BN_139 = self.caffe_ReLU_140(caffe_BN_139)
        caffe_SpatialConvolution_141 = self.caffe_SpatialConvolution_141(
            caffe_BN_139)
        caffe_BN_142 = self.caffe_BN_142(caffe_SpatialConvolution_141)
        caffe_BN_142 = self.caffe_ReLU_143(caffe_BN_142)
        caffe_SpatialConvolution_144 = self.caffe_SpatialConvolution_144(
            caffe_BN_142)
        caffe_Eltwise_145 = torch.add(
            caffe_SpatialConvolution_144,
            caffe_Eltwise_135)
        caffe_BN_146 = self.caffe_BN_146(caffe_Eltwise_145)
        caffe_BN_146 = self.caffe_ReLU_147(caffe_BN_146)
        caffe_SpatialConvolution_148 = self.caffe_SpatialConvolution_148(
            caffe_BN_146)
        caffe_BN_149 = self.caffe_BN_149(caffe_SpatialConvolution_148)
        caffe_BN_149 = self.caffe_ReLU_150(caffe_BN_149)
        caffe_SpatialConvolution_151 = self.caffe_SpatialConvolution_151(
            caffe_BN_149)
        caffe_BN_152 = self.caffe_BN_152(caffe_SpatialConvolution_151)
        caffe_BN_152 = self.caffe_ReLU_153(caffe_BN_152)
        caffe_SpatialConvolution_154 = self.caffe_SpatialConvolution_154(
            caffe_BN_152)
        caffe_Eltwise_155 = torch.add(
            caffe_SpatialConvolution_154,
            caffe_Eltwise_145)
        caffe_BN_156 = self.caffe_BN_156(caffe_Eltwise_155)
        caffe_BN_156 = self.caffe_ReLU_157(caffe_BN_156)
        caffe_SpatialConvolution_158 = self.caffe_SpatialConvolution_158(
            caffe_BN_156)
        caffe_BN_159 = self.caffe_BN_159(caffe_SpatialConvolution_158)
        caffe_BN_159 = self.caffe_ReLU_160(caffe_BN_159)
        caffe_SpatialConvolution_161 = self.caffe_SpatialConvolution_161(
            caffe_BN_159)
        caffe_BN_162 = self.caffe_BN_162(caffe_SpatialConvolution_161)
        caffe_BN_162 = self.caffe_ReLU_163(caffe_BN_162)
        caffe_SpatialConvolution_164 = self.caffe_SpatialConvolution_164(
            caffe_BN_162)
        caffe_Eltwise_165 = torch.add(
            caffe_SpatialConvolution_164,
            caffe_Eltwise_155)
        caffe_BN_166 = self.caffe_BN_166(caffe_Eltwise_165)
        caffe_BN_166 = self.caffe_ReLU_167(caffe_BN_166)
        caffe_SpatialConvolution_168 = self.caffe_SpatialConvolution_168(
            caffe_BN_166)
        caffe_BN_169 = self.caffe_BN_169(caffe_SpatialConvolution_168)
        caffe_BN_169 = self.caffe_ReLU_170(caffe_BN_169)
        caffe_SpatialConvolution_171 = self.caffe_SpatialConvolution_171(
            caffe_BN_169)
        caffe_BN_172 = self.caffe_BN_172(caffe_SpatialConvolution_171)
        caffe_BN_172 = self.caffe_ReLU_173(caffe_BN_172)
        caffe_SpatialConvolution_174 = self.caffe_SpatialConvolution_174(
            caffe_BN_172)
        caffe_Eltwise_175 = torch.add(
            caffe_SpatialConvolution_174,
            caffe_Eltwise_165)
        caffe_BN_176 = self.caffe_BN_176(caffe_Eltwise_175)
        caffe_BN_176 = self.caffe_ReLU_177(caffe_BN_176)
        caffe_SpatialConvolution_178 = self.caffe_SpatialConvolution_178(
            caffe_BN_176)
        caffe_BN_179 = self.caffe_BN_179(caffe_SpatialConvolution_178)
        caffe_BN_179 = self.caffe_ReLU_180(caffe_BN_179)
        caffe_SpatialConvolution_181 = self.caffe_SpatialConvolution_181(
            caffe_BN_179)
        # return caffe_SpatialConvolution_181
        caffe_BN_182 = self.caffe_BN_182(caffe_SpatialConvolution_181)
        caffe_BN_182 = self.caffe_ReLU_183(caffe_BN_182)
        caffe_SpatialConvolution_184 = self.caffe_SpatialConvolution_184(
            caffe_BN_182)
        caffe_Eltwise_185 = torch.add(
            caffe_SpatialConvolution_184,
            caffe_Eltwise_175)
        caffe_BN_186 = self.caffe_BN_186(caffe_Eltwise_185)
        caffe_BN_186 = self.caffe_ReLU_187(caffe_BN_186)
        caffe_SpatialConvolution_188 = self.caffe_SpatialConvolution_188(
            caffe_BN_186)
        caffe_BN_189 = self.caffe_BN_189(caffe_SpatialConvolution_188)
        caffe_BN_189 = self.caffe_ReLU_190(caffe_BN_189)
        caffe_SpatialConvolution_191 = self.caffe_SpatialConvolution_191(
            caffe_BN_189)
        caffe_BN_192 = self.caffe_BN_192(caffe_SpatialConvolution_191)
        caffe_BN_192 = self.caffe_ReLU_193(caffe_BN_192)
        caffe_SpatialConvolution_194 = self.caffe_SpatialConvolution_194(
            caffe_BN_192)
        caffe_Eltwise_195 = torch.add(
            caffe_SpatialConvolution_194,
            caffe_Eltwise_185)
        caffe_BN_196 = self.caffe_BN_196(caffe_Eltwise_195)
        caffe_BN_196 = self.caffe_ReLU_197(caffe_BN_196)
        caffe_SpatialConvolution_198 = self.caffe_SpatialConvolution_198(
            caffe_BN_196)
        caffe_BN_199 = self.caffe_BN_199(caffe_SpatialConvolution_198)
        caffe_BN_199 = self.caffe_ReLU_200(caffe_BN_199)
        caffe_SpatialConvolution_201 = self.caffe_SpatialConvolution_201(
            caffe_BN_199)
        caffe_BN_202 = self.caffe_BN_202(caffe_SpatialConvolution_201)
        caffe_BN_202 = self.caffe_ReLU_203(caffe_BN_202)
        caffe_SpatialConvolution_204 = self.caffe_SpatialConvolution_204(
            caffe_BN_202)
        caffe_Eltwise_205 = torch.add(
            caffe_SpatialConvolution_204,
            caffe_Eltwise_195)
        caffe_BN_206 = self.caffe_BN_206(caffe_Eltwise_205)
        caffe_BN_206 = self.caffe_ReLU_207(caffe_BN_206)
        caffe_SpatialConvolution_208 = self.caffe_SpatialConvolution_208(
            caffe_BN_206)
        caffe_BN_209 = self.caffe_BN_209(caffe_SpatialConvolution_208)
        caffe_BN_209 = self.caffe_ReLU_210(caffe_BN_209)
        caffe_SpatialConvolution_211 = self.caffe_SpatialConvolution_211(
            caffe_BN_209)
        caffe_BN_212 = self.caffe_BN_212(caffe_SpatialConvolution_211)
        caffe_BN_212 = self.caffe_ReLU_213(caffe_BN_212)
        caffe_SpatialConvolution_214 = self.caffe_SpatialConvolution_214(
            caffe_BN_212)
        caffe_Eltwise_215 = torch.add(
            caffe_SpatialConvolution_214,
            caffe_Eltwise_205)
        caffe_BN_216 = self.caffe_BN_216(caffe_Eltwise_215)
        caffe_BN_216 = self.caffe_ReLU_217(caffe_BN_216)
        caffe_SpatialConvolution_218 = self.caffe_SpatialConvolution_218(
            caffe_BN_216)
        caffe_BN_219 = self.caffe_BN_219(caffe_SpatialConvolution_218)
        caffe_BN_219 = self.caffe_ReLU_220(caffe_BN_219)
        caffe_SpatialConvolution_221 = self.caffe_SpatialConvolution_221(
            caffe_BN_219)
        caffe_BN_222 = self.caffe_BN_222(caffe_SpatialConvolution_221)
        caffe_BN_222 = self.caffe_ReLU_223(caffe_BN_222)
        caffe_SpatialConvolution_224 = self.caffe_SpatialConvolution_224(
            caffe_BN_222)
        caffe_Eltwise_225 = torch.add(
            caffe_SpatialConvolution_224,
            caffe_Eltwise_215)
        caffe_BN_226 = self.caffe_BN_226(caffe_Eltwise_225)
        caffe_BN_226 = self.caffe_ReLU_227(caffe_BN_226)
        caffe_SpatialConvolution_228 = self.caffe_SpatialConvolution_228(
            caffe_BN_226)
        caffe_BN_229 = self.caffe_BN_229(caffe_SpatialConvolution_228)
        caffe_BN_229 = self.caffe_ReLU_230(caffe_BN_229)
        caffe_SpatialConvolution_231 = self.caffe_SpatialConvolution_231(
            caffe_BN_229)
        caffe_BN_232 = self.caffe_BN_232(caffe_SpatialConvolution_231)
        caffe_BN_232 = self.caffe_ReLU_233(caffe_BN_232)
        caffe_SpatialConvolution_234 = self.caffe_SpatialConvolution_234(
            caffe_BN_232)
        caffe_Eltwise_235 = torch.add(
            caffe_SpatialConvolution_234,
            caffe_Eltwise_225)
        caffe_BN_236 = self.caffe_BN_236(caffe_Eltwise_235)
        caffe_BN_236 = self.caffe_ReLU_237(caffe_BN_236)
        caffe_SpatialConvolution_238 = self.caffe_SpatialConvolution_238(
            caffe_BN_236)
        caffe_BN_239 = self.caffe_BN_239(caffe_SpatialConvolution_238)
        caffe_BN_239 = self.caffe_ReLU_240(caffe_BN_239)
        caffe_SpatialConvolution_241 = self.caffe_SpatialConvolution_241(
            caffe_BN_239)
        caffe_BN_242 = self.caffe_BN_242(caffe_SpatialConvolution_241)
        caffe_BN_242 = self.caffe_ReLU_243(caffe_BN_242)
        caffe_SpatialConvolution_244 = self.caffe_SpatialConvolution_244(
            caffe_BN_242)
        caffe_Eltwise_245 = torch.add(
            caffe_SpatialConvolution_244,
            caffe_Eltwise_235)
        caffe_BN_246 = self.caffe_BN_246(caffe_Eltwise_245)
        caffe_BN_246 = self.caffe_ReLU_247(caffe_BN_246)
        caffe_SpatialConvolution_248 = self.caffe_SpatialConvolution_248(
            caffe_BN_246)
        caffe_BN_249 = self.caffe_BN_249(caffe_SpatialConvolution_248)
        caffe_BN_249 = self.caffe_ReLU_250(caffe_BN_249)
        caffe_SpatialConvolution_251 = self.caffe_SpatialConvolution_251(
            caffe_BN_249)
        caffe_BN_252 = self.caffe_BN_252(caffe_SpatialConvolution_251)
        caffe_BN_252 = self.caffe_ReLU_253(caffe_BN_252)
        caffe_SpatialConvolution_254 = self.caffe_SpatialConvolution_254(
            caffe_BN_252)
        caffe_Eltwise_255 = torch.add(
            caffe_SpatialConvolution_254,
            caffe_Eltwise_245)
        caffe_BN_256 = self.caffe_BN_256(caffe_Eltwise_255)
        caffe_BN_256 = self.caffe_ReLU_257(caffe_BN_256)
        caffe_SpatialConvolution_258 = self.caffe_SpatialConvolution_258(
            caffe_BN_256)
        caffe_BN_259 = self.caffe_BN_259(caffe_SpatialConvolution_258)
        caffe_BN_259 = self.caffe_ReLU_260(caffe_BN_259)
        caffe_SpatialConvolution_261 = self.caffe_SpatialConvolution_261(
            caffe_BN_259)
        caffe_BN_262 = self.caffe_BN_262(caffe_SpatialConvolution_261)
        caffe_BN_262 = self.caffe_ReLU_263(caffe_BN_262)
        caffe_SpatialConvolution_264 = self.caffe_SpatialConvolution_264(
            caffe_BN_262)
        caffe_Eltwise_265 = torch.add(
            caffe_SpatialConvolution_264,
            caffe_Eltwise_255)
        caffe_BN_266 = self.caffe_BN_266(caffe_Eltwise_265)
        caffe_BN_266 = self.caffe_ReLU_267(caffe_BN_266)
        caffe_SpatialConvolution_268 = self.caffe_SpatialConvolution_268(
            caffe_BN_266)
        caffe_BN_269 = self.caffe_BN_269(caffe_SpatialConvolution_268)
        caffe_BN_269 = self.caffe_ReLU_270(caffe_BN_269)
        caffe_SpatialConvolution_271 = self.caffe_SpatialConvolution_271(
            caffe_BN_269)
        caffe_BN_272 = self.caffe_BN_272(caffe_SpatialConvolution_271)
        caffe_BN_272 = self.caffe_ReLU_273(caffe_BN_272)
        caffe_SpatialConvolution_274 = self.caffe_SpatialConvolution_274(
            caffe_BN_272)
        caffe_Eltwise_275 = torch.add(
            caffe_SpatialConvolution_274,
            caffe_Eltwise_265)
        caffe_BN_276 = self.caffe_BN_276(caffe_Eltwise_275)
        caffe_BN_276 = self.caffe_ReLU_277(caffe_BN_276)
        caffe_SpatialConvolution_278 = self.caffe_SpatialConvolution_278(
            caffe_BN_276)
        caffe_BN_279 = self.caffe_BN_279(caffe_SpatialConvolution_278)
        caffe_BN_279 = self.caffe_ReLU_280(caffe_BN_279)
        caffe_SpatialConvolution_281 = self.caffe_SpatialConvolution_281(
            caffe_BN_279)
        caffe_BN_282 = self.caffe_BN_282(caffe_SpatialConvolution_281)
        caffe_BN_282 = self.caffe_ReLU_283(caffe_BN_282)
        caffe_SpatialConvolution_284 = self.caffe_SpatialConvolution_284(
            caffe_BN_282)
        caffe_SpatialConvolution_285 = self.caffe_SpatialConvolution_285(
            caffe_Eltwise_275)
        caffe_BN_286 = self.caffe_BN_286(caffe_SpatialConvolution_285)
        caffe_Eltwise_287 = torch.add(
            caffe_SpatialConvolution_284, caffe_BN_286)
        caffe_BN_288 = self.caffe_BN_288(caffe_Eltwise_287)
        caffe_BN_288 = self.caffe_ReLU_289(caffe_BN_288)
        caffe_SpatialConvolution_290 = self.caffe_SpatialConvolution_290(
            caffe_BN_288)
        caffe_BN_291 = self.caffe_BN_291(caffe_SpatialConvolution_290)
        caffe_BN_291 = self.caffe_ReLU_292(caffe_BN_291)
        caffe_SpatialConvolution_293 = self.caffe_SpatialConvolution_293(
            caffe_BN_291)
        caffe_BN_294 = self.caffe_BN_294(caffe_SpatialConvolution_293)
        caffe_BN_294 = self.caffe_ReLU_295(caffe_BN_294)
        caffe_SpatialConvolution_296 = self.caffe_SpatialConvolution_296(
            caffe_BN_294)
        caffe_Eltwise_297 = torch.add(
            caffe_SpatialConvolution_296,
            caffe_Eltwise_287)
        caffe_BN_298 = self.caffe_BN_298(caffe_Eltwise_297)
        caffe_BN_298 = self.caffe_ReLU_299(caffe_BN_298)
        caffe_SpatialConvolution_300 = self.caffe_SpatialConvolution_300(
            caffe_BN_298)
        caffe_BN_301 = self.caffe_BN_301(caffe_SpatialConvolution_300)
        caffe_BN_301 = self.caffe_ReLU_302(caffe_BN_301)
        caffe_SpatialConvolution_303 = self.caffe_SpatialConvolution_303(
            caffe_BN_301)
        caffe_BN_304 = self.caffe_BN_304(caffe_SpatialConvolution_303)
        caffe_BN_304 = self.caffe_ReLU_305(caffe_BN_304)
        caffe_SpatialConvolution_306 = self.caffe_SpatialConvolution_306(
            caffe_BN_304)
        caffe_Eltwise_307 = torch.add(
            caffe_SpatialConvolution_306,
            caffe_Eltwise_297)
        caffe_BN_308 = self.caffe_BN_308(caffe_Eltwise_307)
        caffe_BN_308 = self.caffe_ReLU_309(caffe_BN_308)
        caffe_SpatialConvolution_310 = self.caffe_SpatialConvolution_310(
            caffe_BN_308)
        caffe_BN_311 = self.caffe_BN_311(caffe_SpatialConvolution_310)
        caffe_BN_311 = self.caffe_ReLU_312(caffe_BN_311)
        caffe_SpatialConvolution_313 = self.caffe_SpatialConvolution_313(
            caffe_BN_311)
        caffe_BN_314 = self.caffe_BN_314(caffe_SpatialConvolution_313)
        caffe_BN_314 = self.caffe_ReLU_315(caffe_BN_314)
        caffe_SpatialConvolution_316 = self.caffe_SpatialConvolution_316(
            caffe_BN_314)
        caffe_Eltwise_317 = torch.add(
            caffe_SpatialConvolution_316,
            caffe_Eltwise_307)
        caffe_BN_318 = self.caffe_BN_318(caffe_Eltwise_317)
        caffe_BN_318 = self.caffe_ReLU_319(caffe_BN_318)
        caffe_SpatialConvolution_320 = self.caffe_SpatialConvolution_320(
            caffe_BN_318)
        caffe_BN_321 = self.caffe_BN_321(caffe_SpatialConvolution_320)
        caffe_BN_321 = self.caffe_ReLU_322(caffe_BN_321)
        caffe_SpatialConvolution_323 = self.caffe_SpatialConvolution_323(
            caffe_BN_321)
        caffe_BN_324 = self.caffe_BN_324(caffe_SpatialConvolution_323)
        caffe_BN_324 = self.caffe_ReLU_325(caffe_BN_324)
        caffe_SpatialConvolution_326 = self.caffe_SpatialConvolution_326(
            caffe_BN_324)
        caffe_Eltwise_327 = torch.add(
            caffe_SpatialConvolution_326,
            caffe_Eltwise_317)
        caffe_BN_328 = self.caffe_BN_328(caffe_Eltwise_327)
        caffe_BN_328 = self.caffe_ReLU_329(caffe_BN_328)
        caffe_SpatialConvolution_330 = self.caffe_SpatialConvolution_330(
            caffe_BN_328)
        caffe_BN_331 = self.caffe_BN_331(caffe_SpatialConvolution_330)
        caffe_BN_331 = self.caffe_ReLU_332(caffe_BN_331)
        caffe_SpatialConvolution_333 = self.caffe_SpatialConvolution_333(
            caffe_BN_331)
        caffe_BN_334 = self.caffe_BN_334(caffe_SpatialConvolution_333)
        caffe_BN_334 = self.caffe_ReLU_335(caffe_BN_334)
        caffe_SpatialConvolution_336 = self.caffe_SpatialConvolution_336(
            caffe_BN_334)
        caffe_Eltwise_337 = torch.add(
            caffe_SpatialConvolution_336,
            caffe_Eltwise_327)
        caffe_BN_338 = self.caffe_BN_338(caffe_Eltwise_337)
        caffe_BN_338 = self.caffe_ReLU_339(caffe_BN_338)
        caffe_SpatialConvolution_340 = self.caffe_SpatialConvolution_340(
            caffe_BN_338)
        caffe_BN_341 = self.caffe_BN_341(caffe_SpatialConvolution_340)
        caffe_BN_341 = self.caffe_ReLU_342(caffe_BN_341)
        caffe_SpatialConvolution_343 = self.caffe_SpatialConvolution_343(
            caffe_BN_341)
        caffe_BN_344 = self.caffe_BN_344(caffe_SpatialConvolution_343)
        caffe_BN_344 = self.caffe_ReLU_345(caffe_BN_344)
        caffe_SpatialConvolution_346 = self.caffe_SpatialConvolution_346(
            caffe_BN_344)
        caffe_Eltwise_347 = torch.add(
            caffe_SpatialConvolution_346,
            caffe_Eltwise_337)
        caffe_BN_348 = self.caffe_BN_348(caffe_Eltwise_347)
        caffe_BN_348 = self.caffe_ReLU_349(caffe_BN_348)
        caffe_SpatialConvolution_350 = self.caffe_SpatialConvolution_350(
            caffe_BN_348)
        caffe_BN_351 = self.caffe_BN_351(caffe_SpatialConvolution_350)
        caffe_BN_351 = self.caffe_ReLU_352(caffe_BN_351)
        caffe_SpatialConvolution_353 = self.caffe_SpatialConvolution_353(
            caffe_BN_351)
        caffe_BN_354 = self.caffe_BN_354(caffe_SpatialConvolution_353)
        caffe_BN_354 = self.caffe_ReLU_355(caffe_BN_354)
        caffe_SpatialConvolution_356 = self.caffe_SpatialConvolution_356(
            caffe_BN_354)
        caffe_Eltwise_357 = torch.add(
            caffe_SpatialConvolution_356,
            caffe_Eltwise_347)
        caffe_BN_358 = self.caffe_BN_358(caffe_Eltwise_357)
        caffe_BN_358 = self.caffe_ReLU_359(caffe_BN_358)
        caffe_SpatialConvolution_360 = self.caffe_SpatialConvolution_360(
            caffe_BN_358)
        caffe_BN_361 = self.caffe_BN_361(caffe_SpatialConvolution_360)
        caffe_BN_361 = self.caffe_ReLU_362(caffe_BN_361)
        caffe_SpatialConvolution_363 = self.caffe_SpatialConvolution_363(
            caffe_BN_361)
        caffe_BN_364 = self.caffe_BN_364(caffe_SpatialConvolution_363)
        caffe_BN_364 = self.caffe_ReLU_365(caffe_BN_364)
        caffe_SpatialConvolution_366 = self.caffe_SpatialConvolution_366(
            caffe_BN_364)
        caffe_Eltwise_367 = torch.add(
            caffe_SpatialConvolution_366,
            caffe_Eltwise_357)
        caffe_BN_368 = self.caffe_BN_368(caffe_Eltwise_367)
        caffe_BN_368 = self.caffe_ReLU_369(caffe_BN_368)
        caffe_SpatialConvolution_370 = self.caffe_SpatialConvolution_370(
            caffe_BN_368)
        caffe_BN_371 = self.caffe_BN_371(caffe_SpatialConvolution_370)
        caffe_BN_371 = self.caffe_ReLU_372(caffe_BN_371)
        caffe_SpatialConvolution_373 = self.caffe_SpatialConvolution_373(
            caffe_BN_371)
        caffe_BN_374 = self.caffe_BN_374(caffe_SpatialConvolution_373)
        caffe_BN_374 = self.caffe_ReLU_375(caffe_BN_374)
        caffe_SpatialConvolution_376 = self.caffe_SpatialConvolution_376(
            caffe_BN_374)
        caffe_Eltwise_377 = torch.add(
            caffe_SpatialConvolution_376,
            caffe_Eltwise_367)
        caffe_BN_378 = self.caffe_BN_378(caffe_Eltwise_377)
        caffe_BN_378 = self.caffe_ReLU_379(caffe_BN_378)
        caffe_SpatialConvolution_380 = self.caffe_SpatialConvolution_380(
            caffe_BN_378)
        caffe_BN_381 = self.caffe_BN_381(caffe_SpatialConvolution_380)
        caffe_BN_381 = self.caffe_ReLU_382(caffe_BN_381)
        caffe_SpatialConvolution_383 = self.caffe_SpatialConvolution_383(
            caffe_BN_381)
        caffe_BN_384 = self.caffe_BN_384(caffe_SpatialConvolution_383)
        caffe_BN_384 = self.caffe_ReLU_385(caffe_BN_384)
        caffe_SpatialConvolution_386 = self.caffe_SpatialConvolution_386(
            caffe_BN_384)
        caffe_Eltwise_387 = torch.add(
            caffe_SpatialConvolution_386,
            caffe_Eltwise_377)
        caffe_BN_388 = self.caffe_BN_388(caffe_Eltwise_387)
        caffe_BN_388 = self.caffe_ReLU_389(caffe_BN_388)
        caffe_SpatialConvolution_390 = self.caffe_SpatialConvolution_390(
            caffe_BN_388)
        caffe_BN_391 = self.caffe_BN_391(caffe_SpatialConvolution_390)
        caffe_BN_391 = self.caffe_ReLU_392(caffe_BN_391)
        caffe_SpatialConvolution_393 = self.caffe_SpatialConvolution_393(
            caffe_BN_391)
        caffe_BN_394 = self.caffe_BN_394(caffe_SpatialConvolution_393)
        caffe_BN_394 = self.caffe_ReLU_395(caffe_BN_394)
        caffe_SpatialConvolution_396 = self.caffe_SpatialConvolution_396(
            caffe_BN_394)
        caffe_Eltwise_397 = torch.add(
            caffe_SpatialConvolution_396,
            caffe_Eltwise_387)
        caffe_BN_398 = self.caffe_BN_398(caffe_Eltwise_397)
        caffe_BN_398 = self.caffe_ReLU_399(caffe_BN_398)
        caffe_SpatialConvolution_400 = self.caffe_SpatialConvolution_400(
            caffe_BN_398)
        caffe_BN_401 = self.caffe_BN_401(caffe_SpatialConvolution_400)
        caffe_BN_401 = self.caffe_ReLU_402(caffe_BN_401)
        caffe_SpatialConvolution_403 = self.caffe_SpatialConvolution_403(
            caffe_BN_401)
        caffe_BN_404 = self.caffe_BN_404(caffe_SpatialConvolution_403)
        caffe_BN_404 = self.caffe_ReLU_405(caffe_BN_404)
        caffe_SpatialConvolution_406 = self.caffe_SpatialConvolution_406(
            caffe_BN_404)
        caffe_Eltwise_407 = torch.add(
            caffe_SpatialConvolution_406,
            caffe_Eltwise_397)
        caffe_BN_408 = self.caffe_BN_408(caffe_Eltwise_407)
        caffe_BN_408 = self.caffe_ReLU_409(caffe_BN_408)
        caffe_SpatialConvolution_410 = self.caffe_SpatialConvolution_410(
            caffe_BN_408)
        caffe_BN_411 = self.caffe_BN_411(caffe_SpatialConvolution_410)
        caffe_BN_411 = self.caffe_ReLU_412(caffe_BN_411)
        caffe_SpatialConvolution_413 = self.caffe_SpatialConvolution_413(
            caffe_BN_411)
        caffe_BN_414 = self.caffe_BN_414(caffe_SpatialConvolution_413)
        caffe_BN_414 = self.caffe_ReLU_415(caffe_BN_414)
        caffe_SpatialConvolution_416 = self.caffe_SpatialConvolution_416(
            caffe_BN_414)
        caffe_Eltwise_417 = torch.add(
            caffe_SpatialConvolution_416,
            caffe_Eltwise_407)
        caffe_BN_418 = self.caffe_BN_418(caffe_Eltwise_417)
        caffe_BN_418 = self.caffe_ReLU_419(caffe_BN_418)
        caffe_SpatialConvolution_420 = self.caffe_SpatialConvolution_420(
            caffe_BN_418)
        caffe_BN_421 = self.caffe_BN_421(caffe_SpatialConvolution_420)
        caffe_BN_421 = self.caffe_ReLU_422(caffe_BN_421)
        caffe_SpatialConvolution_423 = self.caffe_SpatialConvolution_423(
            caffe_BN_421)
        caffe_BN_424 = self.caffe_BN_424(caffe_SpatialConvolution_423)
        caffe_BN_424 = self.caffe_ReLU_425(caffe_BN_424)
        caffe_SpatialConvolution_426 = self.caffe_SpatialConvolution_426(
            caffe_BN_424)
        caffe_Eltwise_427 = torch.add(
            caffe_SpatialConvolution_426,
            caffe_Eltwise_417)
        caffe_BN_428 = self.caffe_BN_428(caffe_Eltwise_427)
        caffe_BN_428 = self.caffe_ReLU_429(caffe_BN_428)
        caffe_SpatialConvolution_430 = self.caffe_SpatialConvolution_430(
            caffe_BN_428)
        caffe_BN_431 = self.caffe_BN_431(caffe_SpatialConvolution_430)
        caffe_BN_431 = self.caffe_ReLU_432(caffe_BN_431)
        caffe_SpatialConvolution_433 = self.caffe_SpatialConvolution_433(
            caffe_BN_431)
        caffe_BN_434 = self.caffe_BN_434(caffe_SpatialConvolution_433)
        caffe_BN_434 = self.caffe_ReLU_435(caffe_BN_434)
        caffe_SpatialConvolution_436 = self.caffe_SpatialConvolution_436(
            caffe_BN_434)
        caffe_Eltwise_437 = torch.add(
            caffe_SpatialConvolution_436,
            caffe_Eltwise_427)
        caffe_BN_438 = self.caffe_BN_438(caffe_Eltwise_437)
        caffe_BN_438 = self.caffe_ReLU_439(caffe_BN_438)
        caffe_SpatialConvolution_440 = self.caffe_SpatialConvolution_440(
            caffe_BN_438)
        caffe_BN_441 = self.caffe_BN_441(caffe_SpatialConvolution_440)
        caffe_BN_441 = self.caffe_ReLU_442(caffe_BN_441)
        caffe_SpatialConvolution_443 = self.caffe_SpatialConvolution_443(
            caffe_BN_441)
        caffe_BN_444 = self.caffe_BN_444(caffe_SpatialConvolution_443)
        caffe_BN_444 = self.caffe_ReLU_445(caffe_BN_444)
        caffe_SpatialConvolution_446 = self.caffe_SpatialConvolution_446(
            caffe_BN_444)
        caffe_Eltwise_447 = torch.add(
            caffe_SpatialConvolution_446,
            caffe_Eltwise_437)
        caffe_BN_448 = self.caffe_BN_448(caffe_Eltwise_447)
        caffe_BN_448 = self.caffe_ReLU_449(caffe_BN_448)
        caffe_SpatialConvolution_450 = self.caffe_SpatialConvolution_450(
            caffe_BN_448)
        caffe_BN_451 = self.caffe_BN_451(caffe_SpatialConvolution_450)
        caffe_BN_451 = self.caffe_ReLU_452(caffe_BN_451)
        caffe_SpatialConvolution_453 = self.caffe_SpatialConvolution_453(
            caffe_BN_451)
        caffe_BN_454 = self.caffe_BN_454(caffe_SpatialConvolution_453)
        caffe_BN_454 = self.caffe_ReLU_455(caffe_BN_454)
        caffe_SpatialConvolution_456 = self.caffe_SpatialConvolution_456(
            caffe_BN_454)
        caffe_Eltwise_457 = torch.add(
            caffe_SpatialConvolution_456,
            caffe_Eltwise_447)
        caffe_BN_458 = self.caffe_BN_458(caffe_Eltwise_457)
        caffe_BN_458 = self.caffe_ReLU_459(caffe_BN_458)
        caffe_SpatialConvolution_460 = self.caffe_SpatialConvolution_460(
            caffe_BN_458)
        caffe_BN_461 = self.caffe_BN_461(caffe_SpatialConvolution_460)
        caffe_BN_461 = self.caffe_ReLU_462(caffe_BN_461)
        caffe_SpatialConvolution_463 = self.caffe_SpatialConvolution_463(
            caffe_BN_461)
        caffe_BN_464 = self.caffe_BN_464(caffe_SpatialConvolution_463)
        caffe_BN_464 = self.caffe_ReLU_465(caffe_BN_464)
        caffe_SpatialConvolution_466 = self.caffe_SpatialConvolution_466(
            caffe_BN_464)
        caffe_Eltwise_467 = torch.add(
            caffe_SpatialConvolution_466,
            caffe_Eltwise_457)
        caffe_BN_468 = self.caffe_BN_468(caffe_Eltwise_467)
        caffe_BN_468 = self.caffe_ReLU_469(caffe_BN_468)
        caffe_SpatialConvolution_470 = self.caffe_SpatialConvolution_470(
            caffe_BN_468)
        caffe_BN_471 = self.caffe_BN_471(caffe_SpatialConvolution_470)
        caffe_BN_471 = self.caffe_ReLU_472(caffe_BN_471)
        caffe_SpatialConvolution_473 = self.caffe_SpatialConvolution_473(
            caffe_BN_471)
        caffe_BN_474 = self.caffe_BN_474(caffe_SpatialConvolution_473)
        caffe_BN_474 = self.caffe_ReLU_475(caffe_BN_474)
        caffe_SpatialConvolution_476 = self.caffe_SpatialConvolution_476(
            caffe_BN_474)
        caffe_Eltwise_477 = torch.add(
            caffe_SpatialConvolution_476,
            caffe_Eltwise_467)
        caffe_BN_478 = self.caffe_BN_478(caffe_Eltwise_477)
        caffe_BN_478 = self.caffe_ReLU_479(caffe_BN_478)
        caffe_SpatialConvolution_480 = self.caffe_SpatialConvolution_480(
            caffe_BN_478)
        caffe_BN_481 = self.caffe_BN_481(caffe_SpatialConvolution_480)
        caffe_BN_481 = self.caffe_ReLU_482(caffe_BN_481)
        caffe_SpatialConvolution_483 = self.caffe_SpatialConvolution_483(
            caffe_BN_481)
        caffe_BN_484 = self.caffe_BN_484(caffe_SpatialConvolution_483)
        caffe_BN_484 = self.caffe_ReLU_485(caffe_BN_484)
        caffe_SpatialConvolution_486 = self.caffe_SpatialConvolution_486(
            caffe_BN_484)
        caffe_Eltwise_487 = torch.add(
            caffe_SpatialConvolution_486,
            caffe_Eltwise_477)
        caffe_BN_488 = self.caffe_BN_488(caffe_Eltwise_487)
        caffe_BN_488 = self.caffe_ReLU_489(caffe_BN_488)
        caffe_SpatialConvolution_490 = self.caffe_SpatialConvolution_490(
            caffe_BN_488)
        caffe_BN_491 = self.caffe_BN_491(caffe_SpatialConvolution_490)
        caffe_BN_491 = self.caffe_ReLU_492(caffe_BN_491)
        caffe_SpatialConvolution_493 = self.caffe_SpatialConvolution_493(
            caffe_BN_491)
        caffe_BN_494 = self.caffe_BN_494(caffe_SpatialConvolution_493)
        caffe_BN_494 = self.caffe_ReLU_495(caffe_BN_494)
        caffe_SpatialConvolution_496 = self.caffe_SpatialConvolution_496(
            caffe_BN_494)
        caffe_Eltwise_497 = torch.add(
            caffe_SpatialConvolution_496,
            caffe_Eltwise_487)
        caffe_BN_498 = self.caffe_BN_498(caffe_Eltwise_497)
        caffe_BN_498 = self.caffe_ReLU_499(caffe_BN_498)
        caffe_SpatialConvolution_500 = self.caffe_SpatialConvolution_500(
            caffe_BN_498)
        caffe_BN_501 = self.caffe_BN_501(caffe_SpatialConvolution_500)
        caffe_BN_501 = self.caffe_ReLU_502(caffe_BN_501)
        caffe_SpatialConvolution_503 = self.caffe_SpatialConvolution_503(
            caffe_BN_501)
        caffe_BN_504 = self.caffe_BN_504(caffe_SpatialConvolution_503)
        caffe_BN_504 = self.caffe_ReLU_505(caffe_BN_504)
        caffe_SpatialConvolution_506 = self.caffe_SpatialConvolution_506(
            caffe_BN_504)
        caffe_Eltwise_507 = torch.add(
            caffe_SpatialConvolution_506,
            caffe_Eltwise_497)
        caffe_BN_508 = self.caffe_BN_508(caffe_Eltwise_507)
        caffe_BN_508 = self.caffe_ReLU_509(caffe_BN_508)
        caffe_SpatialConvolution_510 = self.caffe_SpatialConvolution_510(
            caffe_BN_508)
        caffe_BN_511 = self.caffe_BN_511(caffe_SpatialConvolution_510)
        caffe_BN_511 = self.caffe_ReLU_512(caffe_BN_511)
        caffe_SpatialConvolution_513 = self.caffe_SpatialConvolution_513(
            caffe_BN_511)
        caffe_BN_514 = self.caffe_BN_514(caffe_SpatialConvolution_513)
        caffe_BN_514 = self.caffe_ReLU_515(caffe_BN_514)
        caffe_SpatialConvolution_516 = self.caffe_SpatialConvolution_516(
            caffe_BN_514)
        caffe_Eltwise_517 = torch.add(
            caffe_SpatialConvolution_516,
            caffe_Eltwise_507)
        caffe_BN_518 = self.caffe_BN_518(caffe_Eltwise_517)
        caffe_BN_518 = self.caffe_ReLU_519(caffe_BN_518)
        caffe_SpatialConvolution_520 = self.caffe_SpatialConvolution_520(
            caffe_BN_518)
        caffe_BN_521 = self.caffe_BN_521(caffe_SpatialConvolution_520)
        caffe_BN_521 = self.caffe_ReLU_522(caffe_BN_521)
        caffe_SpatialConvolution_523 = self.caffe_SpatialConvolution_523(
            caffe_BN_521)
        caffe_BN_524 = self.caffe_BN_524(caffe_SpatialConvolution_523)
        caffe_BN_524 = self.caffe_ReLU_525(caffe_BN_524)
        caffe_SpatialConvolution_526 = self.caffe_SpatialConvolution_526(
            caffe_BN_524)
        caffe_Eltwise_527 = torch.add(
            caffe_SpatialConvolution_526,
            caffe_Eltwise_517)
        caffe_BN_528 = self.caffe_BN_528(caffe_Eltwise_527)
        caffe_BN_528 = self.caffe_ReLU_529(caffe_BN_528)
        caffe_SpatialConvolution_530 = self.caffe_SpatialConvolution_530(
            caffe_BN_528)
        caffe_BN_531 = self.caffe_BN_531(caffe_SpatialConvolution_530)
        caffe_BN_531 = self.caffe_ReLU_532(caffe_BN_531)
        caffe_SpatialConvolution_533 = self.caffe_SpatialConvolution_533(
            caffe_BN_531)
        caffe_BN_534 = self.caffe_BN_534(caffe_SpatialConvolution_533)
        caffe_BN_534 = self.caffe_ReLU_535(caffe_BN_534)
        caffe_SpatialConvolution_536 = self.caffe_SpatialConvolution_536(
            caffe_BN_534)
        caffe_Eltwise_537 = torch.add(
            caffe_SpatialConvolution_536,
            caffe_Eltwise_527)
        caffe_BN_538 = self.caffe_BN_538(caffe_Eltwise_537)
        caffe_BN_538 = self.caffe_ReLU_539(caffe_BN_538)
        caffe_SpatialConvolution_540 = self.caffe_SpatialConvolution_540(
            caffe_BN_538)
        caffe_BN_541 = self.caffe_BN_541(caffe_SpatialConvolution_540)
        caffe_BN_541 = self.caffe_ReLU_542(caffe_BN_541)
        caffe_SpatialConvolution_543 = self.caffe_SpatialConvolution_543(
            caffe_BN_541)
        caffe_BN_544 = self.caffe_BN_544(caffe_SpatialConvolution_543)
        caffe_BN_544 = self.caffe_ReLU_545(caffe_BN_544)
        caffe_SpatialConvolution_546 = self.caffe_SpatialConvolution_546(
            caffe_BN_544)
        caffe_Eltwise_547 = torch.add(
            caffe_SpatialConvolution_546,
            caffe_Eltwise_537)
        caffe_BN_548 = self.caffe_BN_548(caffe_Eltwise_547)
        caffe_BN_548 = self.caffe_ReLU_549(caffe_BN_548)
        caffe_SpatialConvolution_550 = self.caffe_SpatialConvolution_550(
            caffe_BN_548)
        caffe_BN_551 = self.caffe_BN_551(caffe_SpatialConvolution_550)
        caffe_BN_551 = self.caffe_ReLU_552(caffe_BN_551)
        caffe_SpatialConvolution_553 = self.caffe_SpatialConvolution_553(
            caffe_BN_551)
        caffe_BN_554 = self.caffe_BN_554(caffe_SpatialConvolution_553)
        caffe_BN_554 = self.caffe_ReLU_555(caffe_BN_554)
        caffe_SpatialConvolution_556 = self.caffe_SpatialConvolution_556(
            caffe_BN_554)
        caffe_Eltwise_557 = torch.add(
            caffe_SpatialConvolution_556,
            caffe_Eltwise_547)
        caffe_BN_558 = self.caffe_BN_558(caffe_Eltwise_557)
        caffe_BN_558 = self.caffe_ReLU_559(caffe_BN_558)
        caffe_SpatialConvolution_560 = self.caffe_SpatialConvolution_560(
            caffe_BN_558)
        caffe_BN_561 = self.caffe_BN_561(caffe_SpatialConvolution_560)
        caffe_BN_561 = self.caffe_ReLU_562(caffe_BN_561)
        caffe_SpatialConvolution_563 = self.caffe_SpatialConvolution_563(
            caffe_BN_561)
        caffe_BN_564 = self.caffe_BN_564(caffe_SpatialConvolution_563)
        caffe_BN_564 = self.caffe_ReLU_565(caffe_BN_564)
        caffe_SpatialConvolution_566 = self.caffe_SpatialConvolution_566(
            caffe_BN_564)
        caffe_Eltwise_567 = torch.add(
            caffe_SpatialConvolution_566,
            caffe_Eltwise_557)
        caffe_BN_568 = self.caffe_BN_568(caffe_Eltwise_567)
        caffe_BN_568 = self.caffe_ReLU_569(caffe_BN_568)
        caffe_SpatialConvolution_570 = self.caffe_SpatialConvolution_570(
            caffe_BN_568)
        caffe_BN_571 = self.caffe_BN_571(caffe_SpatialConvolution_570)
        caffe_BN_571 = self.caffe_ReLU_572(caffe_BN_571)
        caffe_SpatialConvolution_573 = self.caffe_SpatialConvolution_573(
            caffe_BN_571)
        caffe_BN_574 = self.caffe_BN_574(caffe_SpatialConvolution_573)
        caffe_BN_574 = self.caffe_ReLU_575(caffe_BN_574)
        caffe_SpatialConvolution_576 = self.caffe_SpatialConvolution_576(
            caffe_BN_574)
        caffe_Eltwise_577 = torch.add(
            caffe_SpatialConvolution_576,
            caffe_Eltwise_567)
        caffe_BN_578 = self.caffe_BN_578(caffe_Eltwise_577)
        caffe_BN_578 = self.caffe_ReLU_579(caffe_BN_578)
        caffe_SpatialConvolution_580 = self.caffe_SpatialConvolution_580(
            caffe_BN_578)
        caffe_BN_581 = self.caffe_BN_581(caffe_SpatialConvolution_580)
        caffe_BN_581 = self.caffe_ReLU_582(caffe_BN_581)
        caffe_SpatialConvolution_583 = self.caffe_SpatialConvolution_583(
            caffe_BN_581)
        caffe_BN_584 = self.caffe_BN_584(caffe_SpatialConvolution_583)
        caffe_BN_584 = self.caffe_ReLU_585(caffe_BN_584)
        caffe_SpatialConvolution_586 = self.caffe_SpatialConvolution_586(
            caffe_BN_584)
        caffe_Eltwise_587 = torch.add(
            caffe_SpatialConvolution_586,
            caffe_Eltwise_577)
        caffe_BN_588 = self.caffe_BN_588(caffe_Eltwise_587)
        caffe_BN_588 = self.caffe_ReLU_589(caffe_BN_588)
        caffe_SpatialConvolution_590 = self.caffe_SpatialConvolution_590(
            caffe_BN_588)
        caffe_BN_591 = self.caffe_BN_591(caffe_SpatialConvolution_590)
        caffe_BN_591 = self.caffe_ReLU_592(caffe_BN_591)
        caffe_SpatialConvolution_593 = self.caffe_SpatialConvolution_593(
            caffe_BN_591)
        caffe_BN_594 = self.caffe_BN_594(caffe_SpatialConvolution_593)
        caffe_BN_594 = self.caffe_ReLU_595(caffe_BN_594)
        caffe_SpatialConvolution_596 = self.caffe_SpatialConvolution_596(
            caffe_BN_594)
        caffe_Eltwise_597 = torch.add(
            caffe_SpatialConvolution_596,
            caffe_Eltwise_587)
        caffe_BN_598 = self.caffe_BN_598(caffe_Eltwise_597)
        caffe_BN_598 = self.caffe_ReLU_599(caffe_BN_598)
        caffe_SpatialConvolution_600 = self.caffe_SpatialConvolution_600(
            caffe_BN_598)
        caffe_BN_601 = self.caffe_BN_601(caffe_SpatialConvolution_600)
        caffe_BN_601 = self.caffe_ReLU_602(caffe_BN_601)
        caffe_SpatialConvolution_603 = self.caffe_SpatialConvolution_603(
            caffe_BN_601)
        caffe_BN_604 = self.caffe_BN_604(caffe_SpatialConvolution_603)
        caffe_BN_604 = self.caffe_ReLU_605(caffe_BN_604)
        caffe_SpatialConvolution_606 = self.caffe_SpatialConvolution_606(
            caffe_BN_604)
        caffe_Eltwise_607 = torch.add(
            caffe_SpatialConvolution_606,
            caffe_Eltwise_597)
        caffe_BN_608 = self.caffe_BN_608(caffe_Eltwise_607)
        caffe_BN_608 = self.caffe_ReLU_609(caffe_BN_608)
        caffe_SpatialConvolution_610 = self.caffe_SpatialConvolution_610(
            caffe_BN_608)
        caffe_BN_611 = self.caffe_BN_611(caffe_SpatialConvolution_610)
        caffe_BN_611 = self.caffe_ReLU_612(caffe_BN_611)
        caffe_SpatialConvolution_613 = self.caffe_SpatialConvolution_613(
            caffe_BN_611)
        caffe_BN_614 = self.caffe_BN_614(caffe_SpatialConvolution_613)
        caffe_BN_614 = self.caffe_ReLU_615(caffe_BN_614)
        caffe_SpatialConvolution_616 = self.caffe_SpatialConvolution_616(
            caffe_BN_614)
        caffe_Eltwise_617 = torch.add(
            caffe_SpatialConvolution_616,
            caffe_Eltwise_607)
        caffe_BN_618 = self.caffe_BN_618(caffe_Eltwise_617)
        caffe_BN_618 = self.caffe_ReLU_619(caffe_BN_618)
        caffe_SpatialConvolution_620 = self.caffe_SpatialConvolution_620(
            caffe_BN_618)
        caffe_BN_621 = self.caffe_BN_621(caffe_SpatialConvolution_620)
        caffe_BN_621 = self.caffe_ReLU_622(caffe_BN_621)
        caffe_SpatialConvolution_623 = self.caffe_SpatialConvolution_623(
            caffe_BN_621)
        caffe_BN_624 = self.caffe_BN_624(caffe_SpatialConvolution_623)
        caffe_BN_624 = self.caffe_ReLU_625(caffe_BN_624)
        caffe_SpatialConvolution_626 = self.caffe_SpatialConvolution_626(
            caffe_BN_624)
        caffe_Eltwise_627 = torch.add(
            caffe_SpatialConvolution_626,
            caffe_Eltwise_617)
        caffe_BN_628 = self.caffe_BN_628(caffe_Eltwise_627)
        caffe_BN_628 = self.caffe_ReLU_629(caffe_BN_628)
        caffe_SpatialConvolution_630 = self.caffe_SpatialConvolution_630(
            caffe_BN_628)
        caffe_BN_631 = self.caffe_BN_631(caffe_SpatialConvolution_630)
        caffe_BN_631 = self.caffe_ReLU_632(caffe_BN_631)
        caffe_SpatialConvolution_633 = self.caffe_SpatialConvolution_633(
            caffe_BN_631)
        caffe_BN_634 = self.caffe_BN_634(caffe_SpatialConvolution_633)
        caffe_BN_634 = self.caffe_ReLU_635(caffe_BN_634)
        caffe_SpatialConvolution_636 = self.caffe_SpatialConvolution_636(
            caffe_BN_634)
        caffe_Eltwise_637 = torch.add(
            caffe_SpatialConvolution_636,
            caffe_Eltwise_627)
        caffe_BN_638 = self.caffe_BN_638(caffe_Eltwise_637)
        caffe_BN_638 = self.caffe_ReLU_639(caffe_BN_638)
        caffe_SpatialConvolution_640 = self.caffe_SpatialConvolution_640(
            caffe_BN_638)
        caffe_BN_641 = self.caffe_BN_641(caffe_SpatialConvolution_640)
        caffe_BN_641 = self.caffe_ReLU_642(caffe_BN_641)
        caffe_SpatialConvolution_643 = self.caffe_SpatialConvolution_643(
            caffe_BN_641)
        caffe_BN_644 = self.caffe_BN_644(caffe_SpatialConvolution_643)
        caffe_BN_644 = self.caffe_ReLU_645(caffe_BN_644)
        caffe_SpatialConvolution_646 = self.caffe_SpatialConvolution_646(
            caffe_BN_644)
        caffe_SpatialConvolution_647 = self.caffe_SpatialConvolution_647(
            caffe_Eltwise_637)
        caffe_BN_648 = self.caffe_BN_648(caffe_SpatialConvolution_647)
        caffe_Eltwise_649 = torch.add(
            caffe_SpatialConvolution_646, caffe_BN_648)
        caffe_BN_650 = self.caffe_BN_650(caffe_Eltwise_649)
        caffe_BN_650 = self.caffe_ReLU_651(caffe_BN_650)
        caffe_SpatialConvolution_652 = self.caffe_SpatialConvolution_652(
            caffe_BN_650)
        caffe_BN_653 = self.caffe_BN_653(caffe_SpatialConvolution_652)
        caffe_BN_653 = self.caffe_ReLU_654(caffe_BN_653)
        caffe_SpatialConvolution_655 = self.caffe_SpatialConvolution_655(
            caffe_BN_653)
        caffe_BN_656 = self.caffe_BN_656(caffe_SpatialConvolution_655)
        caffe_BN_656 = self.caffe_ReLU_657(caffe_BN_656)
        caffe_SpatialConvolution_658 = self.caffe_SpatialConvolution_658(
            caffe_BN_656)
        caffe_Eltwise_659 = torch.add(
            caffe_SpatialConvolution_658,
            caffe_Eltwise_649)
        caffe_BN_660 = self.caffe_BN_660(caffe_Eltwise_659)
        caffe_BN_660 = self.caffe_ReLU_661(caffe_BN_660)
        caffe_SpatialConvolution_662 = self.caffe_SpatialConvolution_662(
            caffe_BN_660)
        caffe_BN_663 = self.caffe_BN_663(caffe_SpatialConvolution_662)
        caffe_BN_663 = self.caffe_ReLU_664(caffe_BN_663)
        caffe_SpatialConvolution_665 = self.caffe_SpatialConvolution_665(
            caffe_BN_663)
        caffe_BN_666 = self.caffe_BN_666(caffe_SpatialConvolution_665)
        caffe_BN_666 = self.caffe_ReLU_667(caffe_BN_666)
        caffe_SpatialConvolution_668 = self.caffe_SpatialConvolution_668(
            caffe_BN_666)
        caffe_Eltwise_669 = torch.add(
            caffe_SpatialConvolution_668,
            caffe_Eltwise_659)
        caffe_BN_670 = self.caffe_BN_670(caffe_Eltwise_669)
        caffe_BN_670 = self.caffe_ReLU_671(caffe_BN_670)
        # TODO(fixme) average pooling's result is
        # difference with caffe's result.
        caffe_Pooling_672 = F.avg_pool2d(
            caffe_BN_670,
            kernel_size=(caffe_BN_670.shape[2], caffe_BN_670.shape[3]),
            padding=0)
        caffe_Flatten_673 = self.caffe_Flatten_673(caffe_Pooling_672)
        caffe_Flatten_673 = self.caffe_Dropout_674(caffe_Flatten_673)
        return caffe_Flatten_673
        # fc_action = self.caffe_InnerProduct_675(caffe_Flatten_673)
        # return fc_action
