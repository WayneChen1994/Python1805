#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：Wayne

'''
使用while循环遍历list，tuple，dict，set
使用try……except……
'''

from typing import Iterable

# 传入的参数若是一个可迭代类型的对象，则将其遍历打印
def printIterByWhile(obj):
    # 判断所传参数是否为可迭代对象
    if isinstance(obj, Iterable):
        # 进一步判断该可迭代对象是否为字典，因为字典需要同时遍历Key和Value
        if isinstance(obj, dict):
            aiter = iter(obj.items())
        else:
            aiter = iter(obj)
        while True:
            try:
                # 迭代输出
                print(next(aiter))
            except StopIteration:
                # 一旦捕捉到此异常，则说明遍历结束，直接break跳出循环
                break
    else:
        print("所给参数不是可迭代类型")


if __name__ == "__main__":
    alist = [x for x in range(39)]
    atuple = (y for y in range(39))
    aset = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
    adict = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
    astr = "qwertyuiopasdfghjklzxcvbnm"
    printIterByWhile(alist)
    printIterByWhile(atuple)
    printIterByWhile(aset)
    printIterByWhile(adict)
    printIterByWhile(astr)
    printIterByWhile(123)
