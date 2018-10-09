#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：Wayne


import csv


'''
语法：
try:
    语句块【有可能发生错误的语句块】
except 捕捉错误类型:【所有的错误都捕捉】
    语句块【错误处理语句】
finally:【无论语句是否发生错误，都会执行此语句】
    语句块

代码执行的顺序：
首先执行try中的语句块，若try中的语句出现异常，则try中的语句块不再执行，执行except对应异常下面的语句
except语句执行完毕之后，执行finally下面的语句块

调用栈：
当代码出现错误的时候，若没有进行错误的捕捉
错误会向上进行抛，直到抛给Python解释器为止

如何查看错误信息？
查看错误的时候先看错误类型，以及提示
从下往上看，看自己的代码，【行数，文件】，进行查找
'''


def func(a, b):
    try:
        res = a / b
        print("@@@@@@@@")
        return res
    # except ZeroDivisionError as e:
    #     print(e)
    # except TypeError as t:
    #     print(t)
    except Exception as b: # 多态的使用
        print(b)
    finally:
        pass


def getList(path, num, col):
    infolist = []
    with open(path, "r", errors="ignore") as f:
        csvReader = csv.reader(f)
        for x in range(num):
            try:
                info = next(csvReader)
                infolist.append(info[:col])
            except StopIteration:
                return infolist


if __name__ == "__main__":
    # print(func(1, 2))
    # print(func(1, 0))
    # print(func("1", "2"))
    # print("*********")

    print(getList("democsv.csv", 300,5))
