# !/user/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 9:18
# @Author   : Merak
# @File     : crack.py
# @Software : PyCharm

from PIL import Image
import re
grey_list = []
front_color_set = []  # 主体部分使用颜色集
background_color = 255  # 背景部分颜色集


def to_grey(im):
    im.convert('P')
    sort_color(im)  # 得到有用的颜色集
    new_im = Image.new("P", im.size,  255)
    for i in range(im.size[0]):
        for j in range(im.size[1]):
            pix = im.getpixel((i, j))
            if pix in front_color_set:
                new_im.putpixel((i, j), 0)
    return new_im



def sort_color(im):
    his = im.histogram()
    value = {}
    last_color_freq = -1
    flag = 0  # 0指向background color，1指向front color
    for i in range(256):
        value[i] = his[i]
    for j, k in sorted(value.items(), key=lambda a: a[1], reverse=True):
        if flag == 0:
            background_color = j
            flag = 1
            last_color_freq = -1
        elif flag == 1:
            if last_color_freq == -1:
                front_color_set.append(j)
                last_color_freq = k
            elif k >= 0.5 * last_color_freq or last_color_freq == -1:
                front_color_set.append(j)
            else:
                break
    print(background_color, front_color_set)


im = Image.open("python_captcha/captcha.gif")
im_new = to_grey(im)
im_new.save('black.gif', 'GIF')
