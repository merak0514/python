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
pdf：s[number].contentType=3;
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


def test():
    """
    出现<Response [200]>即可
    :return:
    """
    link = 'https://www.icourse163.org/' \
           'learn/XJTU-1001756006?tid=1002649017'
    html = requests.get(link)
    print(html)
    text = html.text
    soup = Bs(text, 'html.parser')
    url_set = soup('a')
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
    catalog = []
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
    try:
        req = requests.post(host, headers=headers, data=data)
    except requests.exceptions.ConnectionError:
        print('Connection error!')
        exit(1)
    content = req.text
    split = content.split('\n')
    for i in range(4, len(split) - 1):
        information = split[i]
        if re.findall('s[0-9]{2}\.contentType=3;', information):
            lesson_id = re.findall('s[0-9]+\.id=([0-9]+)', information)[0]
            pdf_id = re.findall('s[0-9]+\.contentId=([0-9]+)', information)[0]
            pdf_name = re.findall('s[0-9]+\.name="(.+)";', information)[0].encode().decode('unicode_escape')
            temp = {
                'lesson_id': lesson_id,
                'pdf_id': pdf_id,
                'name': pdf_name,
            }
            catalog.append(temp)
    print(catalog)
    return catalog


def download(info):
    """
    下载单个pdf文件
    :param info: dictionary pdf对应的代码
    :return:
    """
    pdf_id = info['pdf_id']
    lesson_id = info['lesson_id']
    name = info['name']
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
    try:
        pdf = requests.get(download_address)
        with open(local_address + name + '.pdf', 'wb') as file:
            file.write(pdf.content)
    except OSError:
        print('读写失败！')
        return 1
    return 0


def download_all():
    """
    下载所有的pdf文件
    :return: 1: 用户取消下载/下载失败; 0: 成功
    """
    catalog = get_catalogue()
    downloading = 1
    while True:
        confirm = input('确定要开始下载【所有】的共{}份pdf文件吗(Y/N)？'.format(len(catalog)))
        if confirm is 'n' or confirm is 'N':
            print('取消下载')
            return 1
        elif confirm is 'y' or confirm is 'Y':
            break
        else:
            print('输入有误')
    for i in catalog:
        print('正在下载第{}份pdf'.format(downloading))
        if download(i) == 1:
            print('第{}份pdf下载失败'.format(downloading))
        downloading += 1
    print('下载完成')


if __name__ == '__main__':

    test()
    download_all()
