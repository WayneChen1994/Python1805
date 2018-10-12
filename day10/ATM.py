#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: Wayne.Chen


import time
import random


# 定义一个字典保存所有的用户信息
allInfo = {}


def show_Welcome():  # 打印欢迎信息
    print('''
    **********************
    *                    *
    *  welcome to bank   *
    *                    *
    **********************''')


def atm_Options():  # 打印选项
    print('''
    **********************
    *  1.登陆   2.开户    *
    *  3.查询   4.取款    *
    *  5.存款   6.退出    *
    *  7.锁卡   8.解锁    *
    *  9.转账   10.改密   *
    **********************''')


def createCardID():  # 生成随机六位的卡号
    cardID = ""
    for i in range(6):
        cardID += random.choice([str(x) for x in range(10)])
    return cardID


def show_UserInfo(cardID):  # 打印用户信息
    print("*" * 100)
    print("卡号：%s" % cardID, end=" ")
    print("用户名：%s" % allInfo.get(cardID).get("name"), end=" ")
    print("身份证：%s" % allInfo.get(cardID).get("id"), end=" ")
    print("电话号码：%s" % allInfo.get(cardID).get("phone"), end=" ")
    print("地址：%s" % allInfo.get(cardID).get("address"), end=" ")
    print("账户余额：%d" % allInfo.get(cardID).get("money"))
    print("*" * 100)


def createUser(cardID):  # 开户
    if cardID != -1 and allInfo.get(cardID).get("isOnline"):
        print("请先注销当前用户：%s" % (allInfo.get(cardID).get("name")))
    else:
        uname = input("请输入用户名：")
        uid = input("请输入身份证号码：")
        phone = input("请输入电话号码：")
        address = input("请输入地址：")
        cardID = ""
        while True:
            # 生成临时卡号
            tempCardID = createCardID()
            # 用生成的卡号到字典中取值，若取不到说明是新卡号
            if allInfo.get(tempCardID) is None:
                cardID = tempCardID
                break
        time.sleep(random.choice([1, 2, 3]))
        print("系统为您生成的卡号是：%s".center(50, "=") % cardID)
        while True:
            upwd = input("请设置您的银行卡密码：")
            upwd2 = input("请确认银行卡密码：")
            if upwd == upwd2:
                print("密码设置成功！")
                break
            else:
                print("两次密码输入不一致，请重新输入！")
        while True:
            money = input("请输入预存余额：")
            if money.isdigit() and int(money) > 0:
                break
            else:
                print("非法的操作！请重新输入！")
        # 先以一个字典的形式，保存一个用户的所有信息
        userInfo = {}
        userInfo["name"] = uname
        userInfo["id"] = uid
        userInfo["phone"] = phone
        userInfo["address"] = address
        userInfo["money"] = int(money)
        userInfo["pwd"] = upwd
        userInfo["isLocked"] = False
        userInfo["isOnline"] = False
        # 将卡号和“用户”保存进全局字典中
        allInfo[cardID] = userInfo
        print("开户操作完成,请先进行登陆".center(50, "-"))

    return cardID


def login(cardID):    # 登陆
    if cardID == -1 or not allInfo.get(cardID).get("isOnline"):  # 尚未登陆的才能进行登陆
        ucard = input("请输入您的银行卡号：")
        if allInfo.get(ucard) is None:
            print("卡号不存在！登陆失败！")
        else:
            count = 3
            while count > 0:
                count -= 1
                upwd = input("请输入密码：")
                if allInfo.get(ucard).get("pwd") == upwd:
                    print("登陆成功！")
                    cardID = ucard
                    allInfo.get(cardID)["isOnline"] = True
                    break
                else:
                    if count > 0:
                        print("密码错误！登陆失败～您还有%d次机会" % count)
            else:
                print("您已经连续三次输入了错误的密码！！！此卡%s已被锁定！！！" % ucard)
                allInfo.get(ucard)["isLocked"] = True
    else:
        print("您已登陆，无需操作～")
    return cardID


def searchInfo(cardID):  # 查询
    if cardID != -1 and allInfo.get(cardID).get("isOnline"):
        if allInfo.get(cardID).get("isLocked"):
            print("此卡处于锁定状态！！！请先解锁后再操作～")
        else:
            show_UserInfo(cardID)
    else:
        # 表示尚未登陆，需先登陆
        print("请先完成登陆再操作！".center(50, "~"))


def getMoney(cardID):   # 取款
    if cardID != -1 and allInfo.get(cardID).get("isOnline"):
        if allInfo.get(cardID).get("isLocked"):
            print("此卡处于锁定状态！！！请先解锁后再操作～")
        else:
            # 用户的当前余额
            current_Money = allInfo.get(cardID).get("money")
            while True:
                num = input("请输入取款金额:")
                if num.isdigit():
                    if int(num) < 0:
                        print("取款金额不能为负数！")
                    elif int(num) > current_Money:
                        print("余额不足，取款失败！")
                    else:
                        allInfo.get(cardID)["money"] = current_Money - int(num)
                        print("取款成功！当前用户的余额为：%s" %
                              allInfo.get(cardID)["money"])
                        break
                else:
                    print("取款金额必须是正数！")
    else:
        print("请先完成登陆再操作！".center(50, "~"))


