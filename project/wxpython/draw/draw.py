# !/merak/desktop/python/project/wxpython/draw
# -*- coding: utf-8 -*-
# @Time     : 16:09
# @Author   : Merak
# @File     : test.py
# @Software : PyCharm
import wx
import figure


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

    def draw_line(self, line):

        dc = wx.ClientDC(self)
        dc.DrawLine(line.begin(), line.end())
        return 0

    def resize(self):
        self.SetSize((300, 400))

    def draw_circle(self, circle):
        dc = wx.ClientDC(self)
        dc.SetPen(wx.Pen(wx.Colour(0, 12, 56)))
        dc.DrawPointList(circle)

        dc.SetBrush(wx.Brush('#785f36'))
        dc.DrawRectangle(250, 195, 90, 60)
    # def max(self):
    #     self.ShowFullScreen(True)


if __name__ == '__main__':
    point1 = (50, 60)
    point2 = (50, 90)
    line = figure.Line(point1, point2)
    app = wx.App()
    e = Example()
    e.draw_line(line)
    circle = figure.Circle((0, 0), 50)
    points = circle.points()
    e.draw_circle(points)
    app.MainLoop()
