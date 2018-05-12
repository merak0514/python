# !/merak/desktop/python/
# @Time     : 9:45
# @Author   : Merak
# @File     : test.py
# @Software : PyCharm
import curses
from time import sleep


class A():
    def __init__(self, height=4, width=4, win=2048):
        self.height = height
        self.width = width
        self.win_value = win
        self.score = 0
        self.highscore = 0

    def add(self, a):
        a.clear()
        a.addstr('fsa')
        input('daf')


def main(screen):
    def init():
        # print('init')
        c.add(screen)
        # print('finish init')
        return 1
    c = A()
    s = 1
    while s < 5:
        s = init()
        s += 1
        sleep(1)

    curses.use_default_colors()


curses.wrapper(main)
