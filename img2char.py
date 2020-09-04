#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import argparse
import cv2
import numpy as np

__version__ = '1.0.0'
__author__ = 'ShengYu'
__license__ = 'MIT'

ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")

def get_parser():
    parser = argparse.ArgumentParser('img2char')
    version = '%(prog)s ' + __version__
    parser.add_argument('-v', '--version', action = 'version', version = version)
    parser.add_argument('image') # 輸入檔案
    parser.add_argument('-o', '--output', type = str, default = 'output.txt', help='output filename, default=output.txt') # 輸出檔案
    parser.add_argument('-W', '--width', type = int, default = 80, help='the width of output text, default=80') # 輸出字元圖畫寬
    parser.add_argument('-H', '--height', type = int, default = 80, help='the height of output text, default=80') # 輸出字元圖畫高
    return parser

# 將256灰階(gray)對應到70個字元(ascii_char)上
def gray2char(gray):
    length = len(ascii_char)

    unit = (256.0 + 1)/length
    return ascii_char[int(gray/unit)]

if __name__ == '__main__':
    parser = get_parser()
    args = parser.parse_args()
    in_image_filename = args.image
    width = args.width
    height = args.height
    out_text_filename = args.output

    img = cv2.imread(in_image_filename, 0)
    img = cv2.resize(img, (width,height), interpolation=cv2.INTER_NEAREST)

    txt = ""
    for i in range(height):
        for j in range(width):
            txt += gray2char(img[i,j])
        txt += '\n'
    print(txt)

    # 將字元圖畫輸出到檔案
    with open(out_text_filename,'w') as f:
        f.write(txt)
