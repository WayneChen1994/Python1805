#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：Wayne


# 导入模块
from pymongo import MongoClient


# 创建连接，使用默认ip与端口
# client = MongoClient()
# 参数一：ip地址
# 参数二：端口号
client = MongoClient("127.0.0.1", 27017)


# 1、使用“.”获取数据库
# db = client.studb
# 2、使用字典的方式获取
db = client["studb"]


# 1、使用“.”获取集合
# stu = db.stu
# 使用字典的方式获取
stu = db["stu"]


# 查询所有的数据
res = stu.find()
for x in res:
    print(x)


# 关闭连接
client.close()
