# !/user/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 11:46
# @Author   : Merak
# @File     : download_code.py
# @Software : PyCharm
"""
score字段获得分数
答卷格式：http://www.icourse163.org/learn/XJTU-[course_id]?tid=[term_id]#/learn/ojhw?id=[test_id/tid]&aid=[answer_id/aid]
getOJQuizPaperDto.dwr
c++: ojLanguage = 2
单元测试：type=2
oj测试：type=7
"""
from __future__ import unicode_literals
import re
import Login
import time
import requests
import json



def batch_id():
    return round(time.time() * 1000)


def get_account():
    """
    读取account文件得到用户名密码
    :return: json
    :rtype: dict
    """
    with open('data/account.json') as file:
        js = json.load(file)
    return js


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
        self.oj_set = []
        self.test_set = []

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
        # print(req.text)
        split = req.text.split('\n')

        for line in split:
            if line.startswith('s'):
                term = {
                    'term': re.findall('s([0-9]+)\.', line)[0],
                    'term_id': re.findall('s[0-9]+\.termId=([0-9]+)', line)[0],
                }
                self.terms.append(term)
        # print(self.terms)
        return 0

    def get_moc_data(self, term):
        """
        根据输入的学期查询所有的练习
        :param term: 第几学期
        :type term: int
        :return: req.text if success else 1
        """
        term_id = self.terms[term-1]['term_id'] if int(self.terms[term-1]['term']) == int(term) else -1
        if term_id == -1:
            print('terms没有按照顺序！')
            return 1
        print(term_id)
        host = 'http://www.icourse163.org/dwr/call/plaincall/MocScoreManagerBean.getMocTermDataStatisticDto.dwr'
        data = {
            'callCount': '1',
            'scriptSessionId': '${scriptSessionId}190',
            'c0-scriptName': 'MocScoreManagerBean',
            'c0-methodName': 'getMocTermDataStatisticDto',
            'c0-id': 0,
            'c0-param0': 'string: ' + term_id,
            'batchId': batch_id()
        }
        req = requests.post(host, headers=self.headers, data=data, cookies=self.cookies)
        c = re.compile('description=.*?;')

        o = re.sub(c, '', req.text)
        content = o.encode().decode('unicode_escape')  # 转换为中文
        m = re.sub(c, '', content)
        print(o)
        with open('data/tempGetMocTermDataStatisticDto.dwr', 'wb') as file:
            file.write(content.encode('utf-8'))
            file.close()
        file = open('data/tempGetMocTermDataStatisticDto.dwr', 'rb')
        # print(file)
        for line in file:
            content = line.decode('utf-8')
            # print(content)
            if re.findall('type=7', content) and re.findall('name=', content):
                print(content)
                oj_info = {
                    'name': re.findall('name="(.+)"', content)[0],
                    'id': re.findall('id=(.+?);', content)[0] if re.findall('id=(.+?);', content)[0] else '-1',
                    'chapterId': re.findall('chapterId=(.+?);', content)[0],
                    'avgScore': re.findall('avgScore=(.+?);', content)[0],
                    'releaseTime': re.findall('releaseTime=(.+?);', content)[0],
                    'deadline': re.findall('deadline=(.+?);', content)[0],
                    'evaluateScoreReleaseTime': re.findall('evaluateScoreReleaseTime=.+;', content)[0],
                    'sbjTotalScore': re.findall('sbjTotalScore=(.+?);', content)[0],
                    'termId': re.findall('termId=(.+?);', content)[0],
                    'submitTestCount': re.findall('submitTestCount=(.+?);', content)[0],
                    'type': 7,
                }
                self.oj_set.append(oj_info)
            if re.findall('type=2', content) and re.findall('name=', content):
                print(content)
                test_info = {
                    'name': re.findall('name="(.+)"', content)[0],
                    'id': re.findall('id=(.+?);', content)[0],
                    'chapterId': re.findall('chapterId=(.+?);', content)[0],
                    'avgScore': re.findall('avgScore=(.+?);', content)[0],
                    'releaseTime': re.findall('releaseTime=(.+?);', content)[0],
                    'deadline': re.findall('deadline=(.+?);', content)[0],
                    'evaluateScoreReleaseTime': re.findall('evaluateScoreReleaseTime=(.+?);', content)[0],
                    'ojTotalScore': re.findall('sbjTotalScore=(.+?);', content)[0],
                    'termId': re.findall('termId=(.+?);', content)[0],
                    'submitTestCount': re.findall('submitTestCount=(.+?);', content)[0],
                    'testRandomSetting': re.findall('testRandomSetting=(.+)', content)[0],
                    'type': 2,

                }
                self.test_set.append(test_info)
        print(self.oj_set)
        print(self.test_set)


if __name__ == '__main__':

    account_info = get_account()
    download = DownloadCode(account_info)
    download.login()
    download.get_term_info()
    download.get_moc_data(1)
