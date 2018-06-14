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


def cut_picture(im):
    im.convert('1')
    column_set = list()  # 切割点所在列号
    row_set = list()  # 切割点的行号
    flag1 = 0
    flag2 = 0
    print(im.size)
    for i in range(im.size[0]):  # 获得需要切割的列号
        for j in range(im.size[1]):
            if im.getpixel((i, j)) != background_color:
                if flag1 == 0:
                    column_set.append(i)
                flag1 = 1  # 进入字母前的列标采集完成
                break
        else:
            if flag1 == 1:
                column_set.append(i)
                flag1 = 0  # 离开字母的列标采集完成
    for j in range(im.size[1]):  # 获得需要切割的行号
        for i in range(im.size[0]):
            if im.getpixel((i, j)) != background_color:
                if flag2 == 0:
                    row_set.append(j)
                    flag2 = 1  # 已获得第一个行号
                break
        else:
            if flag2 == 1:
                row_set.append(j)
                break
    print(column_set, row_set)


def to_grey(im):
    im.convert('P')
    sort_color(im)  # 得到有用的颜色集
    new_im = Image.new("1", im.size,  255)
    for i in range(im.size[0]):
        for j in range(im.size[1]):
            pix = im.getpixel((i, j))
            if pix in front_color_set:
                new_im.putpixel((i, j), 0)
    return new_im


def sort_color(im):
    global front_color_set, background_color
    his = im.histogram()
    value = {}
    # last_color_freq = -1
    flag = 0  # 0指向background color，1指向front color
    for i in range(256):
        value[i] = his[i]
    for j, k in sorted(value.items(), key=lambda a: a[1], reverse=True):
        if flag == 0:
            background_color = j
            flag = 1
            # last_color_freq = -1
        # elif flag == 1:
        #     if last_color_freq == -1:
        #         front_color_set.append(j)
        #         last_color_freq = k
        #     elif k >= 0.5 * last_color_freq or last_color_freq == -1:
        #         front_color_set.append(j)
        #     else:
        #         break
    # 我日这样不行，手动设置
    front_color_set = [220, 227]
    print(background_color, front_color_set)


im = Image.open("python_captcha/captcha.gif")
im_new = to_grey(im)
im_new.save('black.gif', 'GIF')
cut_picture(im_new)
