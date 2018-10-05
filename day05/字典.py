#! /usr/bin/env python
# -*- coding: utf-8 -*-
# author: Wayne.Chen


'''
dict字典
存储：是以键值对(key-value)的方式来进行存储的
对于key必须满足以下要求：
1、key必须唯一
【key不能出现重复】
2、key必须是不可变类型
不可变类型：number、str、bool、None、tuple

什么时候使用字典？
比如学生的考试成绩
'''

'''
字典的创建：
字典名 = {键1：值1,键2：值2，……，键n:值n}
键与值之间使用“:”连接，键值对之间使用“,”连接
'''
dict1 = {}
dict2 = {1: 2, 2: 3, 3: 4, 3: 5}
dict3 = {"11": 2, 2: 3, 3: 4, 3: 5}
dict4 = {"11": 2, False: 3, 3: 4, 3: 5}
dict5 = {"11": 2, False: 3, (1, 2, 3): 4, None: 5}
print(dict1)
print(dict2)
print(dict3)
print(dict4)
print(dict5)

'''
字典访问：
第一种访问方式：
字典名[key]
注意：当key不存在的时候，则会报错KeyError

第二种访问方式:
字典名.get(key)
注意：当key不存在的时候，返回None，而不会报错
'''
# print(dict5["None"])
print(dict5[None])
print(dict5.get(None))
print(dict5.get("None"))

'''
添加元素
语法：
字典名[key] = value
注意：key不能重复，当key出现重复的时候，后面添加的会将前面的value覆盖掉
'''
dict5["22"] = "hello"
print(dict5)
dict5[False] = False
print(dict5)


'''
删除元素
字典名.pop(key)
功能：删除指定的键值对【key-value】
并且返回对应key的value值
若删除的key不存在，则报错
'''
# print(dict5.pop("11"))
# print(dict5)
# print(dict5.pop(11))
# print(dict5)


'''
注意：字典在内存中的存储是无序的，因此不能通过下标来进行取值
'''
for key in dict5:
    print(key, end="\t")
print()
for value in dict5:
    print(value, end="\t")
print()
for item in dict5.items():
    print(item, end="\t")
print()
for k, v in dict5.items():
    print(k, v, end="\t")

'''
与list相比：
1、查找与插入速度，dict比较快，不会随着数据的增多而变慢
2、占用空间，dict比较浪费内存，
    1.多存储了一个key
    2.数据存储排列是不紧密的
'''
