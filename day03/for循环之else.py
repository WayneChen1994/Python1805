#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: Wayne.Chen


'''
语法：
for x in 序列：
    语句块1
else:
    语句块2
当整个循环正常执行结束之后，则执行else下面的语句块2，若是通过break退出的，则不会执行else语句
'''


# for x in range(1, 100):
#     if x % 20 == 0:
#         continue
#     else:
#         print(x)
# else:
#     print("end")


'''
需求：从控制台输入六位的银行卡密码，判断输入的密码是否合法：
1、长度6位
2、密码取值0~9
并且打印提示
'''


# pwd = input("请输入六位的银行卡密码：")
# pwd_len = 0
# for x in pwd:
#     pwd_len += 1
# if pwd_len == 6:
#     for char in pwd:
#         if char < "0" or char > "9":
#             print("密码不合法,存在非法字符！")
#             break
#     else:
#         print("密码合法")
# else:
#     print("密码的长度不正确")


# psd = input("请输入六位的银行卡密码：")
# length = 0
# for x in psd:
#     length += 1
#     if x >= "0" and x <= "9":
#         pass
#     else:
#         print("密码不合法")
#         break
# else:
#     if length != 6:
#         print("密码长度不合法")
#     else:
#         print("密码合法")
