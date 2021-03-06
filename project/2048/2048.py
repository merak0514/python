# !/user/bin/env python
# @Time     : 19:47
# @Author   : Merak
# @File     : 2048.py
# @Software : PyCharm
# ord函数：输入字符，返回一个ASCII或Unicode数值
# zip函数：接收多个序列，打包后返回一个序列（需要用list（））打出
# list(zip([1,2,3],[4,5]))->[(1,4),(2,5)]
# 原来的bug：在curses.wrapper()中的a=list(), b=list(), a=b会使两者占用内存位置相同。
import curses
from random import random, choice
import datetime
import os
import DrawTitle

'''
用户操作列表
'''
action = ["up", "right", "down", "left", "restart", "quit"]
available_input = [ord(char) for char in "wdsarqWDSARQ"]
action_dict = dict(zip(available_input, action * 2))

"""
日志部分
"""
temp = 1
while True:
    if not os.path.isfile('log/operation_%i.log' % temp):
        break
    temp += 1
# fhand = open('log/operation_%i.log' % temp, 'a')  # 打开日志文件


def write_in(string):
    s = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    s += string + '\n'
    # fhand.write(s)


def input_char(gameboard):
    """
    键盘上按一个按键
    :return: string
    """
    char = "N"
    while char not in action_dict:
        char = gameboard.getch()
    return action_dict[char]


class Game:
    def __init__(self):
        self.rand2 = 0.8  # 随机出现2的概率
        self.height = 4
        self.width = 4
        self.score = 0
        self.high_score = 0
        self.field = [[0 for i in range(self.width)]
                      for j in range(self.height)]
        self.message = ''  # 其实没用用
        self.reset()  # 初始化

    def draw(self, gameboard, is_game_over=False):

        def cast(string):
            """ gameboard上的输出函数"""
            gameboard.addstr(string + '\n')

        def draw_row():
            cast('+' + "-----+" * self.width)

        gameboard.clear()
        d = DrawTitle.DrawT(self.width * 6, self.message,
                            gameboard, self.score, self.high_score)
        d.draw_title()
        d.draw_score()

        for i in range(self.height):
            draw_row()
            for j in range(self.width):
                gameboard.addstr('|{:^5}'.format(
                    self.field[i][j])if self.field[i][j] > 0 else '|     ')
            gameboard.addstr('|\n')
        draw_row()

        if is_game_over:
            cast("Game Over!")
            cast("(r)Restart; (q)Quit")
        else:
            cast("(w)Up; (d)Right; (s)Down; (a)Left; (r)Restart; (q)Quit")

    def reset(self):
        """
        重新开始游戏，放置两个数字到棋盘上
        """
        if self.score > self.high_score:
            self.high_score = self.score
            self.message = 'New High Score'
            write_in("New High Score")
        write_in("Game reset")
        self.field = [[0 for i in range(self.width)]
                      for j in range(self.height)]
        self.score = 0
        self.place()
        self.place()

    def place(self):
        """
            随机放置一个数字（2/4）到矩阵中任意为0位置上
            生成2的概率为rand2
        """
        new_element = 2 if random() < self.rand2 else 4
        drop_point = choice([(i, j) for i in range(self.height)
                             for j in range(self.width) if self.field[i][j] == 0])
        self.field[drop_point[0]][drop_point[1]] = new_element
        string = "Place " + str(new_element) + " at " + str(drop_point)
        write_in(string)

    def print_field(self):  # 输出矩阵，在测试中使用
        for row in range(self.height):
            print(self.field[row])
        print('\n')

    def reverse(self):
        """
        矩阵向右旋转
        """
        new = [[0 for i in range(self.width)] for j in range(self.height)]
        for row in range(self.height):
            for column in range(self.width):
                new[column][self.width - row - 1] = self.field[row][column]
        self.field = new

    def move(self, direction):
        """
        操作矩阵
        """
        temp_matrix = [[0 for i in range(self.width)]
                       for j in range(self.height)]
        for i in range(self.height):
            for j in range(self.width):
                temp_matrix[i][j] = self.field[i][j]
        if direction == "left":
            self.reverse()
        elif direction == "down":
            self.reverse()
            self.reverse()
        elif direction == "right":
            self.reverse()
            self.reverse()
            self.reverse()
        for column in range(self.width):  # 移动元素
            current_row = 0  # 记录目前转换后的数字的位置
            for row in range(1, self.height):
                if self.field[row][column] == 0 or row == current_row:  # 无元素
                    continue
                elif self.field[row][column] == self.field[current_row][column]:  # 相同元素
                    self.score += self.field[current_row][column]
                    self.field[current_row][column] *= 2
                    self.field[row][column] = 0
                    current_row += 1
                else:  # 不同元素
                    if self.field[current_row][column] != 0:
                        current_row += 1
                    self.field[current_row][column] = self.field[row][column]
                    self.field[row][column] = 0 if row != current_row else self.field[row][column]

        if direction == "left":
            self.reverse()
            self.reverse()
            self.reverse()
            write_in("Move left")
        elif direction == "down":
            self.reverse()
            self.reverse()
            write_in("Move down")
        elif direction == "right":
            self.reverse()
            write_in("Move right")
        else:
            write_in("Move up")
        if temp_matrix == self.field:
            write_in("Not Success")
            return 0
        else:
            write_in("Success")
            return 1

    def game_over(self):
        """
        判断是否失败
        :return: bool 失败返回1；成功返回0；
        """
        for row in self.field:
            if 0 in row:
                return 0
        write_in("There aren't any 0")
        for i in range(0, self.height):
            for j in range(1, self.width):
                if self.field[i][j] == self.field[i][j - 1]:
                    return 0
        for i in range(0, self.width):
            for j in range(1, self.height):
                if self.field[j][i] == self.field[j - 1][i]:
                    return 0
        write_in("Game Over\n")
        self.message = "Game Over"
        return 1


# Real game
def main(gameboard):

    def init():
        game.reset()
        return "gaming"

    def gaming():
        """
        一次操作：获得输入的操作，根据操作执行一次，生成一个新的方块
        :return: string 游戏状态
        """
        game.draw(gameboard)
        flag = 0
        while flag != 1:
            direction = input_char(gameboard)
            write_in("Input: " + direction)
            if direction == "restart":
                return "restart"
            elif direction == "quit":
                write_in("Quit")
                return "quit"
            flag = game.move(direction)
        game.place()
        if game.game_over():
            return "game_over"
        return "gaming"

    def game_over():
        game.draw(gameboard, True)
        while True:
            a = input_char(gameboard)
            if a == "quit" or a == "restart":
                break
        return a

    status_action = {
        "restart": init,
        "gaming": gaming,
        "game_over": game_over,
    }

    game = Game()
    status = "restart"
    while status != "quit":  # 状态机循环
        status = status_action[status]()


curses.wrapper(main)
