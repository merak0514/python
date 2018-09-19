# !/user/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 10:52
# @Author   : Merak
# @File     : AutoDownloader.py
# @Software : PyCharm


class AutoDownloader(object):
    """
    根据得到的学生信息、测试信息向
    http://www.icourse163.org/dwr/call/plaincall/YocOJQuizBean.adminGetOjQuestionSubmitRecords.dwr
    http://www.icourse163.org/dwr/call/plaincall/YocOJQuizBean.getOJPaperDto.dwr
    发请求，得到该份测验的原始代码、分数
    """
    def __init__(self, info):
        self.username = info['username']
        self.passwd = info['passwd']
        self.cookies = info['cookies']
        self.headers = info['headers']
        self.stu_info = info['stu_info']
        self.term = info['term']
        self.download_path = "H:/data/"


