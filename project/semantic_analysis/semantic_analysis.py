# !/user/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 10:05
# @Author   : Merak
# @File     : semantic_analysis.py
# @Software : PyCharm

import jieba
import jieba.posseg as pseg
from collections import defaultdict

jieba.load_userdict('dict.txt')
try:
    fhand = open("釜山行.txt", 'r', encoding="utf-8")
except:
    print("No such file")
    quit()

print(fhand)
for line in fhand:
    words = pseg.cut(line)
    print(pseg)
