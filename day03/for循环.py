#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: Wayne.Chen


'''
for循环
语法：
for x in 序列/list/tuple/set/dict/str:
    循环体
执行：每次循环将序列中的元素依次取出，取出之后赋值给x，直到序列中的元素取完为止，循环结束。
'''


# list1 = ["hello", "good", True, "nice", 5]
# for x in list1:
#     print(x)

# for char in "hello":
#     print(char)


'''
使用for循环求1+2+3+……+10的值
'''


# sum = 0
# for i in [1,2,3,4,5,6,7,8,9,10]:
#     sum += i
# print(sum)


'''
range([start,]stop[,step])
start：指定起始位置，默认0【可不写】
stop:指定结束位置，取值区间[start,stop)，必须写
step：步长，默认为1【可不写】
'''


# print(list(range(1, 11, 2)))


'''
求积：1x2x3x……x100
使用for循环
'''


res = 1
for i in range(1, 101):
    res *= i
print(res)
