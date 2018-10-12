#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: Wayne.Chen


import os


# 递归遍历目录
def getAllFilesDG(path, indent=""):
    indent += "\t"
    filesList = os.listdir(path)
    for filename in filesList:
        absPath = os.path.join(path, filename)
        if os.path.isdir(absPath):
            print(indent, "目录", filename)
            getAllFilesDG(absPath, indent)
        else:
            print(indent, "文件：", filename)


# 栈模拟遍历目录
def getAllFilesStack(path):
    # 初始化栈
    stack = []
    # 将初始路径放在栈中
    stack.append(path)
    # 判断栈是否为空
    while len(stack) != 0:
        # 将最上面的元素出栈
        dirPath = stack.pop()
        # 列举当前目录下所有的文件【相对路径】
        filesList = os.listdir(dirPath)
        # 遍历
        for filename in filesList:
            # 进行路径拼接
            absPath = os.path.join(path, filename)
            # 判断是否为目录
            if os.path.isdir(absPath):
                print("目录：", filename)
                # 是目录就压栈
                stack.append(absPath)
            else:
                print("文件：", filename)


# 队列模拟遍历目录
import collections


def getAllFilesQueue(path):
    # 初始化一个队列
    queue = collections.deque()
    # 让初始路径入队
    queue.append(path)

    # 判断队列是否为空
    while len(queue) != 0:
        # 取出队列中的头一个路径
        dirPath = queue.popleft()
        # 列出该路径下的所有文件【相对路径】
        filesList = os.listdir(dirPath)

        # 遍历
        for filename in filesList:
            # 进行路径拼接
            absPath = os.path.join(dirPath, filename)
            # 判断是否为目录
            if os.path.isdir(absPath):
                print("目录:", filename)
                # 是目录就入队
                queue.append(absPath)
            else:
                print("文件：", filename)


path = r'/home/wayne/PythonCode/Python1805'
# getAllFilesDG(path)
# getAllFilesStack(path)
getAllFilesQueue(path)
