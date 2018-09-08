# !/user/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 23:16
# @Author   : Merak
# @File     : test.py
# @Software : PyCharm

from PIL import Image
import os


for i in list('0123456789qazwsxedcrfv'):
    path = "python_captcha/iconset/{}/".format(i)
    for file in os.listdir(path):
        if file != "Thumbs.db" and file != ".DS_Store":
            try:
                im = Image.open(path + file)
            except:
                print(path + file, " is not exist")
            else:
                print(firl)
