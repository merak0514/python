# !/merak/desktop/python/
# @Time     : 20:30
# @Author   : Merak
# @File     : test2.py
# @Software : PyCharm
from curses import wrapper


def main(stdscr):
    # Clear screen
    stdscr.clear()

    # This raises ZeroDivisionError when i == 10.
    for i in range(0, 9):
        v = i-10
        stdscr.addstr(i, 0, '10 divided by {} is {}'.format(v, 10/v))

    # stdscr.refresh()      # 似乎可有可无
    stdscr.getkey()


wrapper(main)
