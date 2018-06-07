# !/user/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 22:20
# @Author   : Merak
# @File     : 2048.py
# @Software : PyCharm
"""
设置背景颜色
设置字体
"""
import wx


class GameBoard2048(wx.Frame):
    def __init__(self, title):
        super(GameBoard2048, self).__init__(None, title=title)
        self.matrix = list([2, 4, 8, 2, 0, 4, 0, 2, 4, 0, 0, 8, 2, 0, 0, 0])
        self.init_ui()

    def init_ui(self):
        self.SetSize((450, 400))
        self.menu()
        v_box = wx.BoxSizer(wx.VERTICAL)
        v_box.Add(self.head())
        self.SetSizer(v_box)
        self.SetBackgroundColour('white')  # 设置背景颜色
        v_box.Add(self.body(), wx.EXPAND, wx.ALIGN_CENTER)

    def head(self):
        h_box = wx.BoxSizer(wx.HORIZONTAL)
        static_txt = wx.StaticText(self, label='2048')
        font = wx.Font(18, wx.DECORATIVE, wx.ITALIC, wx.NORMAL)  # 设置字体
        static_txt.SetFont(font)
        h_box.Add(static_txt)
        return h_box

    def body(self):
        def numbers():
            gs = wx.GridSizer(4, 4, 5, 5)
            for num in self.matrix:
                st = wx.StaticText(self, label=str(num))
                gs.Add(st, flag=wx.EXPAND | wx.ALL)
            return gs
        h_box = wx.BoxSizer(wx.HORIZONTAL)
        # h_box.AddStretchSpacer()
        h_box.Add(numbers())
        # h_box.AddStretchSpacer()
        return h_box

    def menu(self):
        def on_quit(e):
            self.Close()
        menu_bar = wx.MenuBar()
        self.SetMenuBar(menu_bar)
        menu1 = wx.Menu()
        menu_bar.Append(menu1, "File")
        quitor = wx.MenuItem(menu1, wx.ID_EXIT, "Quit\tCtrl+q")
        reset = wx.MenuItem(menu1, wx.ID_ANY, "Reset\tCtrl+r")
        self.Bind(wx.EVT_MENU, on_quit, quitor)
        menu1.Append(quitor)
        menu1.Append(reset)


def main():
    app = wx.App()
    game2048 = GameBoard2048('2048')
    game2048.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
