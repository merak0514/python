# 人带着猫鸡米划船过河，船只能带人和三者之一，且必须是人划。人不在时，猫吃鸡，鸡吃米。如何过河？

from random import randint


class Bank(object):
    """人猫鸡米"""

    def __init__(self, human, cat, chick, rice, capacity):
        self.human = human
        self.cat = cat
        self.chick = chick
        self.rice = rice
        self.capacity = capacity
        self.here = (human, cat, chick, rice)
        self.there = (0, 0, 0, 0)

        print('Initialized: %d human, %d cat, %d chick, %d rice, capacity: %d' % (
            human, cat, chick, rice, capacity))

    '''
    允许状态集合
    '''

    def allowStatusSet(self):
        allow_set = []
        for i in range(self.human + 1):
            for j in range(self.cat + 1):
                for k in range(self.chick + 1):
                    for l in range(self.rice + 1):
                        if i >= 1 or not (k >= 1 and (l >= 1 or j >= 1)):
                            allow_set.append((i, j, k, l))
        return allow_set

    '''
    允许决策集合
    '''

    def allowMethods(self):
        allow_methods = []
        for i in range(self.human + 1):
            for j in range(self.cat + 1):
                for k in range(self.chick + 1):
                    for l in range(self.rice + 1):
                        if i >= 1 and (i + j + k + l) <= self.capacity:
                            allow_methods.append((i, j, k, l))
        return allow_methods

    '''
    可采用策略集合
    '''

    def availableMethods(self):
        return self.allowMethods()

    '''
    上船过河
    '''

    def goBoard(self, method, flag, currant_here, currant_there):
        # self.here[0] -= method[0] * (-1)**flag
        # self.here[1] -= method[1] * (-1)**flag
        # self.here[2] -= method[2] * (-1)**flag
        # self.here[3] -= method[3] * (-1)**flag
        # self.there[0] += method[0] * (-1)**flag
        # self.there[1] += method[1] * (-1)**flag
        # self.there[2] += method[2] * (-1)**flag
        # self.there[3] += method[3] * (-1)**flag
        currant_here = (currant_here[0] + (-1)**flag * method[0],
                        currant_here[1] + (-1)**flag * method[1],
                        currant_here[2] + (-1)**flag * method[2],
                        currant_here[3] + (-1)**flag * method[3])
        currant_there = (currant_there[0] - (-1)**flag * method[0],
                         currant_there[1] - (-1)**flag * method[1],
                         currant_there[2] - (-1)**flag * method[2],
                         currant_there[3] - (-1)**flag * method[3])
        return currant_here, currant_there

    '''
    solution
    '''

    def solution(self):
        count = 1
        allow_set = self.allowStatusSet()
        while self.here != (0, 0, 0, 0):
            available_methods = self.availableMethods()
            print(len(available_methods))
            method = available_methods[randint(0, len(available_methods) - 1)]
            print(method)
            temp = self.goBoard(method, count % 2, self.here, self.there)
            print(temp)
            if temp[0] in allow_set or temp[1] in allow_set:
                self.here = temp[0]
                self.there = temp[1]
                print('a')
                print(self.here)
                print('%d 个人，%d 只猫，%d 只鸡，%d 米，在第%d 次渡河的船上' %
                      (method[0], method[1], method[2], method[3], count))
                count += 1


def main():
    bank = Bank(1, 1, 1, 1, 2)

    allow_set = bank.allowStatusSet()
    print("允许状态集合：")
    print(allow_set)

    allow_actions_set = bank.allowMethods()
    print("允许决策集合：")
    print(allow_actions_set)

    bank.solution()


main()
