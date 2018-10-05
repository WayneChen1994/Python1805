#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author：Wayne


# 求和:1+2+……+n
def getSum(n):
    return sum([x for x in range(1, n+1)])

# 求1到n之间的偶数之和
def getSumEven(n):
    return sum([x for x in range(1, n+1)[1::2]])

# 求1到n之间的奇数之和
def getSumOdd(n):
    return sum([x for x in range(1, n+1)[::2]])

# 求1到n之间的任意倍数之和
def getSumAnyTimes(n, times):
    return sum([x for x in range(1, n+1)[times-1::times]])
