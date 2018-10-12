#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Wayne.Chen


# 导入模块
import random


# random.choice(序列)
# 功能：从指定的序列中随机的挑选一个元素
print(random.choice([1, 2, "hello", 56, True, False]))


'''
random.randrange(100)   从0到99之间随机挑选一个整数
random.randrange([start,]stop[,step])
参数一：指定从哪开始【包含】,默认为0
参数二：指定到哪里结束【不包含】，必须写
取头去尾 [start, stop)  左闭右开区间
参数三：指定步长，默认为1
'''


print(random.randrange(100))
print(random.randrange(0, 101, 3))


'''
random.shuffle(list1)
将指定的序列进行随机的排列
'''


list1 = [1, 22, 33, 11, 20]
random.shuffle(list1)
print(list1)


'''
random.random()
从区间[0,1)中随机取一个浮点数
若想更改此区间则需要通过其他的运算
'''


print(random.random())
print(random.random() * 100)


'''
random.uniform(m,n)
随机从[m,n]区间，取一个浮点数
'''


print(random.uniform(1, 10))
