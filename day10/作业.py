#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: Wayne.Chen


'''
银行系统剩余功能
# 使用之前的方法，完成以下的功能
os.path.join(path1,path2,...)
os.path.dirname(path)
os.path.basename(path)
os.path.split(path)
'''


# 实现os.path.join()
def myJoin(path, *paths):
    # 先将所有路径参数添加到一个列表中
    plist = [path]
    plist.extend(paths)
    # 对列表进行一次反转
    plist.reverse()
    # 定义一个变量保存起始路径（起始路径必须是绝对路径）
    startPath = ''
    # 遍历这个列表
    for p in plist:
        # 当发现第一个是绝对路径的元素就退出循环
        # 反转后的第一个，也就是未反转时的最后一个
        if p.startswith('/'):
            # 当前这个路径就是起始路径
            # 参数中必须至少有一个是绝对路径，否则会报错
            startPath = p
            break
    # 将列表再次反转归位
    plist.reverse()
    # 对原列表进行切片操作，去掉起始路径之前的路径
    plist = plist[plist.index(startPath):]
    # 拼接成字符串
    res = '/'.join(plist)
    return res


# print(myJoin('/aaa', 'bbb', 'ccc', 'ddd', 'eee.py'))


# 实现os.path.dirname()
def myDirname(path): 
    return path[:path.rfind('/')]


# print(myDirname('/aaa/bbb/ccc/ddd.py'))


# 实现os.path.basename()
def myBasename(path):
    return path[path.rfind('/')+1:]


# print(myBasename('/aaa/bbb/ccc/ddd.py'))


import os


print(os.path.split('/'))
print(os.path.split('/.'))
print(os.path.split('/qwer'))
print(os.path.split('.'))
print(os.path.split('./'))
print(os.path.split('..'))


# 实现os.path.split()
def mySplit(path=''):
    index = path.rfind('/')
    if index != -1:
        dirPart = path[:index+1]
        filePart = path[index+1:]
    elif path == '.' or path == '..':
        dirPart = ''
        filePart = path
    return tuple([dirPart, filePart])


print(mySplit('/.'))
print(mySplit('./'))
print(mySplit('/'))
print(mySplit('.'))
