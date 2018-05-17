# !/merak/desktop/python/
# @Time     : 8:37
# @Author   : Merak
# @File     : DrawTitle.py
# @Software : PyCharm

"""Draw Title"""


class DrawT:
    def __init__(self, length, message, gameboard, score, high_score=0):
        self.message = message
        self.gameboard = gameboard
        self.length = length
        self.high_score = high_score
        self.score = score

    def draw_title(self):
        self.gameboard.addstr(' '*int((self.length-4)/2) + '2048' + ' '*int((self.length-4)/2) + '\n')

    def draw_message(self):
        self.gameboard.addstr(' '*self.length-len(self.message) + self.message + '\n')

    def draw_score(self):
        self.gameboard.addstr('High Score: {:^6}'.format(self.high_score))
        self.gameboard.addstr('    Score: {:^6}'.format(self.score))
        self.gameboard.addstr('\n')
