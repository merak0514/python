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
            'origin': 'https://www.icourse163.org',
        }
        self.username = ''
        self.passwd = ''
        self.savelogin = True
        self.host = 'https://www.icourse163.org/passport/reg/icourseLogin.do'
        self.cookies = ''

    def set(self, usn, psd, savelogin=True):
        self.username = usn
        self.passwd = psd
        self.savelogin = savelogin

    def login(self, usn, psd, savelogin=True):
        self.set(usn, psd, savelogin)
        data = {
            'username': self.username,
            'passwd': self.passwd,
            'savelogin': self.savelogin,
        }
        req = requests.post(self.host, data=data)
        self.cookies = req.cookies
        print(self.cookies)

    def get_cookies(self):
        return self.cookies


if __name__ == '__main__':
    login = Login()
    login.login('phx001@163.com', 'a123123')
