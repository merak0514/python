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
background_color_set = []  # 背景部分颜色集


def to_grey(im):
    im.convert('P')
    sort_color(im)  # 得到有用的颜色集


def sort_color(im):
    his = im.histogram()
    value = {}
    last_color_freq = -1
    flag = 0  # 0指向background color，1指向front color
    for i in range(256):
        value[i] = his[i]
    for j, k in sorted(value.items(), key=lambda a: a[1], reverse=True):
        if last_color_freq == -1:
            background_color_set.append(j)
            last_color_freq = k
            flag = 0
        elif k >= 0.6 * last_color_freq and flag == 0:
            background_color_set.append(j)
            last_color_freq = k
        elif k >= 0.5 * last_color_freq and flag == 1:
            front_color_set.append(j)
            last_color_freq = k
        elif flag == 0:
            front_color_set.append(j)
            last_color_freq = k
            flag = 1
        else:
            break
    print(background_color_set, front_color_set)


im = Image.open("python_captcha/captcha.gif")
to_grey(im)
