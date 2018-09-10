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
import Login
import time
import requests


def batch_id():
    return round(time.time() * 1000)


class DownloadCode(object):
    def __init__(self, account):
        self.username = account['username']
        self.passwd = account['passwd']
        self.cookies = ''
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 \
                      (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
            'origin': 'https://www.icourse163.org',
        }
        self.terms = []

    def login(self):
        """
        调用Login进行登陆
        :return: 0
        """
        login = Login.Login()
        login.login(self.username, self.passwd)
        self.cookies = login.get_cookies()
        return 0

    def get_term_info(self):
        """
        得到所有的学期及其对应的term_id
        :return: 0
        """
        if not self.cookies:
            print('请先登陆')
            return 1
        data = {
            'callCount': '1',
            'scriptSessionId': '${scriptSessionId}190',
            'c0-scriptName': 'PublishCourseBean',
            'c0-methodName': 'getTermsByTeacher',
            'c0-id': 0,
            'c0-param0': 'number:2',
            'batchId': batch_id()
        }
        host = 'https://www.icourse163.org/dwr/call/plaincall/PublishCourseBean.getTermsByTeacher.dwr'
        req = requests.post(host, headers=self.headers, data=data, cookies=self.cookies)
        print(req.text)
        split = req.text.split('\n')

        for line in split:
            if line.startswith('s'):
                term = {
                    'term': re.findall('s([0-9]+)\.', line)[0],
                    'term_id': re.findall('s[0-9]+\.termId=([0-9]+)', line)[0],
                }
                self.terms.append(term)
        print(self.terms)
        return 0


if __name__ == '__main__':

    account_info = {
        'username': input('username: '),
        'passwd': input('passwd: ')
    }
    download = DownloadCode(account_info)
    download.login()
    download.get_term_info()
