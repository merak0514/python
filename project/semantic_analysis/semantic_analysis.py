# !/user/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 10:05
# @Author   : Merak
# @File     : semantic_analysis.py
# @Software : PyCharm

import jieba
import jieba.posseg as pseg
from collections import defaultdict
name_set = list()  # 所有的名字集合
name_freq = defaultdict(lambda: 0)  # 所有名字的出现频率（默认为0）
# connection = [[0 for i in range(50)] for j in range(50)]  # 名字与名字间的联系
connection = defaultdict(lambda: defaultdict(lambda: 0))
jieba.load_userdict('dict.txt')
try:
    fhand = open("釜山行.txt", 'r', encoding="utf-8")
except:
    print("No such file")
    quit()

print(fhand)
for line in fhand:
    words = list(pseg.cut(line))
    names = list(word.word for word in words if word.flag == 'nr')
    for name in names:  # 把名字加入名字总集合；把名字出现频率加入
        name_freq[name] += 1
        if name not in name_set:
            name_set.append(name)
    for name1 in names:  # 寻找名字之间的关联
        for name2 in names:
            if name1 == name2:
                continue
            connection[name1][name2] += 1
for k, v in name_freq.items():
    print(k, v)

name_freq = sorted([(v, k) for (k, v) in name_freq.items()], reverse=True)
name_freq = [(k, v) for (v, k) in name_freq]  # 至此，得到人名出现频率的分布

count = 0
for name, freq in name_freq:
    print(name, freq)
    count += 1
print(connection)
