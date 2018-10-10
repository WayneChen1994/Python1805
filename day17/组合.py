#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：Wayne


'''
组合：从n个不同元素中，取m个元素进行组合
我们就称n个元素中m个元素的组合
[1, 2, 3, 4] 取3个
'''


import itertools


'''
itertools.combinations(iter, num)
参数一：序列/可迭代对象
参数二：取值的个数
功能：返回从序列中取num个对象的组合，以迭代器的方式返回
'''
list1 = [1, 2, 3, 4]
res = itertools.combinations(list1, 3)
print(list(res))
