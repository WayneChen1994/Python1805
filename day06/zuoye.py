#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author：zhangjiao


'''
1.设计一个函数，判断用户传入的对象（字符串、列表、元组）长度是否大于5
'''


# def func1(obj):
#     return len(obj)


'''
2.设计一个函数，检查用户传入的对象（字符串、列表、元组）的每一个元素是否含有空内容
【字符串中含有空格，列表与元组中函数有空串】。
若含有则返回True，否则返回False
”hello world“ [12, 34, "", 23]
'''


# def func2(obj):
#     flag = False
#     if isinstance(obj, str):
#         for char in obj:
#             if char.isspace():
#                 flag = True
#                 break
#     elif isinstance(obj, list) or isinstance(obj, tuple):
#         for char in obj:
#             if char == "":
#                 flag = True
#                 break
#     return flag


'''
3.设计一个函数，从控制台输入一个整数，计算整数绝对值的阶乘，n！=1 x 2 x … x n【写成函数】
'''


# num = int(input("请输入一个整数："))


# def func3(n):
#     n = abs(n)
#     res = 1
#     for i in range(1, n + 1):
#         res *= i
#     return res


# print(func3(num))


'''
4.从控制台输入两个正数，求这两个正数的最大公约数，与最小公倍数
注意：最大公约数的公式：
m % n = r ，m = n  n = r  ，r == 0  输出m ，若不为0则继续循环
最小公倍数的公式：
最小公倍数 = 两个正数的乘积/最大公约数
'''


# num1 = int(input("请输入第一个数："))
# num2 = int(input("请输入第二个数："))


# def func4(m, n):
#     if m > n:
#         m, n = n, m
#     maxGYS = 0
#     for i in range(1, m + 1):
#         if m % i == 0 and n % i == 0:
#             maxGYS = i
#     minGBS = m * n / maxGYS
#     return maxGYS, minGBS


# a, b = func4(num1, num2)
# print("最大公约数为%d，最小公倍数为%d" % (a, b))


'''
5.输入一串整数，对其进行冒泡排序【函数】
'''


inputStr = input("请输入一串整数：")
alist = inputStr.split()
blist = []
for i in alist:
    blist.append(int(i))


def func5(li):
    length = len(li)
    for i in range(length - 1):
        for j in range(length - i - 1):
            if li[j] > li[j + 1]:
                li[j], li[j + 1] = li[j + 1], li[j]


func5(blist)
print(blist)
