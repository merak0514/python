# !/user/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 22:50
# @From     : http://www.adamyt.com/blog/20170323-getMOOCpdf/
# @File     : original.py
# @Software : PyCharm

import requests, time, re, os

###以下三项用户自填。直接打开课程网页，在地址栏获取两个id
schoolId = 'BIT-1001870001'  ##学校id
termId = '1001962001'  ##课程id
saveDir = 'F://MOOC/Python网络爬虫/'  ##保存目录
Referer = 'http://www.icourse163.org/learn/' + schoolId + '?tid=' + termId
scriptSessionId = '${scriptSessionId}190'
httpSessionId = 'c885dc4a57f643c080021ffa63ccecc4'
batchId = round(time.time() * 1000)  # 毫秒级unix时间戳
headers = {'Host': 'www.icourse163.org',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
           'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
           'Accept-Encoding': 'gzip, deflate',
           'Content-Type': 'text/plain',
           'Referer': Referer,
           'Connection': 'keep-alive'}
dataGetMocTermDto = {'callCount': '1',
                     'scriptSessionId': scriptSessionId,
                     'httpSessionId': httpSessionId,
                     'c0-scriptName': 'CourseBean',
                     'c0-methodName': 'getMocTermDto',  # 获取目录
                     'c0-id': '0',
                     'c0-param0': 'number:' + termId,  # tid
                     'c0-param1': 'number:1',
                     'c0-param2': 'boolean:true',
                     'batchId': batchId, }
dataGetLessonUnitLearnVo = {'callCount': '1',
                            'scriptSessionId': scriptSessionId,
                            'httpSessionId': httpSessionId,
                            'c0-scriptName': 'CourseBean',
                            'c0-methodName': 'getLessonUnitLearnVo',
                            'c0-id': '0',
                            'c0-param0': 'number:805080',  # contentId
                            'c0-param1': 'number:3',  # type=3代表文档  type=1代表视频
                            'c0-param2': 'number:0',
                            'c0-param3': 'number:1002834377',  # id
                            'batchId': batchId}


def getMocTermDto():  # 获取总体目录
    urlGetMocTermDto = 'http://www.icourse163.org/dwr/call/plaincall/CourseBean.getMocTermDto.dwr'
    try:
        res = requests.post(urlGetMocTermDto, headers=headers, data=dataGetMocTermDto)
        res.raise_for_status()
        re_getInfo = u'anchorQuestions=.*contentId=(\d*);.*contentType=3;.*id=(\d*);.*name="(.*)";'
        content = res.text.encode('utf-8').decode('unicode_escape')  # 原文本中的unicode字符串是以ASCII码形式存在的，所以需要重编码
        infoList = re.findall(re_getInfo, content)
        if len(infoList) == 0:
            if content.find('Session Error') != -1:
                print('哟呵，session过期咯，再去获取一次吧')
                return -1
    except:
        print('哎呀，出了点问题，可能是id输入错误，也可能是老师并没有发布课件\n')  # 比如电子科大的微积分三就没课件 惊了！还以为有BUG呢
        return -1
    return infoList


def getLessonUnitLearnVo(infoList):  # 获取该讲的文档地址
    urlGetLessonUnitLearnVo = 'http://www.icourse163.org/dwr/call/plaincall/CourseBean.getLessonUnitLearnVo.dwr'
    re_pdfUrl = r'http://nos.netease.com/.*?\.pdf'  # 匹配pdf下载链接
    if not os.path.isdir(saveDir):
        os.mkdir(saveDir)
    count = 1  # 计数
    for item in infoList:
        contendId = item[0]
        ID = item[1]
        name = item[2]
        if os.path.exists(saveDir + name + '.pdf'):  # 检查文件是否已下载过
            print(name + ' 已存在，跳过...\n')
            continue
        batchId = round(time.time() * 1000)  # 毫秒级unix时间戳
        dataGetLessonUnitLearnVo['c0-param0'] = 'number:' + contendId
        dataGetLessonUnitLearnVo['c0-param3'] = 'number:' + ID
        dataGetLessonUnitLearnVo['batchId'] = batchId
        try:
            eachRes = requests.post(urlGetLessonUnitLearnVo, headers=headers, data=dataGetLessonUnitLearnVo)
            eachRes.raise_for_status()
            pdfUrl = re.search(re_pdfUrl, eachRes.text)
            pdf = requests.get(pdfUrl.group(0))
            print('正在下载第{}份 - {} ...\n'.format(count, name))
            with open(saveDir + '/' + name + '.pdf', 'wb') as file:
                file.write(pdf.content)
        except:
            print('哎呀，这步出了点问题\n')
            continue
        count = count + 1
    print('共下载{}个文件\n'.format(count - 1))


def main():
    infoList = getMocTermDto()
    if infoList == -1:
        return 0
    confirm = input('当前共有{}份pdf文档，确认全部下载？(Y/N)\n'.format(len(infoList)))
    if confirm == 'Y' or confirm == 'y':
        getLessonUnitLearnVo(infoList)
        print('下载完成\n')
    else:
        print('你取消了下载\n')


if __name__ == '__main__':
    main()