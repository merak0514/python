# !/merak/desktop/python/
# -*- coding: utf-8 -*-
# @Time     : 20:07
# @Author   : Merak
# @File     : test.py
# @Software : PyCharm
import wx


class Example(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)
        self.InitUI()

    def InitUI(self):

        menu_bar = wx.MenuBar()
        fileMenu = wx.Menu()
        file_item = fileMenu().Append(wx.ID_EXIT, 'Quit', 'Quit application')
        menu_bar.Append(fileMenu, '&File')
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