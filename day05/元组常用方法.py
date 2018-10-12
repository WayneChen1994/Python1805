#! /usr/bin/env python
# -*- coding: utf-8 -*-
# author: Wayne.Chen


'''
获取元组的长度【元素个数】
'''


t1 = (123, 44, 5, 53, 13, 23)
print(len(t1))


'''
max()
获取元组中的最大值
min()
获取元组中的最小值
注意：无论是min还是max，都要保证元组中的元素类型必须一致，
必须str或者number类型
'''


print(max(t1))
print(min(t1))


'''
tuple(list)
将list转成元组
'''


print(tuple([1, 2, 3]))
print(tuple(range(10)))


'''
二维元组：
当元组中的元素依然是元组，则此元组我们可以称为二维元组
语法：
元组名 = (元组1，元组2，……，元组n)
二维元组元素的访问：
元组名[index1][index2]
index1：代表第index1个元组
index2：代表第index2个元素
'''


tt = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
print(tt[2][2])
print(tt[-1][-1])
