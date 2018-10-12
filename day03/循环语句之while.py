#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: Wayne.Chen


'''
while 判断条件:
    语句块

执行：先执行判断条件，当条件成立，则执行下面的语句块，
执行完语句块之后，继续执行判断条件，直到条件不成立的时候，则退出循环
'''


'''
求和：
1+2+3+……+10
'''


# res = 0
# n = 1
# while n <= 10:
#     res += n
#     n += 1
# print(res, n)


'''
求积：
1*2*3*……*100
'''


# res = 1
# num = 1
# while num <= 100:
#    res *= num
#    num += 1
# print(res, num)


'''
求阶乘
从控制台输入一个数，求这个数的阶乘
3！= 1 x 2 x 3
5! = 1 x 2 x 3 x 4 x 5
'''


# num = int(input("请输入一个正整数:"))
# res = 1
# n = 1
# while n <= num:
#     res *= n
#     n += 1
# print(res, n)


# num = int(input("请输入一个正整数："))
# sum = 0
# res = 1
# n = 1
# while n <= num:
#     res *= n
#     sum += res
#     n += 1
# print(sum)


# num = int(input("请输入一个正整数："))
# sum = 0
# n = 1
# while n <= num:
#     res = 1
#     m = 1
#     while m <= n:
#         res *= m
#         m += 1
#     sum += res
#     n += 1
# print(sum)


#打印九九乘法表
i = 1
while i < 10:
    j = 1
    while j <= i:
        print("%d×%d＝%d" % (j, i, i*j), end="\t\t")
        j += 1
    print()
    i += 1
