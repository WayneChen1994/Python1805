#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：Wayne


'''
文档测试
使用文档测试的时候，需要导入doctest模块
此模块可以将函数体中的注释进行提取
提取的时候严格按照Python的交互式模式
使用运算的结果与断言的结果进行对比
'''


import doctest


def mySum(x, y):
    '''
    :param x:
    :param y:
    :return: x + y
    >>> print(mySum(1, 2))
    3
    '''
    return x + y


doctest.testmod()
