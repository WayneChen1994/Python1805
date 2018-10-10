#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：Wayne


'''
排列：
从n个元素中取出m个元素，按照一定的顺序进行排列
我们就叫做n个元素中m个元素的排列，当n=m的时候，
我们又称这个排列为全排列
1, 2, 3, 4
随机取三个数进行排列，求其排列方式有多少种？
'''


import itertools


'''
排列：
itertools.permutations(iter, num)
参数一：序列【可迭代对象】
参数二：进行排列的个数
功能：从序列中取num个元素进行排列，并且返回排列的结果（作为一个迭代器返回）
'''
list1 = [1, 3, 3, 4]
res = itertools.permutations(set(list1), 3)
print(list(res))
print(len(list(res)))
