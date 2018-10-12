#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：Wayne


import time
import os


# 递归求和：1+2+……+n
def getSumRecu(n):
    if n == 1:
        return 1
    else:
        return getSumRecu(n - 1) + n


# 循环求和：1+2+……+n
def getSumLoop(n):
    res = 0
    for i in range(1, n+1):
        res += i
    return res


# 递归求n!
def getFactorialRecu(n):
    if n == 1:
        return 1
    else:
        return getFactorialRecu(n - 1) * n


# 循环求n！
def getFactorialLoop(n):
    res = 1
    for i in range(1, n+1):
        res *= i
    return res


# 递归遍历目录
def getAllFilesRecu(path, indent=''):
    indent += '\t'
    filesList = os.listdir(path)
    for filename in filesList:
        absFilePath = os.path.join(path, filename)
        if os.path.isdir(absFilePath):
            # print(indent, "目录", filename)
            getAllFilesRecu(absFilePath, indent)
        else:
            # print(indent, "文件：", filename)
            pass


# 循环遍历目录
def getAllFilesLoop(path):
    stack = []
    stack.append(path)
    while len(stack) != 0:
        dirPath = stack.pop()
        filesList = os.listdir(dirPath)
        for filename in filesList:
            absFilePath = os.path.join(path, filename)
            if os.path.isdir(absFilePath):
                # print("目录：", filename)
                stack.append(absFilePath)
            else:
                # print("文件：", filename)
                pass


if __name__ == '__main__':
    gsr1 = time.clock()
    getSumRecu(500)
    gsr2 = time.clock()
    print("递归求1+2+……+500用时为：", (gsr2-gsr1))


    gsl1 = time.clock()
    getSumLoop(500)
    gsl2 = time.clock()
    print("循环求1+2+……+500用时为：", (gsl2 - gsl1))


    gfr1 = time.clock()
    getFactorialRecu(500)
    gfr2 = time.clock()
    print("递归求500!的用时为：", (gfr2-gfr1))


    gfl1 = time.clock()
    getFactorialLoop(500)
    gfl2 = time.clock()
    print("循环求500!的用时为：", (gfl2 - gfl1))


    path = r"/home/wayne/PythonCode/Python1805"


    gafr1 = time.clock()
    getAllFilesRecu(path)
    gafr2 = time.clock()
    print("递归遍历目录的用时为：", (gafr2-gafr1))


    gafl1 = time.clock()
    getAllFilesLoop(path)
    gafl2 = time.clock()
    print("循环遍历目录的用时为：", (gafl2 - gafl1))
