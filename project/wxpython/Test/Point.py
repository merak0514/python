# !/merak/desktop/python/
# -*- coding: utf-8 -*-
# @Time     : 9:26
# @Author   : Merak
# @File     : Point.py
# @Software : PyCharm
import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def position(self):
        return self.x, self.y
