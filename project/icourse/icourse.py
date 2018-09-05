# !/user/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 19:19
# @Author   : Merak
# @File     : icourse.py
# @Software : PyCharm
import requests
from bs4 import BeautifulSoup as Bs


def test(link):
    html = requests.get(link)
    print(html)
    text = html.text
    soup = Bs(text, 'html.parser')
    url_set = soup('a')
    new_url_set = [u.get('href', None) for u in url_set]
    for u in url_set:
        print(u)


if __name__ == '__main__':

    url = "https://www.icourse163.org/" \
          "learn/XJTU-1001756006?tid=1002649017#/learn/content"
    # test(url)
