# !/merak/desktop/python/
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

# stdscr = curses.initscr()

'''
用户操作列表
'''
action = ["up", "right", "down", "left", "restart", "quit"]
available_input = [ord(char) for char in "wdsarqWDSARQ"]
action_dict = dict(zip(available_input, action * 2))

temp = 1
while True:
    if not os.path.isfile('log/operation_%i.log' % temp):
        break
    temp += 1
fhand = open('log/operation_%i.log' % temp, 'a')  # 打开日志文件
print(action_dict)


def write_in(string):
    s = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    s += string + '\n'
    fhand.write(s)


def input_char(gameboard):
    """
    键盘上按一个按键
    :return: string
    """
    char = "N"
    while char not in action_dict:
        char = gameboard.getch()
    return action_dict[char]


# d = input_char('s')
# print(d)

class Game:
    def __init__(self):
        self.rand2 = 0.8  # 随机出现2的概率
        self.height = 4
        self.width = 4
        self.score = 0
        self.high_score = 0
        # self.field = [[2, 2, 0, 0], [2, 2, 2, 0], [2, 2, 2, 2], [2, 0, 0, 2]]  # 测试move
        # self.field = [[2, 2, 0, 2], [2, 2, 2, 2], [2, 2, 2, 8], [2, 0, 0, 8]]  # 测试move
        # self.field = [[0, 0, 0, 0], [4, 2, 2, 2], [2, 2, 4, 8], [2, 2, 2, 8]]  # 测试game_over
        self.field = [[0, 2, 2, 0], [0, 0, 0, 0], [0, 0, 0, 4], [0, 0, 4, 0]]  # 测试game_over
        # self.field = [[2, 4, 5, 2], [1, 3, 2, 9], [10, 12, 22, 48], [92, 186, 74, 58]]  # 测试game_over
        self.field = [[0 for i in range(self.width)] for j in range(self.height)]
        self.message = ''
        # self.reset()

    def draw(self, gameboard):

        def cast(string):
            """
            gameboard上的输出函数
            :param string: 需要输出的
            """
            gameboard.addstr(string + '\n')

        def draw_row():
            cast('+'+"----+" * self.width)

        gameboard.clear()
        for i in range(self.height):
            for j in range(self.width):
                gameboard.addstr('{}'.format(self.field[i][j]) + '\t')
            gameboard.addstr('\n')
        if self.game_over():
            cast("Game Over!")

    def reset(self):
        """
        重新开始游戏，放置两个数字到棋盘上
        """

        if self.score > self.high_score:
            self.high_score = self.score
            self.message = 'New High Score'
            write_in("New High Score")
        write_in("Game reset")
        self.field = [[0 for i in range(self.width)] for j in range(self.height)]
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
        self.field[drop_point[0]][drop_point[1]] = new_element
        string = "Place " + str(new_element) + " at " + str(drop_point)
        write_in(string)

    def print_field(self):  # 输出矩阵
        for row in range(self.height):
            print(self.field[row])
        print('\n')

    def reverse(self):
        """
        矩阵向左转置
        """
        new = [[0 for i in range(self.width)] for j in range(self.height)]
        for row in range(self.height):
            for column in range(self.width):
                new[column][self.width-row-1] = self.field[row][column]
        self.field = new

    def move(self, direction):
        """
        操作矩阵
        """
        temp_matrix = [[0 for i in range(self.width)] for j in range(self.height)]
        for i in range(self.height):
            for j in range(self.width):
                temp_matrix[i][j] = self.field[i][j]
        print(temp_matrix == self.field)
        print(temp_matrix)
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
            flag = 0  # flag还未启用。在第一次合并后会启用，避免出现连续合并的现象
            current_row = 0  # 记录目前转换后的数字的位置
            for row in range(1, self.height):
                if self.field[row][column] == 0 or row == current_row:  # 无元素
                    continue
                elif self.field[row][column] == self.field[current_row][column]:  # 相同元素
                    # if flag == 0:
                    self.field[current_row][column] *= 2
                    self.field[row][column] = 0
                    current_row += 1
                    flag = 1  # flag已使用
                # else:
                    flag = 0  # flag重置为未使用
                else:  # 不同元素
                    if self.field[current_row][column] != 0:
                        current_row += 1
                    # current_row += 1
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
        self.print_field()
        print(temp_matrix)
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
                write_in("There is zero in row ")
                return 0
        write_in("There aren't any 0")
        for i in range(0, self.height):
            for j in range(1, self.width):
                write_in("Testing %i, %i" % (i, j))
                if self.field[i][j] == self.field[i][j-1]:
                    write_in("Game not over %i, %i" % (i, j))
                    return 0
        for i in range(0, self.width):
            for j in range(1, self.height):
                write_in("Testing %i, %i" % (i, j))
                if self.field[i][j] == self.field[i-1][j]:
                    write_in("Game not over %i, %i" % (i, j))
                    return 0
        write_in("Game Over\n")
        return 1


# game = Game()
# print(game.game_over())
# game.print_field()


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
            write_in("Input: "+direction)
            print("direction: "+direction)
            if direction == "restart":
                return "restart"
            elif direction == "quit":
                write_in("Quit")
                return "quit"
            flag = game.move(direction)
        game.place()
        if game.game_over():
            return "game_over"
        game.draw(gameboard)
        return "gaming"

    def game_over():
        game.draw(gameboard)
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
    while status != "quit":
        print(status)
        status = status_action[status]()
    init()


curses.wrapper(main)


# game.print_field()

# REVERSE
# game.reverse()
# game.print_field()
# game.reverse()
# game.print_field()
# game.reverse()
# game.print_field()

# # GAME
# game = Game()
# game.print_field()
# while True:
#     a = input("direction")
#     if a == 'q':
#         write_in('quit')
#         break
#     else:
#         print(action_dict[ord(a)])
#         game.move(action_dict[ord(a)])
#         game.print_field()
#
#
# game.print_field()

# game.reverse()
# game.print_field()
# game.place()
