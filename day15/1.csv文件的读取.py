#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：Wayne


import csv

'''
读取csv文件
1、首先导入csv模块
2、打开文件之后，
csv.reader(f)
返回一个迭代器
3、可以通过迭代器将数据取出
'''
# with open("democsv.csv", "r") as f:
#     all = csv.reader(f)
#     for line in all:
#         print(line)


'''
需求：封装一个函数，返回这个文件前30条前五列信息
'''


def getList(path, num, col):
    infolist = []
    with open(path, "r", errors="ignore") as f:
        csvReader = csv.reader(f)
        for x in range(num):
            info = next(csvReader)
            infolist.append(info[:col])
    return infolist

print(getList("democsv.csv", 30, 5))
