#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：Wayne


import pymysql


db = pymysql.connect("127.0.0.1", "root", "0831", "studb")
cursor = db.cursor()


'''
需求：将来自广州的男生年龄加2
'''


sql = "update stutable set age=age+2 where gender and address='广州'"


try:
    cursor.execute(sql)
    print("执行成功")
    db.commit()
except:
    print("执行失败。。。")
    db.rollback()


db.close()
