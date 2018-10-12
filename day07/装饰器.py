#! /usr/bin/env python
# -*- coding: utf-8 -*-
# author: Wayne.Chen


'''
什么是装饰器？
在代码运行期间，动态增加功能的方式，我们称之为装饰器
'''


'''
在打印时间之前，给我打印一个分隔符*******当前时间********
要求：不能改变原函数
'''


# print("当前时间".center(50, "*"))
# func()


# def func2():
#     print("当前时间".center(50, "-"))
#     func()


# func2()


'''
登陆功能
'''


'''
最简单的装饰器
装饰器的语法：
# func --> 被装饰的函数
def outer(func):
    def inner()
        # 执行要添加的功能
        # 内函数中，执行被装饰的函数
        return func()
    return inner

注意：对于装饰器分为内函数与外函数，内函数与外函数的函数名都是自己取的
在外函数中outer()中，我们要将被装饰的函数传进去
在内函数中inner()中，我们要添加功能，要执行被装饰的函数，最后要将装饰好的内函数返回【注意：内函数返回时不带小括号】
'''


def deco(func):
    def wrapper():
        print("当前时间".center(50, "-"))
        func()
    return wrapper


@deco
def func():
    print("2018-09-20")


func()


'''
@符号的使用
@装饰器的名字
def 被装饰的函数

@装饰器
def demo():
    pass

@后面跟的是装饰器的名字，添加到被装饰的函数的顶部
'''
