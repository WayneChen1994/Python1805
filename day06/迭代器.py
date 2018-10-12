#! /usr/bin/env python
# -*- coding: utf-8 -*-
# author: Wayne.Chen


'''
迭代器：
不但能作用于for循环，而且还能被next()函数调用，返回下一个值
本质：复写了__iter__和__next__函数
'''


from collections import Iterator


print(isinstance([], Iterator))
print(isinstance(iter([1, 2, 3]), Iterator))
print(isinstance((), Iterator))
print(isinstance({}, Iterator))
print(isinstance({1, 2}, Iterator))
print(isinstance((x for x in range(10)), Iterator))


'''
可迭代对象不一定是迭代器，但是迭代器一定是可迭代对象
'''


list1 = [1, 2, 3, 4, 5, 6]
list1 = iter(list1)
print(next(list1))
print(next(list1))
print(next(list1))
print(next(list1))
print(next(list1))
print(next(list1))
print(next(list1))
