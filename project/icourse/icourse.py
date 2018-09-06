# !/user/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 19:19
# @Author   : Merak
# @File     : icourse.py
# @Software : PyCharm
"""
地址格式: https://www.icourse163.org/learn/+[school]-[course_id]?tid=[term_id]
e.g.: https://www.icourse163.org/learn/XJTU-1001756006?tid=1002649017
"""
import time
import requests
from bs4 import BeautifulSoup as Bs
import re

local_address = "download/"


def test(link):
    html = requests.get(link)
    print(html)
    text = html.text
    soup = Bs(text, 'html.parser')
    url_set = soup('a')
    new_url_set = [u.get('href', None) for u in url_set]
    for u in url_set:
        print(u)


def get():
    pass


def download(link):
    """
    下载单个pdf文件
    :param link: str
    :return:
    """
    batch_id = round(time.time() * 1000)
    download_host = "https://www.icourse163.org/dwr/call/plaincall/CourseBean.getLessonUnitLearnVo.dwr"
    headers = {
        "Host": "www.icourse163.org",
        "Connection": "keep-alive",
        "Content-Length": "280",
        "Origin": "https://www.icourse163.org",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 "
                      "(KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
        "DNT": "1",
        "Content-Type": "text/plain",
        "Accept": "*/*",
        "Referer": "https://www.icourse163.org/learn/XJTU-1001756006?tid=1002649017",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9",
    }
    data = {
        "callCount": 1,
        "scriptSessionId": "${scriptSessionId}190",
        "httpSessionId": "fd621056c8464bc3bc4bf24ced87737e",
        "c0-scriptName": "CourseBean",
        "c0-methodName": "getLessonUnitLearnVo",
        "c0-id": 0,
        "c0-param0": "number: 1004700192",
        "c0-param1": "number: 3",
        "c0-param2": "number: 0",
        "c0-param3": "number: 1004311624",
        "batchId": batch_id,
    }
    a = requests.post(download_host, headers=headers, data=data)
    content = a.text
    download_address = re.findall('textOrigUrl:\"(.+)\"', content)[0]
    print(download_address)
    try:
        pdf = requests.get(download_address)
        with open(local_address + "test" + ".pdf", "wb") as file:
            file.write(pdf.content)
    except:
        print('Wrong!')


if __name__ == '__main__':

    url = "https://www.icourse163.org/" \
          "learn/XJTU-1001756006?tid=1002649017"
    # test(url)
    school_id = 'XJTU'

    download(1)
