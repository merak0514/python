# !/user/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 13:10
# @Author   : Merak
# @File     : select.py
# @Software : PyCharm
import xlrd
import re
from collections import defaultdict
from requests import post
import time

data = xlrd.open_workbook('club_info.xls')
table = data.sheets()[0]
name_columns = table.col_values(1)
info_columns = table.col_values(4)
all = zip(name_columns, info_columns)
info = defaultdict(lambda: 0)
# url = "https://guide.tiaozhan.com/api/v1.0/personal/qqgroup"
nothing = 0
nothing2 = 0
for row in all:
    qq = re.findall('群.+?([0-9]+)', row[1])
    email = re.findall('邮箱.+?([0-9]+)', row[1])
    # if not qq:
    #     nothing += 1
    #     temp = {'email': email}
    # elif not email:
    #     temp = {'qq': qq}
    #     nothing2 += 1
    # else:
    #     temp = {'qq': qq, 'email': email}
    # info[row[0]] = temp
    if qq:
        info[row[0]] = qq[0]
        nothing += 1
        # temp = {
        #     'code': 'wx12afe63d2e',
        #     'name': row[0],
        #     'qq': qq
        # }
        # r = post(url, data=temp)
        # print(r)
        # time.sleep(0.1)
print(info)
print(nothing, nothing2)
