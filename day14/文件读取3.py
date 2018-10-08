#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：Wayne


'''
常见的一些配置文件，读取可以按行读取
f.readline()：每次读取一行，返回字符串
f.readlines():一次性读取所有行，并且返回一个列表
'''

# with open('set.text', encoding='utf-8') as f:
#     # print(f.readlines())
#     print(f.readline())


'''
需求：分别使用readline与readlines提取配置文件中的数据，并且将数据存储到字典中
'''
# with open('set.txt', encoding='utf-8') as f:
#     infodict = {}
#     infolist = f.readlines()
#     for line in infolist:
#         li = line.split(':')
#         infodict[li[0]] = li[1][:-2]
#
# print(infodict)

# with open('set.txt', encoding='utf-8') as f:
#     infodict = {}
#     while True:
#         lineStr = f.readline()
#         if lineStr == "":
#             break
#         li = lineStr.split(':')
#         infodict[li[0][1:-1]] = li[1][1:-2][1:-1]
#
# print(infodict)


# with open('set.txt', encoding='utf-8') as f:
#     setDict = {}
#     list1 = f.readlines()
#     for x in list1:
#         xlist = x.split(': ')
#         print(xlist)
#         setDict[xlist[0][1:-1]] = xlist[1][1:-3]
#     print(setDict)


with open('set.txt', encoding='utf-8') as f:
    setDict = {}
    while True:
        line = f.readline()
        if line == '':
            break
        else:
            lineList = line.split(': ')
            setDict[lineList[0][1:-1]] = lineList[1][1:-3]

print(setDict)
