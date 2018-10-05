#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author：zhangjiao
import random
from day13.银行系统.card import Card
from day13.银行系统.user import User


class ATM:

    @staticmethod
    def welcome():
        print('''
        **********************
        *                    *
        *  welcome to bank   *
        *                    *
        **********************
        ''')

    # 选择操作
    @staticmethod
    def select():
        print('''
        **********************
        *  1.登陆   2.开户    *
        *  3.查询   4.取款    *
        *  5.存款   6.退出    *
        *  7.锁卡   8.解锁    *
        *  9.转账   10.改密   *
        **********************
        ''')
        num = input("请输入您要操作的选项：")
        return num

    @staticmethod
    def getCardNum(cardNumList):
        while True:
            num = ""
            for x in range(6):
                num += str(random.randrange(10))
            # 获取所有的卡号，并且判断，生成新的卡号是已经否存在
            # 若存在，则证明卡号重复，则重新生成，若不存在，则
            # 生成卡号未重复。
            if num in cardNumList:
                continue
            else:
                break
        return num


    @classmethod
    def kaihu(cls,userDict):
        #用户名 身份证 手机号  卡
        username = input("请输入用户名：")
        idCard = input("请输入身份证号码：")
        phone = input("请输入手机号码：")
        #卡号 密码 余额  是否锁卡
        psd = input("请设置卡的密码：")
        psd2 = input("请确认密码：")
        if psd !=psd2:
            print("两次输入密码不一致，开户失败！")
            return
        else:
            while 1:
                money = int(input("请输入预存余额："))
                if money>0:
                    break
                else:
                    print("输入的金额不合法，请重新输入...")
        cardNumList = list(userDict)
        cardNum = cls.getCardNum(cardNumList)
        card = Card(cardNum,psd,money)
        user = User(username,idCard,phone,card)
        userDict[cardNum] = user
        print("开户成功，您的卡号为%s，请牢记。。。"%cardNum)
        return


    @staticmethod
    def login(userDict):
        cardnum = input("请输入卡号：")
        # 获取用户
        user = userDict.get(cardnum)
        # 用户存在
        if user is not None:
            # 卡号是否被锁定，若卡未被锁定
            if not user.card.islock:
                # 输入密码
                n = 0
                while True:
                    if n > 2:
                        print("密码输入已经超过三次，卡已锁定。。。")
                        # 锁定卡
                        user.card.islock = True
                        break
                    psd = input("请输入密码：")
                    n += 1
                    # 密码正确
                    if psd == user.card.psd:
                        print("恭喜你登陆成功！")
                        return cardnum
                    else:
                        print("密码错误，您还有%d机会"%(3-n))
            else:
                print("卡已被锁定，请解锁后登陆。。。")
        else:
            print("卡号不存在，请查证后登陆。。。")
