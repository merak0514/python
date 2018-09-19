# !/user/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 14:35
# @Author   : Merak
# @File     : ModuleIcourse.py
# @Software : PyCharm
import pymysql
# pymysql.err.InternalError


def upload_moc_data(data):
    print('Connecting MySQL')
    db = pymysql.connect('localhost', 'root', '', 'code_data_term1')
    oj_set = data['oj_set']
    test_set = data['test_set']
    sql = "INSERT INTO `exercises`(`exName`, `exId`, `exType`, `avgScore`, `sbjTotalScore`," \
          " `releaseTime`, `deadline`) VALUES(%s, %s, %s, %s, %s, %s, %s)"
    cursor = db.cursor()
    cursor.execute("set names 'utf8'")
    for oj in oj_set:
        cursor.execute(sql, (oj['name'], int(oj['id']), 2, float(oj['avgScore']),
                             float(oj['sbjTotalScore']), oj['releaseTime'], oj['deadline']))
    db.commit()
    print('OJ uploaded')
    for test in test_set:
        cursor.execute(sql, (test['name'], int(test['id']), 2, float(test['avgScore']),
                             0, test['releaseTime'], test['deadline']))
    print('Test uploaded')
    db.commit()
    db.close()
    print('Connecting closed')
