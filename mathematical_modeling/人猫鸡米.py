# 人带着猫鸡米划船过河，船只能带人和三者之一，且必须是人划。人不在时，猫吃鸡，鸡吃米。如何过河？

from random import randint


class Bank(object):
    """人猫鸡米"""

    def __init__(self, human, cat, chick, rice, capacity):
        self.CAPACITY = capacity
        self.here = (human, cat, chick, rice)
        self.START = self.here
        self.there = (0, 0, 0, 0)
        self.forbiden_methods = []
        self.last_operation = (0, 0, 0, 0)
        self.solution = []
        print('Initialized: %d human, %d cat, %d chick, %d rice, capacity: %d' % (
            human, cat, chick, rice, capacity))

    '''
    允许状态集合
    '''

    def allowStatusSet(self):
        allow_set = []
        for i in range(self.START[0] + 1):
            for j in range(self.START[1] + 1):
                for k in range(self.START[2] + 1):
                    for l in range(self.START[3] + 1):
                        if i >= 1 or not (k >= 1 and (l >= 1 or j >= 1)):
                            allow_set.append((i, j, k, l))
        return allow_set

    '''
    允许决策集合
    '''

    def allowMethods(self):
        allow_methods = []
        for i in range(self.START[0] + 1):
            for j in range(self.START[1] + 1):
                for k in range(self.START[2] + 1):
                    for l in range(self.START[3] + 1):
                        if i >= 1 and (i + j + k + l) <= self.CAPACITY:
                            allow_methods.append((i, j, k, l))
        return allow_methods

    '''
    可采用策略集合
    格式：method
    '''

    def availableMethods(self, currant, flag):
        available_methods = self.allowMethods()
        for a, b, method in self.forbiden_methods:
            if a == currant and b == flag:
                if method in available_methods:
                    available_methods.remove(method)
        if self.last_operation in available_methods:
            available_methods.remove(self.last_operation)
        return available_methods

    '''
    禁止使用策略集合
    格式：currant, flag, method 目前情况+操作
    （禁止直接原路返回）
    '''

    def forbidenMethods(self, currant, flag, method):
        if (currant, flag, method) not in self.forbiden_methods:    # 禁用已经尝试的失败方案
            self.forbiden_methods.append((currant, flag, method))
            # print(self.forbiden_methods)

    '''
    上船过河
    @return tuple 两岸情形
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
    是否有将已进行的失败案例禁用的必要？ 有
    '''

    def solve(self):
        allow_set = self.allowStatusSet()
        while self.here != (0, 0, 0, 0):
            self.here = self.START
            self.there = (0, 0, 0, 0)
            self.last_operation = (0, 0, 0, 0)
            self.solution = []
            count = 1
            while self.here != (0, 0, 0, 0):
                available_methods = self.availableMethods(self.here, count % 2)
                if available_methods == []:
                    break
                # print(len(available_methods))
                method = available_methods[randint(
                    0, len(available_methods) - 1)]
                # print(method)
                temp = self.goBoard(method, count % 2, self.here, self.there)
                # print(temp)
                if temp[0] in allow_set and temp[1] in allow_set:
                    self.here = temp[0]
                    self.there = temp[1]
                    # print(self.here)
                    # print('%d 个人，%d 只猫，%d 只鸡，%d 米，在第%d 次渡河的船上' %
                    # (method[0], method[1], method[2], method[3], count))
                    self.solution.append((method, count))
                    self.last_operation = method
                    # print('last operation here', self.last_operation)
                    count += 1
                else:
                    self.forbidenMethods(self.here, count % 2, method)


def main():
    bank = Bank(1, 1, 1, 1, 2)

    allow_set = bank.allowStatusSet()
    print("允许状态集合：")
    print(allow_set)

    allow_actions_set = bank.allowMethods()
    print("允许决策集合：")
    print(allow_actions_set)

    bank.solve()
    for method in bank.solution:
        print('%d 个人，%d 只猫，%d 只鸡，%d 米，在第%d 次渡河的船上' %
              (method[0][0], method[0][1], method[0][2], method[0][3], method[1]))


main()
