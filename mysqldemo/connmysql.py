#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：Wayne


# 导入pymysql模块
import pymysql


# 打开数据库连接
# 参数一:IP地址
# 参数二:用户名
# 参数三:密码
# 参数四:数据库名
db = pymysql.connect("127.0.0.1", "root", "0831", "studb")


# 获取游标对象
cursor = db.cursor()


# 执行sql语句
# cursor.execute("select version()")

# 获取一条查询的结果
# res = cursor.fetchone()
# print(res)


'''
需求:循环获取所有的数据库名,并且将数据库名放到列表中
'''


# list1 = []
cursor.execute("show databases")
# flag = True
# while flag:
#     res = cursor.fetchone()
#     if not res:
#         flag = False
#     else:
#         list1.append(res[0])
# print(list1)

res = cursor.fetchall()
for i in res:
    print(i[0])


# 关闭连接
db.close()
