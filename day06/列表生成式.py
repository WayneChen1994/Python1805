#! /usr/bin/env python
# -*- coding: utf-8 -*-
# author: Wayne.Chen


'''
列表生成式语法：
list1 = [result for x in range(m,n)]
'''


list1 = [x for x in range(1, 11)]
# print(list1)


'''
使用一行代码生成一个序列[0,2,4,6,8,……,100]
'''


list2 = [x for x in range(0, 101, 2)]
# print(list2)


'''
使用一行代码生成一个序列[0,2,4,5,6,8,10,……,100]
'''


list3 = [x for x in range(101) if x % 2 == 0 or x % 5 == 0]
print(list3)