def saveMoney(cardID):   # 存款
    if cardID != -1 and allInfo.get(cardID).get("isOnline"):
        if allInfo.get(cardID).get("isLocked"):
            print("此卡处于锁定状态！！！请先解锁后再操作～")
        else:
            # 用户的当前余额
            current_Money = allInfo.get(cardID).get("money")
            while True:
                num = input("请输入存款金额:")
                if num.isdigit():
                    if int(num) < 0:
                        print("存款金额不能为负数！")
                    else:
                        allInfo.get(cardID)["money"] = current_Money + int(num)
                        print("存款成功！当前用户的余额为：%s" %
                              allInfo.get(cardID)["money"])
                        break
                else:
                    print("存款金额必须是正数！")
    else:
        print("请先完成登陆再操作！".center(50, "~"))


def lockCard(cardID):   # 锁卡
    if cardID != -1 and allInfo.get(cardID).get("isOnline"):
        if allInfo.get(cardID).get("isLocked"):
            print("该银行卡已经锁定，无需操作～")
        else:
            allInfo.get(cardID)["isLocked"] = True
            print("系统已完成锁卡操作！")
    else:
        print("请先完成登陆再操作！".center(50, "~"))


def unLockCard(cardID):   # 解锁
    if cardID != -1 and allInfo.get(cardID).get("isOnline"):
        if not allInfo.get(cardID).get("isLocked"):
            print("该银行卡并未锁定，无需操作～")
        else:
            uid = input("解锁需要核对本人身份证，请仔细核对后输入：")
            if allInfo.get(cardID).get("id") == uid:
                allInfo.get(cardID)["isLocked"] = False
                print("核对成功，系统已完成解锁操作！")
            else:
                print("身份证核对失败，请查证后重新进行解锁操作！")
    else:
        print("请先完成登陆再操作！".center(50, "~"))


def logout(cardID):  # 注销，而不是退出整个程序,不然没办法实现用户的切换，毕竟没有做数据的持久化处理
    if cardID != -1 and allInfo.get(cardID).get("isOnline"):
        allInfo.get(cardID)["isOnline"] = False  # 修改成离线状态
        cardID = -1
    else:
        print("您尚未登陆，无需操作～")
    return cardID


def transferMoney(cardID):  # 转账
    if cardID != -1 and allInfo.get(cardID).get("isOnline"):
        if allInfo.get(cardID).get("isLocked"):
            print("此卡处于锁定状态！！！请先解锁后再操作～")
        else:
            while True:
                tran = input("请输入您要转账的金额：")
                if not tran.isdigit():
                    print("转账的金额必须是正整数！")
                else:
                    if int(tran) <= 0 or int(tran) > allInfo.get(cardID).get("money"):
                        print("无法完成转账操作！")
                    else:
                        toCard = input("请输入对方的卡号：")
                        if allInfo.get(toCard) is None:
                            print("系统查无此卡号，转账失败！")
                        else:
                            allInfo.get(cardID)["money"] -= int(tran)
                            allInfo.get(toCard)["money"] += int(tran)
                            print("转账成功！！！")
                            break
    else:
        print("请先完成登陆再操作！".center(50, "~"))


def changePasswd(cardID):   # 改密
    if cardID == -1 or not allInfo.get(cardID).get("isOnline"):
        print("请先完成登陆再操作！")
    elif allInfo.get(cardID).get("isLocked"):
        print("此卡处于锁定状态！！！请先解锁后再操作～")
    else:
        while True:
            newpwd = input("请输入新密码：")
            newpwd2 = input("请确认新密码：")
            if newpwd == newpwd2:
                allInfo.get(cardID)["pwd"] = newpwd
                print("密码修改成功！")
                break
            else:
                print("密码输入不一致！请重新设置！")


# 程序的具体流程
show_Welcome()
cid = -1
while True:
    atm_Options()
    if cid != -1 and allInfo.get(cid).get("isOnline"):
        print("%s正在使用ATM机".center(50, "+") % allInfo.get(cid).get("name"))
    else:
        print("ATM机，冷冷清清，无人问津～".center(50, "+"))
    choice = input("请输入操作序号：")
    if choice == "1":   # 登陆
        cid = login(cid)
    elif choice == "2":  # 开户
        cid = createUser(cid)
    elif choice == "3":  # 查询
        searchInfo(cid)
    elif choice == "4":  # 存款
        getMoney(cid)
    elif choice == "5":  # 取款
        saveMoney(cid)
    elif choice == "6":  # 退出
        if cid != -1:
            print("注销当前用户：%s" % (allInfo.get(cid).get("name")))
            cid = logout(cid)
        else:
            # 若当前没有用户登陆，则是程序结束
            print("当前没有用户在操作，系统关闭～")
            break
    elif choice == "7":  # 锁卡
        lockCard(cid)
    elif choice == "8":  # 解锁
        unLockCard(cid)
    elif choice == "9":  # 转账
        transferMoney(cid)
    elif choice == "10":  # 改密
        changePasswd(cid)
    else:
        print("非法的操作！请重新输入！")
    time.sleep(random.choice([1, 2, 3]))
    print("用户信息一览表".center(100, "#"))
    print(allInfo)
    print("#" * 100)
