import os

import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F

from fastflownet.correlation_package.correlation import Correlation
from fastflownet.data import get_pretrained_model


def centralize(img1, img2):
    b, c, h, w = img1.shape
    rgb_mean = torch.cat([img1, img2], dim=2).view(b, c, -1).mean(2).view(b, c, 1, 1)
    return img1 - rgb_mean, img2 - rgb_mean, rgb_mean


def convrelu(in_channels, out_channels, kernel_size=3, stride=1, padding=1, dilation=1, groups=1, bias=True):
    return nn.Sequential(
        nn.Conv2d(in_channels, out_channels, kernel_size, stride, padding, dilation, groups, bias=bias), 
        nn.LeakyReLU(0.1, inplace=True)
    )


def deconv(in_planes, out_planes, kernel_size=4, stride=2, padding=1):
    return nn.ConvTranspose2d(in_planes, out_planes, kernel_size, stride, padding, bias=True)


class Decoder(nn.Module):
    def __init__(self, in_channels, groups):
        super(Decoder, self).__init__()
        self.in_channels = in_channels
        self.groups = groups
        self.conv1 = convrelu(in_channels, 96, 3, 1)
        self.conv2 = convrelu(96, 96, 3, 1, groups=groups)
        self.conv3 = convrelu(96, 96, 3, 1, groups=groups)
        self.conv4 = convrelu(96, 96, 3, 1, groups=groups)
        self.conv5 = convrelu(96, 64, 3, 1)
        self.conv6 = convrelu(64, 32, 3, 1)
        self.conv7 = nn.Conv2d(32, 2, 3, 1, 1)


    def channel_shuffle(self, x, groups):
        b, c, h, w = x.size()
        channels_per_group = c // groups
        x = x.view(b, groups, channels_per_group, h, w)
        x = x.transpose(1, 2).contiguous()
        x = x.view(b, -1, h, w)
        return x


    def forward(self, x):
        if self.groups == 1:
            out = self.conv7(self.conv6(self.conv5(self.conv4(self.conv3(self.conv2(self.conv1(x)))))))
        else:
            out = self.conv1(x)
            out = self.channel_shuffle(self.conv2(out), self.groups)
            out = self.channel_shuffle(self.conv3(out), self.groups)
            out = self.channel_shuffle(self.conv4(out), self.groups)
            out = self.conv7(self.conv6(self.conv5(out)))
        return out


