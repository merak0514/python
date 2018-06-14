# !/user/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 9:18
# @Author   : Merak
# @File     : crack.py
# @Software : PyCharm

from PIL import Image
import re
import os

grey_list = []
front_color_set = []  # 主体部分使用颜色集
background_color = 255  # 背景部分颜色集
parent_set = list()


def cut_picture(im):
    im.convert('1')
    column_set = list()  # 切割点所在列号
    row_set = list()  # 切割点的行号
    flag1 = 0
    flag2 = 0
    temp = -1
    im_set = list()
    print(im.size)
    for i in range(im.size[0]):  # 获得需要切割的列号
        for j in range(im.size[1]):
            if im.getpixel((i, j)) != background_color:
                if flag1 == 0:
                    temp = i
                flag1 = 1  # 进入字母前的列标采集完成
                break
        else:
            if flag1 == 1:
                column_set.append((temp, i))
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
    for i in column_set:
        temp_im = im.crop((i[0], row_set[0], i[1], row_set[1]))
        im_set.append(temp_im)
    print(im_set)


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


def train():
    global parent_set
    for i in list('0123456789qazwsxedcrfvtgbyhnujmikolp'):
        base_path = "python_captcha/iconset/{}/".format(i)
        for file_name in os.listdir(base_path):
            if file_name != 'Thumbs.db' and file_name != '.DS_Store':
                im = Image.open(base_path + file_name)
                temp = im_to_vector(im)
                parent_set.append({i: temp})


def im_to_vector(im: Image.Image):
    """
    获得的向量是由从数字黑白图开始到结束的像素构成
    返回的向量是一个dict，其中键为从数字开端开始横向计数的像素编号
    会删去末尾的空白
    :param im: Image.Image
    :return: dict
    """
    flag = 0  # 还未找到第一个字符
    vector = dict()
    count = 0
    im.convert('1')
    for j in range(im.size[1]):
        for i in range(im.size[0]):
            pixel = im.getpixel((i, j))
            if flag == 0 and pixel == 0:
                vector[count] = pixel
                flag = 1
                count += 1
            elif flag == 1:
                vector[count] = pixel
                count += 1
    for i in range(count):
        if vector[count - i - 1] == 255:
            del(vector[count - i - 1])
            continue
        break
    print(vector)
    return vector


image = Image.open("python_captcha/captcha.gif")
im_new = to_grey(image)
im_new.save('black.gif', 'GIF')
cut_picture(im_new)
train()
print(parent_set)
