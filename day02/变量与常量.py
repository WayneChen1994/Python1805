#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Wayne.Chen


'''
作用：将不同的数据存储到内存中
变量定义：
变量名 = 变量名
注意：当我们创建变量的时候，必须给变量名进行赋值
如何查看变量的数据类型？
type(变量名)
通过id函数查看变量的地址
id(变量名)
删除变量
del 变量名
注意：变量一旦删除，则不能再进行引用

常量：
程序运行期间不能改变的数据，我们称之为常量
作用：常量就是用来给变量赋值的
比如：123，"hello"
'''


age = 18
# 同时创建多个变量
num1, num2, num3 = 10, 20, 30
print(num1, num2, num3)
num1 = "hello"
print(num1)
# del age
# print(age)

