#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Wayne.Chen
print()
'''
计算1~100以内所有能被3或者17整除的数的和
sum = 0
for i in range(1, 101):
    if i % 3 == 0 or i % 17 == 0:
        sum += i
print(sum)
'''

'''
计算100~999的水仙花数的个数
count = 0
num = 100
while num <= 999:
    a = num //100
    b = num //10 % 10
    c = num % 10
    if a**3+b**3+c**3 == num:
        count += 1
    num += 1
print(count)
'''

'''
计算五位数中回文数的个数：
count = 0
for i in range(10000, 100000):
    wan = i // 10000
    ge = i % 10
    qian = i // 1000 % 10
    shi = i // 10 % 10
    if wan == ge and qian == shi:
        count += 1
print(count)
'''

'''
计算200~500以内能被7整除但不是偶数的数的个数。
count = 0
for i in range(200, 501):
    if i % 7 == 0 and i % 2 != 0:
        count += 1
print(count)
'''

'''
押宝游戏：

开始游戏 -> 投入赌金【一次性投入】 -> 

循环  ：押宝【5块钱一次】 -> 开奖  --》中奖/未中奖 --》用户输入是否继续 【当余额不足则自动退出游戏】
import random
print("押宝游戏开始")
money = int(input("请投入您的一次性赌金："))
while money > 0:
    if money >= 5:
        print("押宝5块钱一次，正在开奖……")
        money -= 5
        res = random.choice([True, False])
        if res:
            print("中奖了！")
        else:
            print("很遗憾，没中奖……")
    if money >= 5:
        your_choice = input("您的当前余额为%s元，是否继续？"%money)
        if your_choice == "是":
            continue
        elif your_choice == "否":
            print("欢迎再来玩")
            break
        else:
            print("输入有误，游戏结束！")
            break
    else:
        print("您的余额为%d元，不足5元，充钱才能继续！"%money)
        break
'''

'''
百钱买百鸡，现有100文钱，公鸡5文钱一只，母鸡3文钱一只，小鸡一文钱3只，要求：公鸡，母鸡，小鸡都要有，
把100文钱买100只鸡，买的鸡是整数。多少只公鸡，多少只母鸡多少只小鸡？
for cock in range(1, 99):
    for hen in range(1, 100-cock):
        for chick in range(1, 101-cock-hen):
            if (cock+hen+chick == 100) and (cock*5+hen*3+chick*(1/3) == 100):
                print("公鸡：%d只，母鸡：%d只，小鸡：%d只" % (cock, hen, chick))
'''



'''
打印九九乘法表：
'''
row = 0
for x in range(1, 10):
    if row != 0:
        print("        " * row, end="")
    row += 1
    left_num = 10 - x
    for y in range(1, 10):
        right_num = 10 - y
        if left_num >= right_num:
            print("%d=%dx%d" % (left_num*right_num, left_num, right_num), end="\t")
    print()

