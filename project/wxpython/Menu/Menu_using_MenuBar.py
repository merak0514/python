# !/user/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 20:07
# @Author   : Merak
# @File     : Menu_using_MenuBar.py
# @Software : PyCharm
"""
ZetCode wxPython tutorial

This example shows a simple menu.

author: Jan Bodnar
website: www.zetcode.com
last modified: April 2018
"""
import wx


class Example(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)
        self.InitUI()

    def InitUI(self):

        menu_bar = wx.MenuBar()
        file_menu = wx.Menu()
        file_item = file_menu.Append(wx.ID_EXIT, 'Quit', 'Quit application')
        menu_bar.Append(file_menu, 'File')
        self.SetMenuBar(menu_bar)

        self.Bind(wx.EVT_MENU, self.OnQuit, file_item)

        self.SetSize((300, 200))
        self.SetTitle('Simple Menu')
        self.Center()

    def OnQuit(self, e):
        self.Close()


def main():

    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()