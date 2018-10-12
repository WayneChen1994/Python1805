#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: Wayne.Chen


import calendar


# 返回指定月份的日历【字符串类型】
# cm = calendar.month(2018, 9)
# print(cm)
# print(type(cm))


# 返回指定年份的日历【字符串类型】
# cy = calendar.calendar(2018)
# print(cy)
# print(type(cy))
# print(calendar.firstweekday())


# 判断指定的年份是否为闰年
# print(calendar.isleap(100))
# print(calendar.isleap(200))
# print(calendar.isleap(400))


# 返回[year1, year2)之间闰年的个数
# print(calendar.leapdays(2008, 2018))
# print(calendar.leapdays(2008, 2020))


# 返回指定月份第一天的星期码，与这个月的天数
# print(calendar.monthrange(2018, 9))
# print(calendar.monthrange(2018, 8))


# 返回一个以周为单位的日期的列表，若出现空余的则补0
# print(calendar.monthcalendar(2018, 9))


# 返回指定日期的星期码
# print(calendar.weekday(2018, 9, 26))


'''
需求1：利用month.weekday，monthrange打印当月的日历
'''


def getMonthCalendar(year, month):
    num, days = calendar.monthrange(year, month)
    res = '星期一\t星期二\t星期三\t星期四\t星期五\t星期六\t星期日\t\n'
    for i in range(num):
        res += '\t\t'
    for x in range(1, days+1):
        res += str(x) + '\t\t'
        if (x+num) % 7 == 0:
            res += '\n'
    return res


print(getMonthCalendar(2018, 9))


'''
需求2：给定指定的月份，打印指定月份的日历
'''
