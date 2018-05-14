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
        # self.field = [[2, 2, 0, 0], [2, 2, 2, 0], [2, 2, 2, 2], [2, 0, 0, 2]]  # 单元测试
        # self.field = [[2, 2, 0, 2], [2, 2, 2, 2], [2, 2, 2, 8], [2, 0, 0, 8]]  # 单元测试
        self.field = [[0 for i in range(self.width)] for j in range(self.height)]
        self.message = ''
        # self.reset()

    def draw(self, gameboard):

        def cast(string):
            """
            gameboard上的输出函数
            :param string: 需要输出的
            """
            gameboard.addstr(string, '\n')

        def draw_row():
            cast('+'+"----+" * self.width)

        gameboard.clear()
        for i in range(self.height):
            for j in range(self.width):
                gameboard.addstr(self.field[i][j], '\t')
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
                new[column][row] = self.field[row][column]
        self.field = new

    def move(self, direction):
        """
        操作矩阵
        """
        temp = self.field
        if direction == "right":
            self.reverse()
        elif direction == "down:":
            self.reverse()
            self.reverse()
        elif direction == "left":
            self.reverse()
            self.reverse()
            self.reverse()
        for column in range(self.width):  # 移动元素
            current_row = 0  # 记录目前转换后的数字的位置
            for row in range(self.height):
                if self.field[row][column] == 0 or row == current_row:  # 无元素
                    continue
                elif self.field[row][column] == self.field[current_row][column]:  # 相同元素
                    self.field[current_row][column] *= 2
                    self.field[row][column] = 0
                else:  # 不同元素
                    if self.field[current_row][column] != 0:
                        current_row += 1
                    self.field[current_row][column] = self.field[row][column]
                    self.field[row][column] = 0 if row != current_row else self.field[row][column]
        if direction == "right":
            self.reverse()
            self.reverse()
            self.reverse()
        elif direction == "down:":
            self.reverse()
            self.reverse()
        elif direction == "left":
            self.reverse()
        if temp == self.field:
            return 0
        else:
            return 1

    def game_over(self):
        """
        判断是否失败
        :return: bool 失败返回1；成功返回0；
        """
        for i in range(2, self.height-1):
            for j in range(2, self.width-1):
                if self.field[i][j] == (self.field[i][j - 1] or self.field[i][j + 1]
                                        or self.field[i - 1][j] or self.field[i + 1][j] or 0):
                    return 1
                return 0


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
            if direction == "restart":
                return "restart"
            elif direction == "quit":
                return "quit"
            flag = game.move(direction)
        game.place()
        if game.game_over():
            return "game_over"
        game.draw(gameboard)
        return "gaming"

    def game_over():
        game.draw(gameboard)

    status_action = {
        "restart": init,
        "gaming": gaming,
        "game_over": game_over
    }

    game = Game()
    status = "init"
    while status != "quit":
        status = status_action[status]()
    # game.print_field()
    # # a = 1
    # # while a != 0:
    # game.move("left")
    # # a = int(input('输入a'))
    # game.print_field()
    # # game.reverse()
    # # game.print_field()
    # # game.place()


curses.wrapper(main)
