#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：Wayne


from pymongo import MongoClient


client = MongoClient()
db = client.studb
stu = db.stu


# 查询年龄大于25的男生，将其年龄减1
# .update({查询条件},{设置},multi=False)
# 默认只更改一条数据，若想更改所有数据，需要multi=True
stu.update({'age':{'$gt':20}, 'gender':1}, {'$inc':{'age':-1}},multi=True)


client.close()
