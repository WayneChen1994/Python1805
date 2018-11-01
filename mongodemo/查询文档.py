#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：Wayne


from pymongo import MongoClient
import pymongo


client = MongoClient()
db = client.studb
stu = db.stu


# 查询所有的数据，返回一个迭代器
# res = stu.find()
# for row in res:
#     print(row)


# 根据条件查询数据
# 若条件中含有正则的时候，我们使用$regex
# res2 = stu.find({"name":{"$regex":"li$"}})
# for row in res2:
#     print(row)


# 获取查询数据的条数
# res3 = stu.find({"name":{"$regex":"li$"}}).count()
# print(res3)


# 获取指定的字段
# res4 = stu.find({"name":{"$regex":"li$"}}, {"name":1, "age":1, "class":1, "_id":0})
# for row in res4:
#     print(row)


# 排序.sort([(key,1),(key2,-1)])
# 若取值为1则为升序，若取值为-1则为降序
# res5 = stu.find().sort([("age", pymongo.ASCENDING), ("_id", pymongo.DESCENDING)])
# for row in res5:
#     print(row)


for num in range(int(stu.find().count()/3)):
    # 分页获取数据
    res6 = stu.find().skip(3*num).limit(3)
    for row in res6:
        print(row)
    print()
    print()
    print()


client.close()
