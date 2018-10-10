#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：Wayne


'''
map函数的功能：
将传入的函数依次作用于序列中的每一个对象，
然后将其作用的结果作为一个迭代器返回
'''

'''
需求：将列表中的["1", "2", "3", "4", "5"]
转为[1, 2, 3, 4, 5]，写成一个函数。
'''

def func(alist):
    return [int(x) for x in alist]


list1 = ["1", "2", "3", "4", "5"]
print(list1)
print(func(list1))



res = map(int, list1)
print(list(res))


'''
map(func,lsd)
参数一：要作用函数，【此函数有且只有一个参数】
参数二：要作用的序列
'''


'''
使用map函数，求n的序列[1, 4, 9, ..., n^2]， 一行代码实现上述的要求，n从控制台输入。
'''


def func2(n):
    return list(map(lambda x:x**2, range(1, n+1)))


num = int(input("请输入n的值："))
print(func2(num))


print(list(map(lambda n:n*n, range(1, int(input("请输入一个整数："))+1))))

