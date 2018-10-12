#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: Wayne.Chen


'''
数据如何存储？
'''


import random
import time


def welcome(): 
    print('''
    **********************
    *                    *
    *  welcome to bank   *
    *                    *
    **********************''')


def select(): 
    print('''
    **********************
    *  1.登陆   2.开户    *
    *  3.查询   4.取款    *
    *  5.存款   6.退出    *
    *  7.锁卡   8.解锁    *
    *  9.转账   10.改密   *
    **********************''')
    num = input("请输入您要操作的选项：")
    return num


def getCardNum(alluser):
    while True:
        num = ""
        for x in range(6):
            num += str(random.randrange(10))
        # 获取所有的卡号，并且判断生成新的卡号是否已经存在
        # 若存在，则证明卡号重复，需重新生成
        # 若不存在，则生成卡号未重复
        if num in list(alluser):
            continue
        else:
            break
    return num


def kaihu(alluser):
    idCard = input("请输入身份证号码：")
    phone = input("请输入电话号码：")
    user = input("请设置用户名：")
    psd = input("请设置密码：")
    psd2 = input("请确认密码：")
    if psd != psd2:
        print("两次密码输入不一致，注册失败。。。")
        return
    else:
        while True:
            money = int(input("请输入预存余额："))
            if money < 0:
                print("输入有误，请重新输入")
            else:
                break
    cardNum = getCardNum(AllUserDict)
    return {"idCard":idCard, "phone":phone, "user":user, "psd":psd, "money":money, "cardNum":cardNum}


def login(allDict):
    cardnum = input("请输入卡号：")
    psd = input("请输入密码：")
    userdict = allDict.get(cardnum)
    if userdict is None:
        print("该用户不存在，请开户后登陆。。。")
    else:
        if userdict.get("psd") == psd:
            print("恭喜你登陆成功")
            return cardnum
        else:
            print("密码错误，请查证后登陆。。。")


def search(alluser, cardnum):
    return alluser.get(cardnum).get("money")


welcome()
AllUserDict = {}
isLogin = None


while True:
    time.sleep(1)
    num = select()
    if num == "1":
        print("登陆")
        isLogin = login(AllUserDict)
    elif num == "2":
        print("开户")
        userdict = kaihu()
        if userdict is not None:
            AllUserDict[userdict.get("cardNum")] = userdict
            print("恭喜你开户成功，您的卡号为%s，请牢记。。。" % userdict.get("cardNum"))
    elif num == "3":
        print("查询")
        if isLogin is None:
            print("请登陆后查询。。。")
        else:
            res = search(AllUserDict, isLogin)
            print("您目前的余额为%d" % res)
    elif num == "4":
        print("取款")
    elif num == "5":
        print("存款")
    elif num == "6":
        print("退出")
