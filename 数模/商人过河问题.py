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

    def allowset(self):
        allowset = []
        for merchants_here in range(self.merchants + 1):
            for minors_here in range(self.minors + 1):
                # print([merchants_here, minors_here])
                if merchants_here == 0 or merchants_here == self.merchants:
                    allowset.append([merchants_here, minors_here])
                elif merchants_here >= minors_here and (self.merchants -
                                                        merchants_here) >= (self.minors - minors_here):
                    allowset.append([merchants_here, minors_here])
        return allowset

    '''allowaction'''

    def allowaction(self):
        allowaction = []
        for merchant_num in range(self.capacity + 1):
            for minor_num in range(self.capacity + 1 - merchant_num):
                if minor_num + merchant_num != 0:
                    allowaction.append([merchant_num, minor_num])
        return allowaction

    '''solution'''

    def solve(self, allowset, allowactionset):
        # method = 1  # 方法数
        current = [self.merchants, self.minors]
        # print(current)
        count = 1  # 第n次渡船
        while current != [0, 0]:
            move = allowactionset[randint(
                0, len(allowactionset) - 1)]  # 随机采用一种行动方式
            # print(move)
            temp = [current[0] + ((-1) ** count) * move[0],
                    current[1] + ((-1) ** count) * move[1]]
            # print(temp)
            if temp in allowset:
                current = temp
                print('%d 个商人，%d 个随从，在第%d 次渡河的船上' % (move[0], move[1], count))
                count += 1

    def usedMethod(self, current, move):
        self.used_method.append([current, move])

    def avaliableMethod(self):
        pass


'''主方法'''


def main():
    boat = Boat(3, 3, 2)
    allowset = boat.allowset()
    print("允许状态集合：")
    print(allowset)

    allowactionset = boat.allowaction()
    print("允许决策集合：")
    print(allowactionset)

    boat.solve(allowset, allowactionset)


main()
