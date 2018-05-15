# !/merak/desktop/python/
# @Time     : 20:30
# @Author   : Merak
# @File     : test2.py
# @Software : PyCharm

from collections import defaultdict
line = '+' + ('------+' * 5)
separator = defaultdict(lambda: line)
print(separator[10])
print(separator)
