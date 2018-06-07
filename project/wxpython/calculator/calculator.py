# !/user/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 9:19
# @Author   : Merak
# @File     : calculator.py
# @Software : PyCharm
"""
排版思路：分为头部和board界面，分别采用几个box结合起来，其中多个数字键等批量生成
运算思路：将按键以一定形式，一定条件写到textctrl上，运算时读取textctrl上内容
"""
import wx


class Calculator(wx.Frame):

    def __init__(self, parent, title):
        super(Calculator, self).__init__(parent, title=title)
        self.output = ''
        self.result = 0
        self.last_operator = '+'
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

    def menu(self):  # 创建菜单
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

    def grid_sizer(self):  # 主界面
        labels = list(["AC", 'DEL', 'Pi', 'CLOSE'])+list(char for char in "789+456-123*0.=/")
        gs = wx.GridSizer(5, 4, 5, 5)
        for label in labels:
            button = wx.Button(self, label=label)
            self.add_method(label, button)
            gs.Add(button, flag=wx.EXPAND | wx.ALL)
        return gs

    def head(self):  # 头部（此处为文本框）
        self.tc = wx.TextCtrl(self, style=wx.TE_RIGHT)
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        st1 = wx.StaticText(self, label="Input")
        hbox.Add(st1, flag=wx.RIGHT, border=8)
        hbox.Add(self.tc, proportion=1, flag=wx.EXPAND | wx.DOWN | wx.RIGHT | wx.LEFT, border=10)
        return hbox

    def add_method(self, label, button):
        if label in "0123456789. Pi":
            self.Bind(wx.EVT_BUTTON, self.methodNumber, button)
        elif label == 'CLOSE':
            self.Bind(wx.EVT_BUTTON, self.methodClose, button)
        elif label == 'DEL':
            self.Bind(wx.EVT_BUTTON, self.methodDel, button)
        elif label == 'AC':
            self.Bind(wx.EVT_BUTTON, self.methodAC, button)
        elif label in "+-*/":
            self.Bind(wx.EVT_BUTTON, self.methodOperator, button)
        elif label == '=':
            self.Bind(wx.EVT_BUTTON, self.methodEqual, button)

    def methodNumber(self, event):
        if self.last_operator == '=':
            self.methodAC(event)
        event_button = event.GetEventObject()
        label = event_button.GetLabel()
        if label == 'Pi':
            label = '3.14159'
        self.output += label
        self.tc.SetValue(self.output)

    def methodClose(self, event):
        self.on_quit(event)

    def methodDel(self, event):  # 删除最后一位
        self.output = self.output[:len(self.output)-1]
        self.tc.SetValue(self.output)

    def methodAC(self, event):
        self.output = ''
        self.result = 0
        self.tc.Clear()
        self.last_operator = '+'

    def methodOperator(self, event):  # +-*/
        event_button = event.GetEventObject()
        label = event_button.GetLabel()
        num = float(self.output)
        self.operate(num)

        self.last_operator = label
        self.output = ''
        self.tc.SetValue(self.output)

    def methodEqual(self, event):  # =
        num = float(self.output)
        self.operate(num)
        self.output = str(self.result)
        self.tc.SetValue(self.output)
        self.last_operator = '='

    def operate(self, num):  # 计算
        if self.last_operator == '+':
            self.result += num
        if self.last_operator == '-':
            self.result -= num
        if self.last_operator == '*':
            self.result *= num
        if self.last_operator == '/':
            self.result /= num


def main():
    app = wx.App()
    calculator = Calculator(None, "Calculator")
    calculator.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
