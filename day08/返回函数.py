#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: Wayne.Chen


'''
返回函数：
将函数作为返回值返回，我们就称此函数为返回函数
'''


import functools


int3 = functools.partial(int, base=2)
# print(type(int3))


# 装饰器
# def outer(f):
#     def inner():
#         print("**********")
#         f()
#     return inner


'''
求和：
从控制台输入几个数，求这几个数的和
'''


def func(*args):
    res = 0
    for x in args:
        res += x
    return res


print(func(1, 2, 3, 4))
print(func(1, 2, 3))
print(func(3, 2, 3))


def lazy_func(*args):
    def func():
        res = 0
        for x in args:
            res += x
        return res
    return func


print(lazy_func(1, 2, 3)())
