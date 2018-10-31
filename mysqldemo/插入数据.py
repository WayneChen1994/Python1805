#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：Wayne


import pymysql


db = pymysql.connect("127.0.0.1", "root", "0831", "studb")
cursor = db.cursor()


'''
需求：要求用户名与年龄从控制台输入。
'''


def insertData(name, age):
    sql = "insert into teacher(name, age) values('%s', %d)" % (name, age)
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 提交事务
        db.commit()
    except Exception as e:
        print(e)
        # 回滚到执行sql之前的状态
        db.rollback()


for i in range(5):
    name = input("请输入您的姓名：")
    age = int(input("请输入您的年龄："))
    insertData(name, age)


db.close()
