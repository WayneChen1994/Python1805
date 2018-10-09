#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：Wayne


'''
自定义异常的时候，我们需要选好继承的关系。
异常不但可以捕捉，还可以抛出，抛出异常
'''


class ZeroError(ValueError):pass


def func(a, b):
    b = int(b)
    if b == 0:
        # 抛出异常
        raise ZeroError("除数为0")
    return a / b


print(func(1, 2))
print(func(1, 0))
