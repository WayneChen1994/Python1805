#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author：Wayne


import random
import time
'''
银行系统：
使用面向对象写，
对象？

卡：
特征：卡号，密码，余额，是否锁卡

用户：
特征：用户名，身份证，手机号，卡
行为：操作ATM机

ATM：
特征：
行为：开户，登陆，查询，存款，取款，转账，改密，锁卡，解锁，退出
'''


class Card:
    def __init__(self, cardId=None, password=None, money=0, isLocked=False):
        self.cardId = cardId
        self.password = password
        self.money = money
        self.isLocked = isLocked



class ATM:
    def __init__(self, allUserInfo={}):
        self.allUserInfo = allUserInfo


    def show_Welcome(self):
        print('''
        **********************
        *                    *
        *  welcome to bank   *
        *                    *
        **********************''')


    def show_Options(self):
        print('''
        **********************
        *  1.登陆   2.开户    *
        *  3.查询   4.取款    *
        *  5.存款   6.退出    *
        *  7.锁卡   8.解锁    *
        *  9.转账   10.改密   *
        **********************''')


    def createCardId(self):
        cardId = ""
        for i in range(6):
            cardId += random.choice([str(x) for x in range(10)])
        return cardId


    def createUser(self, currentUser):
        if not currentUser.isOnline:
            print("开户".center(50, "*"))
            userName = input("请输入您的用户名：")
            userId = input("请输入您的身份证号码：")
            userPhoneNum = input("请输入您的手机号码：")

            while True:
                money = input("请输入预存金额：")
                if money.isdigit() or money[0]=="-" and money[1:].isdigit():
                    if int(money) > 0:
                        break
                    else:
                        print("金额必须是正整数！")
                else:
                    print("金额必须是数字！")

            while True:
                cardPwd = input("请设置银行卡的密码：")
                cardPwd2 = input("请确认银行卡的密码：")
                if cardPwd == cardPwd2:
                    print("银行卡密码设置成功！")
                    break
                else:
                    print("两次输入的密码不一致，请重新设置！")

            print("一切就绪！正在出卡，请稍等……")
            time.sleep(2)
            while True:
                tempCardId = self.createCardId()
                if not self.allUserInfo.get(tempCardId):
                    cardId = tempCardId
                    break
            print("系统为您生成的卡号为：%s".center(50, "=") % cardId)

            userCard = Card(cardId, cardPwd, int(money))
            newUser = User(userName, userId, userPhoneNum, userCard)
            self.allUserInfo[cardId] = newUser
            print("开户成功！请先进行登陆！")

            return newUser
        else:
            print("请先注销当前用户！")
            return currentUser


    def login(self, currentUser):
        print("登陆".center(50, "*"))
        cardId = input("请输入银行卡号：")
        if self.allUserInfo.get(cardId):
            currentUser = self.allUserInfo.get(cardId)
            if not currentUser.isOnline:
                if not currentUser.card.isLocked:
                    count = 3
                    while count > 0:
                        count -= 1
                        cardPwd = input("请输入银行卡密码：")
                        if currentUser.card.password == cardPwd:
                            print("登陆成功！")
                            currentUser.isOnline = True
                            break
                        else:
                            if count > 0:
                                print("密码错误，您还有%d次机会重试密码！"%count)
                    else:
                        currentUser.card.isLocked = True
                        print("三次密码输入错误！此卡已锁！！！请先解锁～")
                else:
                    print("此卡已锁！请先解锁～")
            else:
                print("您已登陆，无需操作！")
        else:
            print("系统查无此卡号！登陆失败！")

        return currentUser

    # 装饰器，用于验证当前操作的用户状态,必须满足用户在线且卡未被锁定才能执行func
    def userAuthenticate(func):
        def wrapper(*args):
            print("args[-1] =", args[-1])
            if args[-1].isOnline:
                if not args[-1].card.isLocked:
                    func(*args)
                else:
                    print("此卡已锁，请解锁后再操作！")
                    return args[-1]
            else:
                print("您尚未登陆！请先进行登陆再操作！")
                return args[-1]
        return wrapper


    @userAuthenticate
    def search(self, currentUser):
        print("查询".center(50, "*"))
        print("您银行卡当前的剩余金额为：%d" % currentUser.card.money)
        return currentUser


    @userAuthenticate
    def takeMoney(self, currentUser):
        print("取款".center(50, "*"))
        while True:
            cash = input("请输入取款金额：")
            if cash.isdigit():
                if int(cash) > 0:
                    if int(cash) <= currentUser.card.money:
                        currentUser.card.money -= int(cash)
                        print("取款成功！")
                        break
                    else:
                        print("余额不足，取款失败！请重试！")
                else:
                    print("取款金额不能是负数！请重新输入！")
            else:
                print("输入有误！请重新输入！")

        return currentUser


    @userAuthenticate
    def saveMoney(self, currentUser):
        print("存款".center(50, "*"))
        while True:
            save = input("请输入存款金额：")
            if save.isdigit():
                if int(save) > 0:
                    currentUser.card.money += int(save)
                    print("存款成功！")
                    break
                else:
                    print("存款金额不能是负数！请重新输入！")
            else:
                print("输入有误！请重新输入！")

        return currentUser


    def logout(self, currentUser):
        print("注销".center(50, "*"))
        if currentUser.isOnline:
            currentUser.isOnline = False
            print("注销登陆。。。")
        else:
            print("您尚未登陆！请先进行登陆！")

        return currentUser

    @userAuthenticate
    def lock(self, currentUser):
        print("1、currentUser ==", currentUser)
        print("锁定".center(50, "*"))
        count = 3
        while count > 0:
            pwd = input("请输入银行卡密码：")
            count -= 1
            if pwd == currentUser.card.password:
                currentUser.card.isLocked = True
                print("锁卡成功！")
                break
            else:
                print("密码错误！锁卡失败！您还有%d次机会！"%count)
        else:
            print("操作失败！")
            print("2、currentUser ==", currentUser)
        return currentUser

    def unlock(self, currentUser):
        print("解锁".center(50, "*"))
        if currentUser.card.isLocked:
            print("您当前所持卡号为%s的银行卡处于锁定状态。。。" % currentUser.card.cardId)
            count = 3
            while count > 0:
                pwd = input("请输入银行卡密码完成解锁：")
                count -= 1
                if pwd == currentUser.card.password:
                    currentUser.card.isLocked = False
                    print("解锁成功！")
                    break
                else:
                    if count > 0:
                        print("密码错误！解锁失败！您还有%d次机会！" % count)
            else:
                print("操作失败！")
        else:
            print("此卡未被锁定！无需操作！")

        return currentUser


    @userAuthenticate
    def transform(self, currentUser):
        print("转账".center(50, "*"))
        to = input("请输入对方卡号：")
        if self.allUserInfo.get(to):
            toUser = self.allUserInfo.get(to)
            while True:
                trans = input("请输入转账金额：")
                if trans.isdigit():
                    if int(trans) > 0:
                        if int(trans) <= currentUser.card.money:
                            currentUser.card.money -= int(trans)
                            toUser.card.money += int(trans)
                            print("转账成功！")
                            break
                        else:
                            print("余额不足！转账失败！请重新输入！")
                    else:
                        print("转账金额必须是正整数！")
                else:
                    print("输入有误！请重新输入！")
        else:
            print("目标卡号不存在！转账失败！")

        return currentUser


    @userAuthenticate
    def setPassword(self, currentUser):
        print("改密".center(50, "*"))
        oldPwd = input("请输入银行卡密码：")
        if oldPwd == currentUser.card.password:
            newPwd = input("请为您的银行卡设置一个新密码：")
            currentUser.card.password = newPwd
            print("修改密码成功！请牢记新密码！")
        else:
            print("密码输入错误！改密操作失败！")

        return currentUser



