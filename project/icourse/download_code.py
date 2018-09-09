# !/user/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 11:46
# @Author   : Merak
# @File     : download_code.py
# @Software : PyCharm
"""
nickName字段获得名字
score字段获得分数
答卷格式：http://www.icourse163.org/learn/XJTU-[course_id]?tid=[term_id]#/learn/ojhw?id=[test_id/tid]&aid=[answer_id/aid]
getOJQuizPaperDto.dwr
c++: ojLanguage = 2
"""
import re


def get_nickname():
    file = open('data/getStudentScoreByTestId.dwr')
    for line in file:
        nick_name = re.findall('nickName="(.+?)"', line)
        if nick_name:
            print(nick_name[0].encode().decode('unicode_escape'))


get_nickname()
