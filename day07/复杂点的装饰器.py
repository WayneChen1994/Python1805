#! /usr/bin/env python
# -*- coding: utf-8 -*-
# author: Wayne.Chen


# def deco(f):
#     def wrapper(age):
#         if age > 160 or age < 0:
#             print("输入不合法。。。")
#             return
#         else:
#             f(age)
#     return wrapper


# @deco
# def func2(age):
#     if age < 18:
#         print("未成年人禁止进入")
#     else:
#         print("欢迎光临！！！")


# func2(18)
# func2(-20)
# func2(190)


'''
需求：伪登陆
用户名的长度与密码长度都为6位，并且用户名和密码都是数字
若不符合则打印输入非法
'''


def deco(func):
    def wrapper(user, psd):
        if len(user) == 6 and len(psd) == 6 \
                and user.isdecimal() and psd.isdecimal():
            func(user, psd)
        else:
            print("输入非法")
    return wrapper


@deco
def login(user, psd):
    if user == "333999" and psd == "123456":
        print("登陆成功")
    else:
        print("登陆失败")


uname = input("请输入用户名：")
upsd = input("请输入密码：")
login(uname, upsd)


'''
装饰器的优点：
在实际开发过程中，我们可以使用装饰器做到在不修改别人创建的函数的情况下，添加或者修改某些功能
'''


'''
复杂点的装饰器的定义：
def outer(f):
    def inner(参数列表):
        # 添加的功能
        f(参数列表)
    return inner
注意：当我们装饰的函数需要参数的时候，我们需要将被装饰的函数名传递给外函数，需要的参数传递给内函数，最后将装饰好的内函数通过外函数返回。
'''
