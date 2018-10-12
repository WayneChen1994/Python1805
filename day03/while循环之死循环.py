#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: Wayne.Chen


# 1~160，输入年龄非法，请重新输入
# while True:
#     age = int(input("请输入您的年龄："))
#     if 0 < age <= 160:
#         print("ok没毛病")
#         break
#     else:
#         print("输入年龄非法！请重新输入")
# print("age =", age)


'''
伪登录：
用户名：admin 密码：123456
用户输入密码，密码输入两次错误提示“只剩一次机会了”，
输入三次错误，提示“卡被锁了”
若输入密码正确，提示“登陆成功”
'''


err = 0
while err < 3:
    pwd = input("请输入您的银行卡密码：")
    err += 1
    if pwd == "123456":
        print("登陆成功")
        break
    else:
        if err == 1:
            print("输入密码不正确，请重新输入。。。")
        elif err == 2:
            print("只剩一次机会了")
        elif err == 3:
            print("卡被锁了")
