#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Wayne.Chen


'''
闰年：
year = int(input("请输入一个年份:"))
if (year % 100 != 0 and year % 4 == 0) or (year % 100 == 0 and year % 400 == 0):
    print(str(year) + "年是闰年")
else:
    print(str(year) + "年不是闰年")
'''


'''
水仙花数：
num = int(input("请输入一个三位数："))
a = num // 100
b = num //10 % 10
c = num % 10
if a**3+b**3+c**3 == num:
    print(str(num)+"是水仙花数")
else:
    print(str(num) + "不是水仙花数")
'''


'''
回文数：
num = int(input("请输入一个五位数："))
A = num // 10000
B = num // 1000 % 10
b = num // 10 % 10
a = num % 10
if A==a and B==b:
    print(str(num)+"是回文数")
else:
    print(str(num) + "不是回文数")
'''


'''
摇色子游戏：
import random
your_choice = input("押大还是押小？")
result = random.choice([1,2,3,4,5,6])
print("得到的点数为：", result)
if (result in [1,2,3] and your_choice=="小") or (result in [4,5,6] and your_choice=="大"):
    print("押中了！庄家喝酒。。。。")
else:
    print("没押中！先干为敬。。。")
'''
