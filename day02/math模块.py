#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Wayne.Chen

# 导入模块
import math

print(math.ceil(123.35))
print(math.ceil(123.05))
print(math.ceil(123.95))

print(math.floor(123.45))
print(math.floor(123.85))
print(math.floor(123.85))

print(math.modf(-123.456))
x, y = math.modf(12.45)
print(x, y)

print(math.sqrt(9))
print(math.sqrt(8))

'''
# ceil  天花板
# math.ceil()   向上取整

# floor 地板
# math.floor()  向下取整

# math.modf(num)    返回num的小数部分与整数部分
# 返回的数值符号与num的符号相同，返回的结果是一个元组
# 第一个元素是小数部分，第二个是整数部分[以浮点数的形式显示]

# math.sqrt(num)    返回num的开平方,值为浮点数
'''
