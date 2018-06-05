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
        head = self.head()
        gs = self.grid_sizer()
        vbox.Add(head, flag=wx.EXPAND | wx.UP | wx.RIGHT | wx.LEFT, border=10)
        vbox.Add(gs, proportion=1, flag=wx.EXPAND)
        self.SetSizer(vbox)

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
        labels = list(["AC", 'DEL', 'Pi', 'CLOSE'])+list(char for char in "789+456-123*0.=/")
        gs = wx.GridSizer(5, 4, 5, 5)
        for label in labels:
            button = wx.Button(self, label=label)
            gs.Add(button, flag=wx.EXPAND | wx.ALL)
        return gs

    def head(self):
        # panel = wx.Panel()
        tc = wx.TextCtrl(self)
        vbox = wx.BoxSizer(wx.VERTICAL)
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        st1 = wx.StaticText(self, label="Input")
        hbox.Add(st1, flag=wx.RIGHT, border=8)
        hbox.Add(tc, proportion=1, flag=wx.EXPAND | wx.DOWN | wx.RIGHT | wx.LEFT, border=10)
        return hbox
        # vbox.Add(hbox, flag=wx.EXPAND | wx.UP | wx.RIGHT | wx.LEFT, border=10)
        # panel.SetSizer(vbox)

def main():

    app = wx.App()
    calculator = Calculator(None, "Calculator")
    calculator.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