class FastFlowNet(nn.Module):

    def __init__(self, groups=3, pretrained_model=None):
        super(FastFlowNet, self).__init__()
        self.groups = groups
        self.pconv1_1 = convrelu(3, 16, 3, 2)
        self.pconv1_2 = convrelu(16, 16, 3, 1)
        self.pconv2_1 = convrelu(16, 32, 3, 2)
        self.pconv2_2 = convrelu(32, 32, 3, 1)
        self.pconv2_3 = convrelu(32, 32, 3, 1)
        self.pconv3_1 = convrelu(32, 64, 3, 2)
        self.pconv3_2 = convrelu(64, 64, 3, 1)
        self.pconv3_3 = convrelu(64, 64, 3, 1)

        self.corr = Correlation(pad_size=4, kernel_size=1, max_displacement=4, stride1=1, stride2=1, corr_multiply=1)
        self.index = torch.tensor([0, 2, 4, 6, 8, 
                10, 12, 14, 16, 
                18, 20, 21, 22, 23, 24, 26, 
                28, 29, 30, 31, 32, 33, 34, 
                36, 38, 39, 40, 41, 42, 44, 
                46, 47, 48, 49, 50, 51, 52, 
                54, 56, 57, 58, 59, 60, 62, 
                64, 66, 68, 70, 
                72, 74, 76, 78, 80])

        self.rconv2 = convrelu(32, 32, 3, 1)
        self.rconv3 = convrelu(64, 32, 3, 1)
        self.rconv4 = convrelu(64, 32, 3, 1)
        self.rconv5 = convrelu(64, 32, 3, 1)
        self.rconv6 = convrelu(64, 32, 3, 1)

        self.up3 = deconv(2, 2)
        self.up4 = deconv(2, 2)
        self.up5 = deconv(2, 2)
        self.up6 = deconv(2, 2)

        self.decoder2 = Decoder(87, groups)
        self.decoder3 = Decoder(87, groups)
        self.decoder4 = Decoder(87, groups)
        self.decoder5 = Decoder(87, groups)
        self.decoder6 = Decoder(87, groups)
        
        for m in self.modules():
            if isinstance(m, nn.Conv2d) or isinstance(m, nn.ConvTranspose2d):
                nn.init.kaiming_normal_(m.weight)
                if m.bias is not None:
                    nn.init.zeros_(m.bias)

        if pretrained_model is None:
            state_dict = torch.load(get_pretrained_model(),
                                    map_location='cpu')
            self.load_state_dict(state_dict)

    def warp(self, x, flo):
        B, C, H, W = x.size()
        xx = torch.arange(0, W).view(1, -1).repeat(H, 1)
        yy = torch.arange(0, H).view(-1, 1).repeat(1, W)
        xx = xx.view(1, 1, H, W).repeat(B, 1, 1, 1)
        yy = yy.view(1, 1, H, W).repeat(B, 1, 1, 1)
        grid = torch.cat([xx, yy], 1).to(x)
        vgrid = grid + flo
        vgrid[:, 0, :, :] = 2.0 * vgrid[:, 0, :, :] / max(W-1, 1) - 1.0
        vgrid[:, 1, :, :] = 2.0 * vgrid[:, 1, :, :] / max(H-1, 1) - 1.0
        vgrid = vgrid.permute(0, 2, 3, 1)        
        output = F.grid_sample(x, vgrid, mode='bilinear')
        return output


    def forward(self, x):
        img1 = x[:, :3, :, :]
        img2 = x[:, 3:6, :, :]
        f11 = self.pconv1_2(self.pconv1_1(img1))
        f21 = self.pconv1_2(self.pconv1_1(img2))
        f12 = self.pconv2_3(self.pconv2_2(self.pconv2_1(f11)))
        f22 = self.pconv2_3(self.pconv2_2(self.pconv2_1(f21)))
        f13 = self.pconv3_3(self.pconv3_2(self.pconv3_1(f12)))
        f23 = self.pconv3_3(self.pconv3_2(self.pconv3_1(f22)))
        f14 = F.avg_pool2d(f13, kernel_size=(2, 2), stride=(2, 2))
        f24 = F.avg_pool2d(f23, kernel_size=(2, 2), stride=(2, 2))
        f15 = F.avg_pool2d(f14, kernel_size=(2, 2), stride=(2, 2))
        f25 = F.avg_pool2d(f24, kernel_size=(2, 2), stride=(2, 2))
        f16 = F.avg_pool2d(f15, kernel_size=(2, 2), stride=(2, 2))
        f26 = F.avg_pool2d(f25, kernel_size=(2, 2), stride=(2, 2))

        flow7_up = torch.zeros(f16.size(0), 2, f16.size(2), f16.size(3)).to(f15)
        cv6 = torch.index_select(self.corr(f16, f26), dim=1, index=self.index.to(f16).long())
        r16 = self.rconv6(f16)
        cat6 = torch.cat([cv6, r16, flow7_up], 1)
        flow6 = self.decoder6(cat6)

        flow6_up = self.up6(flow6)
        f25_w = self.warp(f25, flow6_up*0.625)
        cv5 = torch.index_select(self.corr(f15, f25_w), dim=1, index=self.index.to(f15).long())
        r15 = self.rconv5(f15)
        cat5 = torch.cat([cv5, r15, flow6_up], 1)
        flow5 = self.decoder5(cat5) + flow6_up

        flow5_up = self.up5(flow5)
        f24_w = self.warp(f24, flow5_up*1.25)
        cv4 = torch.index_select(self.corr(f14, f24_w), dim=1, index=self.index.to(f14).long())
        r14 = self.rconv4(f14)
        cat4 = torch.cat([cv4, r14, flow5_up], 1)
        flow4 = self.decoder4(cat4) + flow5_up

        flow4_up = self.up4(flow4)
        f23_w = self.warp(f23, flow4_up*2.5)
        cv3 = torch.index_select(self.corr(f13, f23_w), dim=1, index=self.index.to(f13).long())
        r13 = self.rconv3(f13)
        cat3 = torch.cat([cv3, r13, flow4_up], 1)
        flow3 = self.decoder3(cat3) + flow4_up

        flow3_up = self.up3(flow3)
        f22_w = self.warp(f22, flow3_up*5.0)
        cv2 = torch.index_select(self.corr(f12, f22_w), dim=1, index=self.index.to(f12).long())
        r12 = self.rconv2(f12)
        cat2 = torch.cat([cv2, r12, flow3_up], 1)
        flow2 = self.decoder2(cat2) + flow3_up
        
        if self.training:
            return flow2, flow3, flow4, flow5, flow6
        else:
            return flow2

    def calculate_flow(self, prev_img, cur_img,
                       div_flow=20.0, div_size=64):
        """Calculate optical flow from two image.

        Parameters
        ----------
        prev_img : numpy.ndarray
            bgr image.
        cur_img : numpy.ndarray
            bgr image.
        """
        img1 = torch.from_numpy(
            prev_img).float().permute(2, 0, 1).unsqueeze(0) / 255.0
        img2 = torch.from_numpy(
            cur_img).float().permute(2, 0, 1).unsqueeze(0) / 255.0
        img1, img2, _ = centralize(img1, img2)

        height, width = img1.shape[-2:]
        orig_size = (int(height), int(width))

        if height % div_size != 0 or width % div_size != 0:
            input_size = (
                int(div_size * np.ceil(height / div_size)),
                int(div_size * np.ceil(width / div_size))
            )
            img1 = F.interpolate(
                img1, size=input_size, mode='bilinear', align_corners=False)
            img2 = F.interpolate(
                img2, size=input_size, mode='bilinear', align_corners=False)
        else:
            input_size = orig_size

        input_t = torch.cat([img1, img2], 1).cuda()

        with torch.no_grad():
            output = self(input_t).data
            flow = div_flow * F.interpolate(
                output, size=input_size, mode='bilinear',
                align_corners=True)

        if input_size != orig_size:
            scale_h = orig_size[0] / input_size[0]
            scale_w = orig_size[1] / input_size[1]
            flow = F.interpolate(flow, size=orig_size, mode='bilinear', align_corners=False)
            flow[:, 0, :, :] *= scale_w
            flow[:, 1, :, :] *= scale_h

        flow = flow[0].cpu().permute(1, 2, 0).numpy()
        return flow
