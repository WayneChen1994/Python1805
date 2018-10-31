#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：Wayne


import pymysql


db = pymysql.connect("127.0.0.1", "root", "0831", "studb")
cursor = db.cursor()


sql = "select * from teacher limit 3"
sql2 = "select * from teacher"


cursor.execute(sql)
cursor.execute(sql2)


# cursor.fetchall() 获取全部的结果
# 结果集是一个迭代器，每一条数据则为一个元组
userDict = {}
for x in cursor.fetchall():
    userDict[x[0]] = x[1]
print(userDict)


# cursor.fetchone() 获取一条数据
print(cursor.fetchone())


# cursor.rowcount 返回总数据的条数
print(cursor.rowcount)


# 关闭连接
db.close()
