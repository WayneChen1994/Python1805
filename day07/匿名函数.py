#! /usr/bin/env python
# -*- coding: utf-8 -*-
# author: Wayne.Chen


'''
匿名函数
概念：是指一类不需要定义函数名的函数

特点：
1、不需要使用def定义，使用lambda定义
2、不需要定义函数名
3、函数体只有一个表达式
4、不需要return，表达式的结果就是返回值

语法：
lambda 参数1，参数2，……，参数n:表达式
若无参数可不写，但冒号不能省略

优点：函数没有名字，不用担心函数名冲突

匿名函数的调用：
1、将匿名函数赋值给一个变量
2、通过变量来进行函数的调用【与之前的函数调用相同】
'''


# func = lambda a,b:a if a>b else b
# print(type(func))
# print(func(10, 20))


# func2 = lambda : print("hello")
# func2()
