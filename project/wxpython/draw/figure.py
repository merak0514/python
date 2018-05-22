# !/merak/desktop/python/
# -*- coding: utf-8 -*-
# @Time     : 9:26
# @Author   : Merak
# @File     : figure.py
# @Software : PyCharm
import math


class Line(object):
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y2 = y1
        self.x2 = x2
        self.y2 = y2

    def __init__(self, point1, point2):
        self.x1 = point1[0]
        self.y1 = point1[1]
        self.x2 = point2[0]
        self.y2 = point2[1]

    def begin(self):
        return self.x1, self.y1

    def end(self):
        return self.x2, self.y2


class Circle(object):
    def __init__(self, center, radius):
        self.center = center
        self.r = radius

    def points(self):
        point_set = list()
        for theta in range(0, int(200 * math.pi), 1):
            x = self.r * math.cos(theta/100)
            y = self.r * math.sin(theta/100)
            point_set.append((x, y))
        return point_set

# class Triangle(object):
#     def __init__(self, x1, y1, x2, y2, x3, y3):
#         if (y2 - y1)/(x2 - x1) == (y3 - y1)/(x3 - x1):
#             raise ValueError("Can't become a triangle")
#         self.x1 = x1
#         self.y1 = y1
#         self.y2 = y2
#         self.x2 = x2
#         self.x3 = x3
#         self.y3 = y3
#
#     def