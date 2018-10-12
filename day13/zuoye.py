#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：Wayne


'''
import time


def gettime():
    return time.time()


def getstrtime(t1=time.time()):
    # t1 = time.time()
    lt = time.localtime(t1)
    return time.strftime("%Y-%m-%d %X", lt)


def strtotime(strtime):
    st = time.strptime(strtime, "%Y-%m-%d %X")
    return time.mktime(st)


if __name__ == "__main__":
    print(gettime())
    print(getstrtime())
    print(type(getstrtime()))
    print(strtotime("2018-09-29 09:06:02"))
    print(getstrtime(1538183162))
'''


'''
解决问题的时候，最关键的两个地方
1、如何获取当前月的天数
2、这个月的第一天是星期几
'''


'''
import time
def getcalendar(year, month):
    str1 = str(year) + "-" + str(month) + "-1"
    if month == 12:
        str2 = str(year+1) + "-" + "1" + "-1"
    else:
        str2 = str(year) + "-" + str(month+1) + "-1"
    strpt = time.strptime(str1, "%Y-%m-%d")
    num = strpt.tm_wday
    strpt2 = time.strptime(str2, "%Y-%m-%d")
    t1 = time.mktime(strpt)
    t2 = time.mktime(strpt2)
    # 时间间隔天数
    tt = int((t2 - t1)/(60*60*24))
    res = '星期一\t星期二\t星期三\t星期四\t星期五\t星期六\t星期日\t\n'
    for i in range(num):
        res += '\t\t'
    for x in range(1, tt + 1):
        res += str(x) + '\t\t'
        if (x + num) % 7 == 0:
            res += '\n'
    return res


print(getcalendar(2018, 12))
'''


'''
def oushu(n):
    res = 0
    for x in range(n+1):
        if x%2 == 0:
            res += x
    return res


def jishu(n):
    res = 0
    for x in range(n+1):
        if x%2 != 0:
            res += x
    return res


def beishu(m, n):
    res = 0
    for x in range(n+1):
        if x%m == 0:
            res += x
    return res


if __name__ == "__main__":
    print(oushu(10))
    print(jishu(10))
    print(beishu(3, 10))
'''


import time
import datetime


def getnextime():
    print(datetime.datetime.now())
    t1 = time.time()+1
    lt = time.localtime(t1)
    return time.strftime("%Y-%m-%d %X", lt)


print(getnextime())
