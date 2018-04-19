# 问题： 三名商人各带一个随从过河，一只小船只能容纳两个人，随从们约定，只要在河的任何一岸，一旦随从人数多于商人人数就杀人越货，但是商人们知道了他们的约定，并且如何过河的大权掌握在商人们手中，商人们该采取怎样的策略才能安全过河呢？ # noqa

from random import randint


class Boat(object):
    """商人过河"""

    def __init__(self, merchants, minors, capacity):
        '''
        分别为：原始岸边商人的数量、随从的数量；船的容纳量；禁止使用的策略;上一次执行的策略
        '''
        # super(Boat, self).__init__()
        self.merchants = merchants
        self.minors = minors
        self.capacity = capacity
        self.forbid_methods = []
        self.used_methods = []
        self.last_operator = (0, 0)

        print('Initialized:', merchants, 'merchants and',
              minors, 'minors; capacity:', capacity)

    '''
    允许状态集合：满足两个岸边商人数量为0或者商人数量大于随从数量
    @return dict
    '''

    def allowSet(self):
        allow_set = []
        for i in range(self.merchants + 1):
            for j in range(self.minors + 1):
                # print([i, j])
                if i == 0 or i == self.merchants:
                    allow_set.append((i, j))
                elif i >= j and (self.merchants -
                                 i) >= (self.minors - j):
                    allow_set.append((i, j))
        return allow_set

    '''
    允许决策集合：所有符合船最大容纳量的策略
    @return dict
    '''

    def allowActions(self):
        allow_actions = []
        for merchant_num in range(self.capacity + 1):
            for minor_num in range(self.capacity + 1 - merchant_num):
                if minor_num + merchant_num != 0:
                    allow_actions.append((merchant_num, minor_num))
        return allow_actions

    '''
    使用过的决策集合：包括在任意一点向任意方向（此岸/对岸）决策的集合
    flag为方向：1.正向（奇数）2.逆向（偶数）
    '''

    def usedMethods(self, current, flag, method):
        self.used_methods.append((current, flag, method))

    '''
    成环后避免再次经过
    检验目前的点是否已经经过？若经过，则检验使用过的决策表，将在此点已经
    有点奇怪，检验成环并排除很复杂
    `未完成`
    '''

    def noCircle(self, current):
        pass

    '''
    禁止使用的决策集合：对允许决策进一步削弱，禁止在特定点使用特定决策
    flag为方向：1.正向（奇数）2.逆向（偶数）
    '''

    def forbidMethods(self, current, flag, method):
        self.forbid_methods.append((current, flag, method))
        # print("forbid_methods:", self.forbid_methods)

    '''
    结合船的限制与禁止表得到的针对特定点的允许策略集合
    @return dict
    '''

    def avaliableMethods(self, current, flag):
        allow_actions_set = self.allowActions()
        # print('input current aM:', current)
        for a, b, method in self.forbid_methods:
            # print(current, method)
            if a == current and b == flag:
                allow_actions_set.remove(method)
        # print('allow_actions_set aM:', allow_actions_set)
        return allow_actions_set

    '''solution'''

    def solve(self):
        allow_set = self.allowSet()
        # print(allow_set,'hhhhhhh')
        current = (self.merchants, self.minors)
        # print(current)
        count = 1  # 第n次渡船
        while current != (0, 0):
            allow_actions_set = self.avaliableMethods(
                current, count % 2)   # 允许采用的方法
            method = allow_actions_set[randint(
                0, len(allow_actions_set) - 1)]  # 随机采用一种行动方式
            if method != (self.last_operator[1], self.last_operator[0]):   # 禁止直接原路返回
                # self.usedMethods(current, count % 2, method)
                # print(method)
                temp = (current[0] + ((-1) ** count) * method[0],
                        current[1] + ((-1) ** count) * method[1])   # 尝试执行
                # print(temp)
                if temp in allow_set:    # 若尝试执行后结果在允许的状态表中，则实际执行
                    current = temp
                    print('%d 个商人，%d 个随从，在第%d 次渡河的船上' %
                          (method[0], method[1], count))
                    count += 1
                    self.last_operator = method
                else:
                    self.forbidMethods(current, count % 2, method)


'''主方法'''


def main():
    boat = Boat(3, 3, 2)
    allow_set = boat.allowSet()
    print("允许状态集合：")
    print(allow_set)

    allow_actions_set = boat.allowActions()
    print("允许决策集合：")
    print(allow_actions_set)

    boat.solve()


main()
