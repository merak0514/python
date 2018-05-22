# !/merak/desktop/python/project/wxpython/Test
# -*- coding: utf-8 -*-
# @Time     : 16:09
# @Author   : Merak
# @File     : test.py
# @Software : PyCharm
import wx
from Point import Point


class Example(wx.Frame):
    def __init__(self):
        super(Example, self).__init__(None)
        self.SetSize((500, 600))
        self.SetTitle('Line')
        wx.CallLater(1000, self.resize)
        # self.Bind(wx.EVT_PAINT, self.OnPaint)
        # wx.CallLater(2000, self.max)
        self.Center()
        self.Show()
        # self.OnPaint()

    # def OnPaint(self):
    #     dc = wx.ClientDC(self)
    #     dc.DrawLine((50, 60), (100, 120))

    def draw_line(self, pointa=Point, pointb=Point):
        dc = wx.ClientDC(self)
        dc.DrawLine(pointa.position(), pointb.position())
        return 0

    def resize(self):
        self.SetSize((300, 400))

    # def max(self):
    #     self.ShowFullScreen(True)


if __name__ == '__main__':
    point1 = Point(50, 60)
    point2 = Point(50, 90)
    app = wx.App()
    e = Example()
    e.draw_line(point1, point2)
    app.MainLoop()
