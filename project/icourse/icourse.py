# !/user/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 19:19
# @Author   : Merak
# @File     : icourse.py
# @Software : PyCharm
"""
地址格式: https://www.icourse163.org/learn/+[school]-[course_id]?tid=[term_id]
e.g.: https://www.icourse163.org/learn/XJTU-1001756006?tid=1002649017
资源格式: https://www.icourse163.org/learn/+[school]-[course_id]?tid=[term_id]#/learn/content?\
        type=detail&id=[unit_id]&cid=[source_id]
e.g.: https://www.icourse163.org/learn/XJTU-1001756006?tid=1002649017#/learn/content?\
        type=detail&id=1003627038&cid=1004311624
在dwr中表示为: lesson_id, id
获得目录：[POST] CourseBean.getMocTermDto.dwr
获得下载链接：[POST] CourseBean.getLessonUnitLearnVo.dwr
下载：[GET]
"""
import time
import requests
from bs4 import BeautifulSoup as Bs
import re

local_address = 'download/'
school_id = 'XJTU'
course_id = '1001756006'
tid = '1002649017'  # term id


def test(link):
    html = requests.get(link)
    print(html)
    text = html.text
    soup = Bs(text, 'html.parser')
    url_set = soup('a')
    new_url_set = [u.get('href', None) for u in url_set]
    for u in url_set:
        print(u)


def get_headers():
    headers = {
        'Host': 'www.icourse163.org',
        'Connection': 'keep-alive',
        'Content-Length': '280',
        'Origin': 'https://www.icourse163.org',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
                      '(KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
        'DNT': '1',
        'Content-Type': 'text/plain',
        'Accept': '*/*',
        'Referer': 'https://www.icourse163.org/learn/' + school_id + '-' + course_id + '?tid=' + tid,
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
    }
    return headers


def get_catalogue():
    """
    得到目录列表
    :return: catalogue
    """
    catalogue = []
    host = 'https://www.icourse163.org/dwr/call/plaincall/CourseBean.getMocTermDto.dwr'
    headers = get_headers()
    batch_id = round(time.time() * 1000)
    data = {
        'callCount': 1,
        'scriptSessionId': '${scriptSessionId}190',
        'httpSessionId': '5f5c7b6b5448441c9a615b84593a4c6f',
        'c0-scriptName': 'CourseBean',
        'c0-methodName': 'getMocTermDto',
        'c0-id': 0,
        'c0-param0': 'number: ' + tid,
        'c0-param1': 'number: 0',
        'c0-param2': 'boolean: true',
        'batchId': batch_id,
    }
    req = requests.post(host, headers=headers, data=data)
    content = req.text
    split = content.split('\n')
    for i in range(4, len(split) - 1):
        if re.findall('s[0-9]{2}\.contentType=3;', i):
            lesson_id = re.findall('s[0-9]{2}\.id=')
    print(split)
    return catalogue


def download(info):
    """
    下载单个pdf文件
    :param info: dictionary pdf对应的代码
    :return:
    """
    pdf_id = info['pdf_id']
    lesson_id = info['lesson_id']
    batch_id = round(time.time() * 1000)
    host = 'https://www.icourse163.org/dwr/call/plaincall/CourseBean.getLessonUnitLearnVo.dwr'
    headers = get_headers()
    data = {
        'callCount': 1,
        'scriptSessionId': '${scriptSessionId}190',
        'httpSessionId': 'fd621056c8464bc3bc4bf24ced87737e',
        'c0-scriptName': 'CourseBean',
        'c0-methodName': 'getLessonUnitLearnVo',
        'c0-id': 0,
        'c0-param0': 'number: ' + pdf_id,
        'c0-param1': 'number: 3',
        'c0-param2': 'number: 0',
        'c0-param3': 'number: ' + lesson_id,
        'batchId': batch_id,
    }
    req = requests.post(host, headers=headers, data=data)
    content = req.text
    download_address = re.findall('textOrigUrl:\"(.+)\"', content)[0]
    print(download_address)
    try:
        pdf = requests.get(download_address)
        with open(local_address + 'test2' + '.pdf', 'wb') as file:
            file.write(pdf.content)
    except OSError:
        print('读写失败！')
        return 1
    return 0


if __name__ == '__main__':

    url = 'https://www.icourse163.org/' \
          'learn/XJTU-1001756006?tid=1002649017'
    # test(url)
    get_catalogue()
    # download('1004576030')
