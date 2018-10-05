#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author: Wayne.Chen


print()
'''
冒泡排序
第一种实现方式：
li = [32,54,23,12,56,8,45,39]
length = len(li)
while length > 0:
    length -= 1
    index = 0
    while index < length:
        if li[index] > li[index+1]:
            li[index], li[index+1] = li[index+1], li[index]
        index += 1
print(li)
'''

'''
第二种实现方式：
li = [32,54,23,12,56,8,45,39]
for i in range(len(li)-1):
    for j in range(len(li)-1-i):
        if li[j] > li[j+1]:
            li[j], li[j+1] = li[j+1], li[j]
print(li)
'''

'''
第三种实现方式：
li = [32,54,23,12,56,8,45,39]
for i in range(len(li)-1, 0, -1):
    for j in range(i):
        if li[j] > li[j+1]:
            li[j], li[j+1] = li[j+1], li[j]
print(li)
'''

'''
从控制输入一串字符串，要求字符串只能数字字母下划线，并且长度大于等于20，
若不符合条件重新输入，输入完毕之后，要求从控制台输入一个字符，使用自己输入的字符，
来对字符串进行切片，切片完毕之后，并且去掉空串，删除列表中的重复元素。
'''
# while True:
#     input_str = input("请输入一串字符串（只能由数字、字母或下划线组成，并且长度大于等于20）：")
#     if len(input_str) >= 20:
#         for char in input_str:
#             if not ("0"<=char<="9" or "a"<=char<="z" or "A"<=char<="Z" or char=="_"):
#                 print("输入有误！请重新输入！")
#                 break
#         else:
#             break
#     else:
#         print("输入字符串长度小于20，请重新输入！")
#
# achar = input("请输入一个用于切片的字符：")
# alist = input_str.split(achar)
# print("1、切片结果：", alist)
# nullStrCount = alist.count("")
# if nullStrCount > 0:
#     for i in range(nullStrCount):
#         alist.remove("")
# print("2、删除空串结果：", alist)
# 删除列表中重复的元素
# 第一种方式：会修改原来的列表内容，效率最低
# alist.sort()
# length = len(alist)
# lastItem = alist[length-1]
# for i in range(length-2, -1, -1):
#     currentItem = alist[i]
#     if currentItem == lastItem:
#         alist.remove(currentItem)
#     else:
#         lastItem = currentItem
# print("3、去重处理结果：", alist)
# 第二种方式：创建一个新的空列表，将原列表遍历一遍，若当前元素在新列表中没有，则添加进去，效率次之
# resList = []
# for x in alist:
#     if x not in resList:
#         resList.append(x)
# print("3、去重处理结果：", resList)
# 第三种方式：通过set集合的特性实现去重，简单直接，效率最高
# alist = list(set(alist))
# print("3、去重处理结果：", alist)

'''
从控制台输入一个字符串，实现字符串的反转
str1 = input("请输入一个字符串：")
li = list(str1)
li.reverse()
str2 = "".join(li)
print("反转后的结果：" + str2)
'''


# 使用for循环打印图形
# *
# **
# ***
# ****
# *****
# row = 1
# for i in range(5):
#     print("*"*row)
#     row += 1
#     if row == 6:
#         break

'''
写一个双色球彩票系统，
1.开始游戏
2.用户可以充值金额，
3.一张彩票是两块钱，用户可以选择买多少张彩票，
4.判断用户的金额是否充足，若金额不够则提示充值金额，
若用户不愿充值则退出游戏。
5.若金额充足，系统可以随机产生一组数据
，一组彩票数据有六位数，这六位数的的取值范围是0和1。
6.用户输入猜测的数据【必须提示输入6位0/1，
若位数不够或者是其他字符则提示重新输入】
7.若是猜对，则打印”恭喜你中大奖了“，
【猜中的时候，奖金是购买金额的100倍】
8.若没猜中则打印”继续加油！“。
9.用户可以选择继续买票或者是退出。
买票和退出的时候要求打印剩余金额。
'''
import random
import time
print("开始游戏".center(50, "*"))
base_money = int(input("请输入起始金额："))
while True:
    amount = int(input("一张彩票需要2元，您有%d元，需要购买多少张?" % (base_money)))
    if base_money - amount * 2 < 0:
        choice = input("余额不足，是否充值？(yes/no)")
        if choice == "no":
            print("当前剩余金额为%d元，欢迎下次再来！" % base_money)
            break
        elif choice == "yes":
            print("当前剩余金额为：%d," % base_money, end="")
            add_money = int(input("请输入充值金额："))
            base_money += add_money
        else:
            print("输入错误！")
    else:
        base_money -= amount * 2
        print("成功购买了%d张彩票，花费了%d元，剩余金额为%d元" % (amount, amount * 2, base_money))
        print("进行摇号".center(50, "="))
        time.sleep(2)
        res_str = ""
        for x in range(6):
            perNum = random.choice(["0", "1"])
            res_str += perNum
        print("作弊码：", res_str)
        while True:
            guess_str = input("请输入猜测的彩票号码(6位只能由0或1组成的数字)：")
            if len(guess_str) != 6:
                print("输入错误，彩票号码应为6位数！")
            else:
                for a in guess_str:
                    if a not in ["0", "1"]:
                        print("输入错误，彩票号码只由0或1组成！")
                        break
                else:
                    print("正在开奖".center(50, "&"))
                    time.sleep(2)
                    print("开奖结果：%s" % res_str)
                    time.sleep(2)
                    if res_str == guess_str:
                        award = amount * 2 * 100
                        base_money += award
                        print("恭喜中奖！奖金为购买金额的100倍：%d元！剩余金额为%d元" %
                              (award, base_money))
                        break
                    else:
                        print("可惜没中奖！继续努力……")
                        break
        isContinue = input("是否继续(yes/no)?")
        if isContinue == "no":
            print("当前剩余金额为%d元，欢迎下次再来！" % base_money)
            break
        elif isContinue == "yes":
            print("正在为您安排，请稍等……")
            time.sleep(2)
        else:
            print("输入有误！默认继续进行，请稍后……")
            time.sleep(2)

print("游戏结束".center(50, "*"))
