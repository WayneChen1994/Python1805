#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：Wayne


from pymongo import MongoClient
import datetime


client = MongoClient()
db = client.studb
stu = db.stu


file1 = {"name":"lili5", "age":18, "class":"python1805", "sex":0, "stuid":12222, "isDelete":0, "date":datetime.datetime.now()}
file2 = {"name":"lili6", "age":18, "class":"python1805", "sex":0, "stuid":12222, "isDelete":0, "date":datetime.datetime.now()}
# 插入一条数据
# stu.insert_one(file1)
# 插入一条数据
# stu.insert(file1)


# 同时插入多条数据
# stu.insert([file1, file2])
# 同时插入多条数据
stu.insert_many([file1, file2])

# result = db.stu.find({"name":"lili"})
# for x in result:
#     print(x)


client.close()
