# 问题： 三名商人各带一个随从过河，一只小船只能容纳两个人，随从们约定，只要在河的任何一岸，一旦随从人数多于商人人数就杀人越货，但是商人们知道了他们的约定，并且如何过河的大权掌握在商人们手中，商人们该采取怎样的策略才能安全过河呢？ # noqa

# 创建允许状态集合

from random import randint


class Boat(object):
    """商人过河"""

    def __init__(self, merchants, minors, capacity):
        # super(Boat, self).__init__()
        self.merchants = merchants
        self.minors = minors
        self.capacity = capacity
        self.used_method = []

        print('Initialized:', merchants, 'merchants and',
              minors, 'minors; capacity:', capacity)

    '''allowset'''

    def allowSet(self):
        allowset = []
        for merchants_here in range(self.merchants + 1):
            for minors_here in range(self.minors + 1):
                # print([merchants_here, minors_here])
                if merchants_here == 0 or merchants_here == self.merchants:
                    allowset.append((merchants_here, minors_here))
                elif merchants_here >= minors_here and (self.merchants -
                                                        merchants_here) >= (self.minors - minors_here):
                    allowset.append((merchants_here, minors_here))
        return allowset

    '''allow_action'''

    def allowAction(self):
        allow_action = []
        for merchant_num in range(self.capacity + 1):
            for minor_num in range(self.capacity + 1 - merchant_num):
                if minor_num + merchant_num != 0:
                    allow_action.append((merchant_num, minor_num))
        return allow_action

    def usedMethod(self, current, flag, move):
        self.used_method.append((current, flag, move))
        print("used_method:", self.used_method)

    def avaliableMethod(self, current, flag):
        allow_action_set = self.allowAction()
        # print('input current aM:', current)
        for a, b, move in self.used_method:
            # print(current, move)
            if a == current and b == flag:
                allow_action_set.remove(move)
        print('allow_action_set aM:', allow_action_set)
        return allow_action_set

    '''solution'''

    def solve(self):
        allowset = self.allowSet()
        # print(allowset,'hhhhhhh')
        current = (self.merchants, self.minors)
        # print(current)
        count = 1  # 第n次渡船
        while current != (0, 0):
            allow_action_set = self.avaliableMethod(current, count % 2)

            move = allow_action_set[randint(
                0, len(allow_action_set) - 1)]  # 随机采用一种行动方式
            # self.usedMethod(current, count % 2, move)
            print(move)
            temp = (current[0] + ((-1) ** count) * move[0],
                    current[1] + ((-1) ** count) * move[1])
            print(temp)
            if temp in allowset:
                current = temp
                print('%d 个商人，%d 个随从，在第%d 次渡河的船上' % (move[0], move[1], count))
                count += 1
            else:
                self.usedMethod(current, count % 2, move)


'''主方法'''


def main():
    boat = Boat(3, 3, 2)
    allowset = boat.allowSet()
    print("允许状态集合：")
    print(allowset)

    allow_action_set = boat.allowAction()
    print("允许决策集合：")
    print(allow_action_set)

    boat.solve()


main()
