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

        self.SetSize((400, 450))
        self.menu()
        vbox = wx.BoxSizer(wx.VERTICAL)
        self.head()
        self.grid_sizer()

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

    def grid_sizer(self):
        vbox = wx.BoxSizer(wx.VERTICAL)
        gs = wx.GridSizer(4, 4, 5, 5)
        one = wx.Button(self, label="1")
        two = wx.Button(self, label="2")
        three = wx.Button(self, label="3")
        four = wx.Button(self, label="4")
        five = wx.Button(self, label="5")
        six = wx.Button(self, label="6")
        seven = wx.Button(self, label="7")
        eight = wx.Button(self, label="8")
        nine = wx.Button(self, label="9")
        zero = wx.Button(self, label="0")
        add = wx.Button(self, label="+")
        sub = wx.Button(self, label="-")
        multiple = wx.Button(self, label="*")
        divide = wx.Button(self, label="/")
        point = wx.Button(self, label=".")
        equal = wx.Button(self, label="=")

        gs.AddMany([
            (seven, 0, wx.EXPAND),
            (eight, 0, wx.EXPAND),
            (nine, 0, wx.EXPAND),
            (add, 0, wx.EXPAND),
            (four, 0, wx.EXPAND),
            (five, 0, wx.EXPAND),
            (six, 0, wx.EXPAND),
            (sub, 0, wx.EXPAND),
            (one, 0, wx.EXPAND),
            (two, 0, wx.EXPAND),
            (three, 0, wx.EXPAND),
            (multiple, 0, wx.EXPAND),
            (zero, 0, wx.EXPAND),
            (point, 0, wx.EXPAND),
            (equal, 0, wx.EXPAND),
            (divide, 0, wx.EXPAND),
        ])
        vbox.Add(gs, proportion=1, flag=wx.EXPAND)
        self.SetSizer(vbox)

    def head(self):
        panel = wx.Panel()
        tc = wx.TextCtrl(panel)
        vbox = wx.BoxSizer(wx.VERTICAL)
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        st1 = wx.StaticText(panel, label="Input")
        hbox.Add(st1, flag=wx.RIGHT, border=8)
        hbox.Add(tc, proportion=1)
        vbox.Add(hbox, flag=wx.EXPAND | wx.UP | wx.RIGHT | wx.LEFT, border=10)
        panel.SetSizer(vbox)


def main():

    app = wx.App()
    calculator = Calculator(None, "Calculator")
    calculator.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
