#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author：Wayne


import random
import json
from day15.atmjson.models import Card, User


class ATM:
    @staticmethod
    def saveDict2Json(dic):
        with open('atmdb.txt', 'w') as f:
            json.dump(dic, f)


    @staticmethod
    def loadJson2Dict():
        with open('atmdb.txt', 'r') as f:
            adict = json.load(f)
        return adict


    @staticmethod
    def welcome():
        print('''
        **********************
        *                    *
        *  welcome to bank   *
        *                    *
        **********************''')


    @staticmethod
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


    @staticmethod
    def getCardNum(cardNumList):
        while True:
            cardNum = ""
            for i in range(6):
                cardNum += random.choice([str(x) for x in range(10)])
            if cardNum not in cardNumList:
                return cardNum


    @classmethod
    def kaihu(cls, userDict):
        username = input("请输入用户名：")
        idCard = input("请输入身份证号码：")
        phone = input("请输入手机号码：")
        psd = input("请设置卡的密码：")
        psd2 = input("请确认密码：")
        if psd != psd2:
            print("两次输入密码不一致，开户失败！")
            return
        else:
            while  1:
                money = int(input("请输入预存余额："))
                if money > 0:
                    break
                else:
                    print("输入的金额不合法，请重新输入")
        cardNumList = list(userDict)
        cardNum = ATM.getCardNum(cardNumList)
        card = Card(cardNum, psd, money)
        user = User(username, idCard, phone, card.__dict__)
        userDict[cardNum] = user.__dict__
        print("开户成功，您的卡号为%s，请牢记。。。"%cardNum)
        return


    @classmethod
    def login(cls, userDict):
        cardNum = input("请输入银行卡号：")
        if cardNum not in list(userDict):
            print("卡号不存在")
            return
        count = 3
        while count > 0:
            psd = input("请输入银行卡密码：")
            count -= 1
            if psd != userDict.get(cardNum).get('card').get('psd'):
                if count > 0:
                    print("密码不正确,还有%d次操作机会！"%count)
            else:
                return userDict.get(cardNum)
        else:
            print("三次密码输入错误，自动锁定此卡！")
            userDict.get(cardNum).get('card')['islock'] = True
            return


    @classmethod
    def search(cls, userDict, cardNum):
        extraMoney = userDict.get(cardNum).get('card').get('money')
        print("您的剩余金额为：%d元" % extraMoney)


    @classmethod
    def takeMoney(cls, currentUser):
        take = int(input("请输入取款金额："))
        if 0 < take <= currentUser.get('card').get('money'):
            currentUser.get('card')['money'] -= take
            return True
        else:
            return False


    @classmethod
    def saveMoney(cls, currentUser):
        save = int(input("请输入存款金额："))
        if save > 0:
            currentUser.get('card')['money'] += save
            return True
        else:
            return False


    @classmethod
    def lockCard(cls, currentUser):
        if not currentUser.get('card').get('islock'):
            psd = input("请输入银行卡密码：")
            if currentUser.get('card').get('psd') == psd:
                currentUser.get('card')['islock'] = True
                print("密码正确")
                return True
            else:
                print("密码错误")
                return False
        else:
            print("此卡已锁，无需再次锁定")
            return False


    @classmethod
    def unlockCard(cls, currentUser):
        if currentUser.get('card').get('islock'):
            psd = input("请输入银行卡密码：")
            if currentUser.get('card').get('psd') == psd:
                currentUser.get('card')['islock'] = False
                print("密码正确")
                return True
            else:
                print("密码错误")
                return False
        else:
            print("此卡未被锁定，无需解锁")
            return False


    @classmethod
    def transMoney(cls, currentUser, toUser):
        trans = int(input("请输入转账金额："))
        if trans >= 0 and trans <= currentUser.get('card').get('money'):
            currentUser.get('card')['money'] -= trans
            toUser.get('card')['money'] += trans
            return True
        else:
            print("转账金额非法")
            return False


    @classmethod
    def changePassword(cls, currentUser):
        oldPsd = input("请输入原来的密码：")
        if currentUser.get('card').get('psd') == oldPsd:
            newPsd = input("请输入新的密码：")
            currentUser.get('card')['psd'] = newPsd
            return True
        else:
            print("原密码验证失败")
            return False


'''
{'001001': {'username': 'wayne', 'idCard': '123', 'phone': '123', 'card': {'cardNum': '001001', 'psd': '123', 'money': 123, 'islock': False}}, '222222': {'username': 'aaaa', 'idCard': '222', 'phone': '222', 'card': {'cardNum': '222222', 'psd': '222', 'money': 222, 'islock': False}}}
'''
