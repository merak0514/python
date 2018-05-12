# !/merak/desktop/python/
# @Time     : 19:47
# @Author   : Merak
# @File     : 2048.py
# @Software : PyCharm
# ord函数：输入字符，返回一个ASCII或Unicode数值
# zip函数：接收多个序列，打包后返回一个序列（需要用list（））打出
# list(zip([1,2,3],[4,5]))->[(1,4),(2,5)]
import curses
from random import random, choice
# stdscr = curses.initscr()

'''
用户操作列表
'''
action = ["up", "right", "down", "left", "restart", "exit"]
available_input = [ord(char) for char in "wdsarqWDSARQ"]
action_dict = dict(zip(available_input, action * 2))

'''
状态判定
'''


class Game:
    def __init__(self):
        self.rand2 = 0.8     # 随机出现2的概率
        self.height = 4
        self.width = 4
        self.score = 0
        self.high_score = 0
        self.field = [[2, 2, 0, 0], [2, 2, 2, 0], [2, 2, 2, 2], [2, 0, 0, 2]]  # 单元测试
        # self.field = [[0 for i in range(self.width)] for j in range(self.height)]
        self.message = ''
        # self.reset()

    def reset(self):

        if self.score > self.high_score:
            self.high_score = self.score
            self.message = 'New High Score'
        self.score = 0
        # self.draw_game_board()
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
        self.field[drop_point[1]][drop_point[1]] = new_element

    def print_field(self):
        for row in range(self.height):
            print(self.field[row])
        print('\n')

    def move(self):
        """
        先移动元素到合理位置
        再把相邻元素合并
        :return:
        """

        for column in range(self.width):  # 移动元素
            current_row = 0  # 记录目前转换后的数字的位置
            for row in range(self.height):
                if self.field[row][column] == 0 or row == current_row:        # 无元素
                    continue
                elif self.field[row][column] == self.field[current_row][column]:
                    self.field[current_row][column] *= 2
                    self.field[row][column] = 0
                    # current_row += 1
                else:
                    current_row += 1
                    self.field[current_row][column] = self.field[row][column]
                    self.field[row][column] = 0 if row != current_row else self.field[row][column]
                    # current_row += 1

                # else:
                #     for position in range(row - 1, 0, 1):
                #         if self.field[position][column] == 0:
                #             continue
                #         if self.field[position][column] == self.field[row][column]:
                #             self.field[position][column] *= 2
                #             self.field[row][column] = 0
                #         else:
                #             temp = self.field[row][column]
                #             self.field[row][column] = 0
                #             self.field[position+1][column] = temp
        # for column in range(self.width):
        #     for row in range(1, self.height):


if __name__ == '__main__':
    game = Game()
    game.print_field()
    # a = 1
    # while a != 0:
    game.move()
    # a = int(input('输入a'))
    game.print_field()
        # game.place()