class User:
    u = None
    def __init__(self, name=None, userId=None, phoneNum=None, card=None, isOnline=False):
        self.name = name
        self.userId = userId
        self.phoneNum = phoneNum
        self.card = card
        self.isOnline = isOnline


    def __str__(self):
        return '''
        ====================
        当前用户信息：
        用户名：%s
        身份证：%s
        手机号：%s
        是否在线：%s
        --------------------
        所持卡信息：
        卡号：%s
        密码：%s
        余额：%d
        是否锁定：%s
        ====================
        ''' % (self.name, self.userId, self.phoneNum, str(self.isOnline), self.card.cardId, self.card.password, self.card.money, str(self.card.isLocked))


    def useATM(self, option, atm):
        if option == "1":
            self.u = atm.login(self)
        elif option == "2":
            self.u = atm.createUser(self)
        elif option == "3":
            print("search1、 self==>", self)
            self.u = atm.search(self)
            print("search2、 self==>", self)
        elif option == "4":
            self.u = atm.takeMoney(self)
        elif option == "5":
            self.u = atm.saveMoney(self)
        elif option == "6":
            self.u = atm.logout(self)
        elif option == "7":
            print("lock1、self ==》", self)
            self.u = atm.lock(self)
            print("lock2、self ==》", self)
        elif option == "8":
            self.u = atm.unlock(self)
        elif option == "9":
            self.u = atm.transform(self)
        elif option == "10":
            self.u = atm.setPassword(self)
        else:
            print("操作失败")
        return self.u



if __name__ == "__main__":
    myATM = ATM()
    myCard = Card()
    myUser = User()
    myUser.card = myCard
    myATM.show_Welcome()
    while True:
        myATM.show_Options()
        choice = input("请选择一项操作（0关闭系统）：")
        time.sleep(random.choice([1, 2]))
        print("-"*50)
        if choice == "0":
            print("ATM机已关闭～")
            break
        print(myUser)
        myUser = myUser.useATM(choice, myATM, myUser)
        print(myUser)
