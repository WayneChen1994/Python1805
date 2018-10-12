#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: Wayne.Chen


import datetime
import time


# 直接获取的系统当前时间
dt = datetime.datetime.now()
print(dt)
print(type(dt))


# 把datetime对象格式化成时间字符串
time1 = dt.strftime('%Y-%m-%d %X')
print(time1.split(' '))
print(type(time1))
time.sleep(2)
dt2 = datetime.datetime.now()


# 当两个时间相减的时候则返回一个时间间隔的对象
dt3 = dt2 - dt
print(dt3)
print(type(dt3))


# 获取间隔的天数
print(dt3.days)


# 获取除天数之外的秒数
print(dt3.seconds)
