#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: Wayne.Chen


print()


'''
列表的定义：
列表的实质就是一个有序的集合。

创建列表的语法：
列表名 = [元素1,元素2,元素3,……,元素n]
元素的类型可以是我们所有的数据类型
'''


list1 = [1, 2, 3, "小明", True, None, [1, 2, 3]]
# print(list1)


# 创建一个空列表
# list2 = []
# print(list2)
# 创建一个空列表
# list3 = list()  # 强转
# print(list3)


'''
如何访问列表中的元素？
通过索引值/下标值来进行访问的
下标值的取值范围[0,len(list1)-1]
长度从1开始数的
下标从0开始数的
但下标为负的时候，则默认从右开始取。[-1,-len(list1)]
'''


# print(len(list1))
# print(list1[6])
# print(list1[-1])


'''
列表中元素的更改
列表名[下标] = 值
可以通过下标来更改列表中的值
'''


# print(list1)
# print(id(list1))
# list1[-1] = "good"
# print(list1)
# print(id(list1))


'''
list3 = list1 + list2
功能：将list1的元素与list2的元素同时存放到list3中返回
'''


list2 = [1, 2, 4]
list3 = ['a', 'b', 'c']
print(list2 + list3)


'''
list2 = list1*n
将list1中的元素重复n次输出到list2，并且返回
'''


print(list2 * 3)


'''
判断元素是否在列表中
元素 in 列表
若存在则返回True，否则返回False
元素 not in 列表：判断元素是否不在列表中，若不在则返回True，否则返回False
'''


print(1 in list2)
print(1 not in list2)


'''
列表的截取：
列表名[start:end]
取值区间[start,end)
若start不写，默认从0开始
若end不写，则默认取到最后
若start和end都不写，则默认取整个列表
'''


print(list1[1:3])
print(list1[:3])
print(list1[1:])
print(list1[:])


'''
二维列表语法：
列表名 = [列表1，列表2，……，列表n]
'''


list4 = [[1, 2, 3],[True, False], ["hello", "hi", "hehe"]]


'''
二维列表访问元素？
list[index1][index2]
index1：用来锁定列表
index2：用来锁定列表中的元素
其中index1代表第index1+1个列表（下标从0开始）
index2代表第index1+1个列表中第index2+1个元素
'''


print(list4[0][0])
print(list4[-1][-1])
