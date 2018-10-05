#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author：Wayne


import time


# 获取当前时间戳
def getTimeStamp():
    return time.time()

# 获取当前时间字符串
def getTimeStr():
    return time.strftime('%Y-%m-%d %X',
                         time.localtime(time.time()))

# 将时间字符串转换为时间戳，pattern为字符串对应的格式
def timeStrToStamp(timeStr, pattern):
    return time.mktime(time.strptime(timeStr, pattern))

# 将时间戳转换为时间字符串，pattern为字符串对应的格式
def timeStampToStr(timeStamp, pattern):
    return time.strftime(pattern, time.localtime(timeStamp))

# 通过月份打印当月日历，只使用time模块
def getCalendarByMonth(month):
    # 只给定月份，那就默认以当前年份为准。。。
    firstDayStr = "2018-%d-1"%month
    timeTuple = time.strptime(firstDayStr, '%Y-%m-%d')
    space = timeTuple.tm_wday + 1
    if month in [1, 3, 5, 7, 8, 10, 12]:
        days = 31
    else:
        days = 30
    res = "日\t一\t二\t三\t四\t五\t六\n"
    for i in range(space):
        res += "\t"
    for x in range(1, days+1):
        res += (str(x) + "\t")
        if (x+space) % 7 == 0:
            res += "\n"
    return res

print(getCalendarByMonth(9))
