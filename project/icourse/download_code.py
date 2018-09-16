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
import Login
import time
import requests
import json
import os
import random_ua
import GetData
import random
import ModuleIcourse


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


def new_folder(folder_path):
    if not os.path.exists(folder_path):
        try:
            os.makedirs(folder_path)
        except FileNotFoundError:
            input('系统找不到指定的路径。' + folder_path)
            return 1
        else:
            print('{} created'.format(folder_path))
            return 0
    else:
        print('{} existed'.format(folder_path))


class DownloadCode(object):
    def __init__(self, account):
        self.ua = random_ua.UserAgent()
        self.username = account['username']
        self.passwd = account['passwd']
        self.is_login = 0
        self.cookies = ''
        self.headers = {
            # 'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:22.0) Gecko/20100101 Firefox/22.0',
            # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 \
            #             #       (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
            'User-Agent': self.ua.random(),
        }
        self.terms = []
        self.oj_set = []  # OJ练习列表 其中第一项是考试
        self.test_set = []  # 单元测试列表 其中第一项是考试
        self.download_path = "H:/data/"

    def new_headers(self):
        self.headers = {
            'User-Agent': self.ua.random()
        }

    def login(self):
        """
        调用Login进行登陆
        :return: 0
        """
        login = Login.Login()
        login.login(self.username, self.passwd)
        self.cookies = login.get_cookies()
        if self.cookies:
            self.is_login = 1
        return 0

    def get_term_info(self):
        """
        得到所有的学期及其对应的term_id
        :return: 0
        """
        if not self.is_login:
            print('请先登陆')
            exit(1)
        data = GetData.get_term_info()
        host = 'https://www.icourse163.org/dwr/call/plaincall/PublishCourseBean.getTermsByTeacher.dwr'
        req = requests.post(host, headers=self.headers, data=data, cookies=self.cookies)
        self.terms = GetData.data_manage_term_info(req.text)
        print(self.terms)
        req.close()
        return 0

    def get_moc_data(self, term):
        """
        根据输入的学期查询所有的练习
        :param term: 第几学期
        :type term: int
        :return: req.text if success else 1
        """
        self.get_term_info()  # 更新学期列表
        term_id = self.terms[term-1]['term_id'] if int(self.terms[term-1]['term']) == int(term) else -1
        if term_id == -1:
            print('terms没有按照顺序！')
            return 1
        host = 'http://www.icourse163.org/dwr/call/plaincall/MocScoreManagerBean.getMocTermDataStatisticDto.dwr'
        data = GetData.get_moc_data(term_id)
        req = requests.post(host, headers=self.headers, data=data, cookies=self.cookies)
        self.oj_set, self.test_set = GetData.data_manage_ex_term(req.text)
        print('编程题', self.oj_set)
        print('客观题', self.test_set)
        req.close()
        ModuleIcourse.upload_moc_data({  # 上传数据库
            'oj_set': self.oj_set[1: len(self.oj_set)],
            'test_set': self.test_set[1: len(self.test_set)]
        })

    def get_all_test_info(self, term):
        """
        根据练习的id找到对应练习的所有的作业
        :param: term
        :type: int
        :return: oj_set
        :rtype: list
        """
        host = 'http://www.icourse163.org/dwr/call/plaincall/MocScoreManagerBean.getStudentScoresByTestId.dwr'
        page = 1
        stu_per_page = 20
        self.download_path += 'term' + str(term) + '/'
        new_folder(self.download_path)
        self.get_moc_data(term)  # 更新对应学期的课程列表

        oj_set = []
        for i in range(1, len(self.oj_set)):
            oj = self.oj_set[i]
            folder_name = oj['name']
            new_folder(self.download_path+folder_name)
            term_id = self.terms[term - 1]['term_id'] if int(self.terms[term - 1]['term']) == int(term) else -1
            if term_id == -1:
                print('terms没有按照顺序！')
                return 1

            data = GetData.get_oj_by_oj_id(oj['id'], page, stu_per_page)
            req = requests.post(host, headers=self.headers, data=data, cookies=self.cookies)
            # 数据处理
            oj_stu_set = GetData.data_manage_oj_stu(req.text)
            print(oj_stu_set)
            print(len(oj_stu_set))
            oj_set.append(oj_stu_set)
            req.close()
            time.sleep(random.randint(1, 10) / 5)
        return oj_set

    def download(self, term, oj_stu_id):
        """
        :param term:
        :type term: int
        :param oj_stu_id:
        :type oj_stu_id: complex
        :return:
        :rtype:
        """
        host = 'http://www.icourse163.org/dwr/call/plaincall/YocOJQuizBean.getOJPaperDto.dwr'
        data = GetData.get_download_data(term, oj_stu_id)
        req = requests.post(host, headers=self.headers, data=data, cookies=self.cookies)
        # print(req.text)

    def auto_download(self):
        term = 1
        oj_set = self.get_all_test_info(term)  # 得到该学期所有的oj测试
        print(oj_set)
        for oj_stu_set in oj_set:
            for oj_stu in oj_stu_set:
                self.download(term, oj_stu['id'])
                break
            break





if __name__ == '__main__':
    #
    account_info = get_account()
    download = DownloadCode(account_info)
    download.login()
    download.auto_download()
