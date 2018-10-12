#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: Wayne.Chen


print()


'''
list1.append(object)
object可以为所有的数据类型
功能：将object作为一个整体追加到list1中
注意：在原列表进行操作的
'''


list1 = []
print(id(list1))
list1.append(12)
list1.append("hello")
list1.append(True)
list1.append(None)
list1.append(True)
list1.append(["good", "nice"])
print(list1)
print(id(list1))


# 可迭代对象


'''
list1.extend(iterable)
常见的可迭代对象：str、list、tuple、set、dict、range
能够作用于for循环都是可迭代对象
功能：将可迭代对象打碎并且追加到list1末尾
'''


list1.extend("haha")
list1.extend(["haha", "hehe"])
print(list1)


'''
list1.insert(index,object)
功能：将指定的对象【object】插入到指定的下标值处，原来的数据
依次往后顺延
'''


print("*" * 50)
list1.insert(0, "你好")
print(list1)


'''
list1.pop([index])
功能：将指定下标的元素移除，并且返回
当index不指定的时候，默认移除最后一个元素
'''


print(list1.pop())
print(list1)
print(list1.pop(0))
print(list1)


'''
list1.remove(object)
功能：将指定的对象移除，移除的为第一个匹配的结果
若没有匹配上，则报错
'''


print("*" * 50)
# list1.remove(True)
print(list1)


'''
list1.clear()
功能：清空列表，注意列表存在，只是元素清空了
del list1
功能：删除列表，元素与列表都没了
'''


# list1.clear()
# print(list1)


'''
list1.index(object[,start][,end])
功能：从左往右在list1中查找指定的对象
若找得到则返回第一个匹配的下标值，若找不到则报错
可以使用start与end指定查找范围，若不指定则查找整个列表
'''


print(list1)
print(list1.index(True))


'''
list1.count(object)
功能：统计object在列表中出现的次数
'''


print(list1.count(True))


'''
len(list1)
功能：获取列表的长度
'''


print(len(list1))
list2 = [1, 3, 33, 4, 65]


'''
max(list)
功能：返回列表中的最大值
min(list)
功能：返回列表中的最小大值
注意：对于列表要求其中的元素类型必须一致【str、num】
'''


print(max(list2))
print(min(list2))


'''
list1.reverse()
功能：将列表中全部元素反转/列表倒序
注意：此函数在原列表操作
'''


print(list1)
list1.reverse()
print(list1)


'''
list1.sort(reverse=False)
功能：对列表进行排序，默认情况下升序
当reverse=True的情况下则为降序。
'''


print(list2)
list2.sort(reverse=True)
print(list2)
