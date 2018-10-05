#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author: Wayne.Chen

print()
'''
赋值拷贝：=
引用拷贝，类似于Windows快捷方式
'''
list1 = [1,3,4,5]
# list2 = list1
# print(list1)
# print(list2)
# list2[-1] = "hello"
# print(list1)
# print(list2)



'''
list1.copy()
拷贝是一个内存拷贝，并非是一个完全内存拷贝
'''
# list2 = list1.copy()
# print(id(list1))
# print(id(list2))
# list2[-1] = "hello"
# print(list1)
# print(list2)

list3 = [1,3,4,5,[1,2,3]]
# list4 = list3.copy()
# print(list3)
# print(list4)
# list4[-1][-1] = "hello"
# print(list3)
# print(list4)
# print(id(list3))
# print(id(list4))

'''
使用copy模块中的copy.deepcopy(list1)
此方法才为一个完全拷贝
若是多维列表拷贝的时候可以使用此方法。
'''
import copy

list5 = copy.deepcopy(list3)
print(list3)
print(list5)
list5[-1][-1] = "hello"
print(list3)
print(list5)






