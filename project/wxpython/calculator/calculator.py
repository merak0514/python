# !/merak/desktop/python/project/wxpython/calculator/calculator
# -*- coding: utf-8 -*-
# @Time     : 9:19
# @Author   : Merak
# @File     : calculator.py
# @Software : PyCharm
import wx


class Calculator(wx.Frame):

    def __init__(self, parent, title):
        super(Calculator, self).__init__(parent, title=title)

        self.initUI()
        self.Center()

    def initUI(self):

        self.menu()

        # self.grid_sizer()

    def menu(self):
        # menu bar
        menu_bar = wx.MenuBar()

        # menu
        file_menu = wx.Menu()

        # menu item
        quitor = wx.MenuItem(file_menu, wx.ID_EXIT, "Quit\tCtrl+q")
        reset = wx.MenuItem(file_menu, wx.ID_ANY, "Reset\tCtrl+r")

        # add menu item to menu
        file_menu.Append(wx.ID_NEW, "New")
        file_menu.Append(quitor)
        file_menu.Append(reset)
        # add menu to menu bar
        menu_bar.Append(file_menu, "File")

        # bind
        self.Bind(wx.EVT_MENU, self.on_quit, quitor)

        # add menu bar to window
        self.SetMenuBar(menu_bar)

    def on_quit(self, e):
        self.Close()


def main():

    app = wx.App()
    calculator = Calculator(None, "Calculator")
    calculator.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
