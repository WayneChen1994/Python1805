#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: Wayne.Chen


def getSum(n):  # 求和：1+2+……+n
    return sum([x for x in range(1, n + 1)])


def getSumEven(n):  # 求1到n的偶数和
    return sum([x for x in range(1, n + 1)][1::2])


def getSumOdd(n):   # 求1到n的奇数和
    return sum([x for x in range(1, n + 1)][::2])
