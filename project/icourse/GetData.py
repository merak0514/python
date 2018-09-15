# !/user/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 9:44
# @Author   : Merak
# @File     : GetData.py
# @Software : PyCharm
import time
import re


def batch_id():
    return round(time.time() * 1000)


def get_term_info():
    data = {
        'callCount': '1',
        'scriptSessionId': '${scriptSessionId}190',
        'c0-scriptName': 'PublishCourseBean',
        'c0-methodName': 'getTermsByTeacher',
        'c0-id': 0,
        'c0-param0': 'number:2',
        'batchId': batch_id()
    }
    return data


def get_moc_data(term_id):
    data = {
        'callCount': '1',
        'scriptSessionId': '${scriptSessionId}190',
        'c0-scriptName': 'MocScoreManagerBean',
        'c0-methodName': 'getMocTermDataStatisticDto',
        'c0-id': 0,
        'c0-param0': 'string: ' + term_id,
        'batchId': batch_id()
    }
    return data


def get_oj_by_oj_id(oj_id, page, stu_per_page):
    """
    :param oj_id:
    :type oj_id: int
    :param page:
    :type page: int
    :param stu_per_page:
    :type stu_per_page: int
    :return: data:
    :rtype: dict
    """
    data = {
        'callCount': '1',
        'scriptSessionId': '${scriptSessionId}190',
        'c0-scriptName': 'MocScoreManagerBean',
        'c0-methodName': 'getStudentScoresByTestId',
        'c0-id': 0,
        'c0-param0': 'string: ' + str(oj_id),
        'c0-param1': 'number:' + str(stu_per_page),
        'c0-param2': 'number:' + str(page),
        'c0-param3': 'null:null',
        'c0-param4': 'number:1',
        'batchId': batch_id(),
    }
    return data


def data_manage_oj_stu(data):
    """
    :param data:
    :type data: str
    :return: oj_stu_set: 每一项是一个学生在此次作业的情况
    :rtype: list
    """
    split = data.split('\n')
    data_dict = {}  # 索引为s_number，内容为所在行
    sign_set = []
    oj_stu_set = []
    for line in split:
        if line.startswith('s2['):
            sign_set = re.findall('=(s[0-9]+);', line)
        if line.startswith('s'):
            data_dict[re.findall('s[0-9]+', line)[0]] = line
    if not sign_set:
        for line in split:
            if line.startswith('s3['):
                sign_set = re.findall('=(s[0-9]+);', line)
    va = list(data_dict.values())
    for line in va:
        line = line.rstrip('\r')
        sign = re.findall('s[0-9]+', line)[0]
        if sign in sign_set:
            temp_set = [line]
            for sign2 in re.findall('=(s[0-9]+);', line):
                temp_set.append(data_dict[sign2].rstrip('\r'))
                for sign3 in re.findall('=(s[0-9]+);', data_dict[sign2]):
                    temp_set.append(data_dict[sign3].rstrip('\r'))
                data_dict.pop(sign2)
            temp = ''.join(temp_set)
            oj_stu = {
                'nickname': re.findall('nickname="(.+?)";', temp)[0].encode().decode('unicode_escape'),
                'email': re.findall('email=(.+?);', temp)[0],
                'personalUrlSuffix': -1 if not re.findall('personalUrlSuffix="(.+?)";', temp) else
                re.findall('personalUrlSuffix="(.+?)";', temp)[0],
                'sex': -1 if not re.findall('sex=(.+?);', temp) else re.findall('sex=(.+?);', temp)[0],
                'realName': re.findall('realName=(.*?);', temp)[0].encode().decode('unicode_escape'),
                'lastLogonTime': re.findall('lastLogonTime=(.+?);', temp)[0],
                'gmtCreate': re.findall('gmtCreate=(.+?);', temp)[0],
                'gmtModified': re.findall('gmtModified=(.+?);', temp)[0],
                'id': re.findall('id=(.+?);', temp)[0],
                'type': 7,
            }
            oj_stu_set.append(oj_stu)
            data_dict.pop(sign)
    return oj_stu_set


def data_manage_ex_term(data):
    """
    :param data: 
    :type data: str
    :return: oj_set, test_set
    :rtype: 
    """
    c = re.compile('description=.*?;')
    content = re.sub(c, '', data).encode().decode('unicode_escape')  # 转换为中文
    split = content.split('\n')
    oj_set = []
    test_set = []
    for line in split:
        if re.findall('type=7', line) and re.findall('name=', line):
            oj_info = {
                'name': re.findall('name="(.+?)";', line)[0],
                'id': re.findall('id=(.+?);', line)[0] if re.findall('id=(.+?);', line)[0] else '-1',
                'chapterId': re.findall('chapterId=(.+?);', line)[0],
                'avgScore': re.findall('avgScore=(.+?);', line)[0],
                'releaseTime': re.findall('releaseTime=(.+?);', line)[0],
                'deadline': re.findall('deadline=(.+?);', line)[0],
                'evaluateScoreReleaseTime': re.findall('evaluateScoreReleaseTime=.+;', line)[0],
                'sbjTotalScore': re.findall('sbjTotalScore=(.+?);', line)[0],
                'termId': re.findall('termId=(.+?);', line)[0],
                'submitTestCount': re.findall('submitTestCount=(.+?);', line)[0],
                'type': 7,
            }
            oj_set.append(oj_info)
        if re.findall('type=2', line) and re.findall('name=', line):
            # print(line)
            test_info = {
                'name': re.findall('name="(.+?)";', line)[0],
                'id': re.findall('id=(.+?);', line)[0],
                'chapterId': re.findall('chapterId=(.+?);', line)[0],
                'avgScore': re.findall('avgScore=(.+?);', line)[0],
                'releaseTime': re.findall('releaseTime=(.+?);', line)[0],
                'deadline': re.findall('deadline=(.+?);', line)[0],
                'evaluateScoreReleaseTime': re.findall('evaluateScoreReleaseTime=(.+?);', line)[0],
                'ojTotalScore': re.findall('sbjTotalScore=(.+?);', line)[0],
                'termId': re.findall('termId=(.+?);', line)[0],
                'submitTestCount': re.findall('submitTestCount=(.+?);', line)[0],
                'testRandomSetting': re.findall('testRandomSetting=(.+)', line)[0],
                'type': 2,

            }
            test_set.append(test_info)
    return oj_set, test_set


def data_manage_term_info(data):
    """
    :param data:
    :type data: str
    :return: terms: 该课程已经进行的学期列表
    :rtype: list
    """
    split = data.split('\n')
    terms = []
    for line in split:
        if line.startswith('s'):
            term = {
                'term': re.findall('s([0-9]+)\.', line)[0],
                'term_id': re.findall('s[0-9]+\.termId=([0-9]+)', line)[0],
            }
            terms.append(term)
    return terms
