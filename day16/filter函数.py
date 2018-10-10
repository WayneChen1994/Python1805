#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：Wayne


'''
filter(func,lsd):
参数一：作用于序列的函数
参数二：序列
功能：过滤序列中的元素，根据返回的True还是False决定该元素是保留还是丢弃
返回True保留，返回False丢弃
'''

'''
[1, 2, 3, 4, 56, 34, 23, 55]
去除序列中的偶数
'''


def func(alist):
    return [x for x in alist if x % 2 != 0]


list1 = [1, 2, 3, 4, 56, 34, 23, 55]
# print(func(list1))


def f(n):
    return False if n % 2 == 0 else True


# print(list(filter(f, list1)))


# print(list(filter(lambda n:n%2!=0, list1)))


data = [["jerry", 18, "老鼠"], ["tom", 25, "无"], ["hanmeimei", 26, "金钱"]]


res = list(filter(lambda l:l[-1] != "无", data))
print(res)
