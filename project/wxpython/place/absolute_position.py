# !/user/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 11:21
# @Author   : Merak
# @File     : absolute_position.py
# @Software : PyCharm

"""
ZetCode wxPython tutorial

In this example, we lay out widgets using
absolute positioning.

author: Jan Bodnar
website: www.zetcode.com
last modified: April 2018
"""

import wx


class Example(wx.Frame):

    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title, size=(350, 300))

        self.InitUI()
        self.Centre()

    def InitUI(self):

        self.panel = wx.Panel(self)

        self.panel.SetBackgroundColour("gray")

        self.LoadImages()

        self.a.SetPosition((20, 20))
        self.b.SetPosition((40, 160))
        self.c.SetPosition((170, 50))

    def LoadImages(self):

        self.a = wx.StaticBitmap(self.panel, wx.ID_ANY,
            wx.Bitmap("a.jpg", wx.BITMAP_TYPE_ANY))
        # self.a.SetClientSize((40, 40))

        self.b = wx.StaticBitmap(self.panel, wx.ID_ANY,
            wx.Bitmap("b.jpg", wx.BITMAP_TYPE_ANY))

        self.c = wx.StaticBitmap(self.panel, wx.ID_ANY,
            wx.Bitmap("c.jpg", wx.BITMAP_TYPE_ANY))


def main():

    app = wx.App()
    ex = Example(None, title='Absolute positioning')
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()