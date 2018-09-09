# !/user/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 10:01
# @Author   : Merak
# @File     : login.py
# @Software : PyCharm
import requests


class Login:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 \
                      (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
            'Referer': 'https://www.icourse163.org/member/login.htm',
            'origin': 'https://www.icourse163.org',
        }
        self.username = ''
        self.passwd = ''
        self.savelogin = True
        self.host = 'https://www.icourse163.org/passport/reg/icourseLogin.do'

    def set(self):
        self.username = 'phx001@163.com'
        self.passwd = 'a123123'

    def login(self):
        self.set()
        data = {
            'username': self.username,
            'passwd': self.passwd,
            'savelogin': self.savelogin,
        }
        req = requests.post(self.host, data=data)
        jar = req.cookies


if __name__ == '__main__':
    login = Login()
    login.login()
