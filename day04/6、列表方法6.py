#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author: Wayne.Chen


print()
'''
list(tuple)可以将元组转为列表
'''
list1 = list((1,2,3))
print(list1)


# 关于列表的遍历
'''
语法：
for 变量 in 列表：
    语句块
功能：依次将列表中的每一个元素取出，并且赋值给我们的变量

for index,value in enumerate(list2):
    语句块
使用此方法可以将元素以及对应下标值一起取出
'''

list2 = ["hehe","haha","xixi"]
for x in list2:
    print(x)

for index,value in enumerate(list2):
    print(index, value)








