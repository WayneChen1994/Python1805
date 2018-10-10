#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：Wayne


'''
注意：在Python2.x中reduce是一个内置函数
但是Python3.x中reduce被放在functools内置模块中
因此，使用reduce的时候，需要先导入functools模块
'''


from functools import reduce
import time

'''
reduce函数：
功能：将序列中的元素作用于函数，
函数需要接收两个参数，
reduce函数会将作用的结果依次与序列中下一个元素进行累计运算，
并且返回运算结果。

reduce(func,lsd)
参数一：要作用的函数【有且只有两个参数】
参数二：传入的序列[可迭代对象]
'''

'''
求map得到的序列之和
print(list(map(lambda n:n*n, range(1, int(input("请输入一个整数："))+1))))
'''


# def func(n):
#     return sum(list(map(lambda x:x*x, range(1, n+1))))
#
#
# print(func(10))

# res3 = reduce(lambda x,y:x+y, list(map(lambda i:i*i, range(1, int(input("请输入一个整数:"))+1))))
#
# print(res3)


'''
需求：分别使用reduce与递归求n的阶乘，比较它们的性能。
'''


def func_reduce(n):
    return reduce(lambda x,y:x*y, range(1, n + 1))


t1 = time.clock()
print(func_reduce(5))
print("reduce求阶乘：{}".format(time.clock() - t1))


def func_recursion(n):
    return 1 if n == 1 else func_recursion(n - 1) * n


t2 = time.clock()
print(func_recursion(5))
print("递归求阶乘：{}".format(time.clock() - t2))
