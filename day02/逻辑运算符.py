#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Wayne.Chen


print()


'''
and ==> 与运算
使用and连接的时候，只有所有的结果都为True的时候，结果才为True

or ==> 或运算
使用or运算连接的时候，只要有一个结果为True，则结果就为True

not ==> 非运算
非运算为单目运算，将True改为False，将False改为True

注意：在Python中表示False的取值：
False、0、None、空序列对象

优先级最高的not, 其次是and, 最后是or

短路原则：
当使用and连接的时候，只要有一个表达式的取值为False，则此结果都为False，后面表达式不需要进行计算
比如：判空处理

当使用or连接的时候，只要有一个表达式的取值为True，则此结果都为True，后面的表达式不再进行计算
'''


# print(True and True)
# print(True and 1 and 2)
# print(1 and True)
# print(True and 0)
# print(True and None)
# print(True and False)


# print(False or False)
# print(False or 0)
# print(False or None)
# print(False or 1)
# print(False or True or 0)


# print(not 0)
# print(not None)
# print(not False)


# print(not -1)


print(False and not 0 or 9)
print(False or 0 and 9)
