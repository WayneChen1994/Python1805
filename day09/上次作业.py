#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: Wayne.Chen


'''
def func1():
    list1 = []
    for i in [1, 2, 3, 4]:
        for j in [1, 2, 3, 4]:
            for k in [1, 2, 3, 4]:
                if i != j and i!=k and j!=k:
                    list1.append((i, j, k))
    return list1


res = func1()
print(len(res))
'''


'''
def lirun(I):
    jiang = 0
    if I <= 10:
        jiang = I * 0.1
    elif I <= 20:
        jiang = 10 * 0.1 + (I - 10) * 0.075
    elif I <= 40:
        jiang = 10 * 0.1 + 10 * 0.075 + (I - 20) * 0.05
    elif I <= 60:
        jiang = 10 * 0.1 + 10 * 0.075 + 20 * 0.05 + (I - 40) * 0.03
    elif I <= 100:
        jiang = 10 * 0.1 + 10 * 0.075 + 20 * 0.05 + 20 * 0.03 + (I - 60) * 0.015
    else:
        jiang = 10 * 0.1 + 10 * 0.075 + 20 * 0.05 + 20 * 0.03 + 40 * 0.015 + (I - 100) * 0.1
    return jiang


print(lirun(120))
print(lirun(100))
print(lirun(80))
print(lirun(60))
print(lirun(40))
print(lirun(20))
'''


'''
list1 = [1, 2, 3, 4, 5]
list2 = list1.copy()
list3 = list1[:]
# deepcopy、for循环遍历
print(id(list1))
print(id(list2))
print(id(list3))
'''


'''
def func(n):
    if n == 1:
        return 10
    else:
        return func(n - 1) + 2


print(func(5))
print(func(3))
'''


'''
li = ["hello", 'seven', ["mon", ["h", "kelly"], 'all'], 123, 446]
print(li[2][1][1].capitalize())
li[2][-1] = 'ALL'
print(li)
'''


'''
def wanshu(n):
    list1 = []
    for x in range(1, n+1):
        res = 0
        for i in range(1, x):
            if x % i == 0:
                res += i
        if x == res:
            list1.append(x)
    return list1


print(wanshu(1000))
'''


'''
def func3(n):
    if n == 1:
        return 100
    else:
        return func3(n - 1) * 0.5


print(func3(10))


def func4(n):
    res = 100
    if n == 1:
        return res
    for x in range(2, n+1):
        res += func3(x) * 2
    return res


print(func4(1))
print(func4(2))
print(func4(3))
print(func4(4))
'''


'''
# res = 1
# for x in range(10, 1, -1):
#     res = (res + 1) * 2
# print(res)


def func5(n):
    if n == 10:
        return 1
    else:
        return (func5(n + 1) + 1) * 2


print("*" * 50)
print(func5(10))
print(func5(9))
print(func5(8))
print(func5(1))
'''


'''
import random


maxNum = int(input("请输入最大数："))
minNum = int(input("请输入最小数："))
suiji = random.randrange(minNum, maxNum+1)
print("数字范围区间为：%d~%d" % (minNum, maxNum))
print("随机数为%d" % suiji)
count = 0


while True:
    count += 1
    num = int(input("请输入您猜测的数据："))
    if num == suiji:
        print("恭喜你猜对了,您使用的次数为%d" % count)
        break
    else:
        if num > suiji:
            print("大了")
        else:
            print("小了")
'''
