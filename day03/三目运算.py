#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author: Wayne.Chen


'''
Python中原本不存在三目运算，而是我们使用if语句将其强制性写在一行而完成的一个伪三目运算
语法：
result1 if 判断条件 else result2
当判断条件成立的情况下，返回result1，
当判断条件不成立的情况下，返回result2
'''

'''
从控制台输入两个数，返回最大的那个
'''

num = int(input("请输入第一个数："))
num2 = int(input("请输入第二个数："))
print(num if num > num2 else num2)









