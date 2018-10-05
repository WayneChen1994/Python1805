#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Wayne.Chen

'''
is ：is判断的是两个标识符是不是引用同一个对象
【换句话说就是两个变量的内存地址是否相同】

is not：判断两个标识符是不是没有引用同一个对象
'''
a = 1000
b = 1000
list1 = [1,2,3,43]
list2 = [1,2,3,43]
list3 = list2

print(list3)
print(id(list2))
print(id(list3))
print(list2 is list3)
print(list1 == list2)

# print(id(list1))
# print(id(list2))
# print(list1 is list2)

# print(id(a))
# print(id(b))
# print(a is b)  #False

print("%.2f" % 12)
