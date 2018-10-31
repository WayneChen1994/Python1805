#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：Wayne

from mysqldemo.atm.user import User
from mysqldemo.atm.card import Card
from mysqldemo.atm.atm import ATM
import time
import json

# username, IdCard, phone, card)
# cardNum, psd, money, islock=False
def user2dict(u):
    print(u)
    cardDict = {"cardNum": u.card.cardNum, "psd": u.card.psd, "money": u.card.money, "islock": u.card.islock}
    return {"username": u.username, "IdCard": u.IdCard, "phone": u.phone, "card": cardDict}


def dict2user(dict1):
    card = Card(dict1["card"]["cardNum"], dict1["card"]["psd"], dict1["card"]["money"], dict1["card"]["islock"])
    return User(dict1["username"], dict1["IdCard"], dict1["phone"], card)


if __name__ == "__main__":
    ATM.welcome()
    userDict = {}
    # 可以将文件中的用户信息全部读出
    with open("user.txt", "r", encoding="utf-8") as f:
        for line in f.readlines():
            user = json.loads(line, object_hook=dict2user)
            userDict[user.card.cardNum] = user

    currentUser = None
    while True:
        print("-"*80)
        print("当前登陆用户：",
              currentUser.username if currentUser else "无")
        print(userDict)
        print("-" * 80)
        time.sleep(1)
        num = ATM.select()
        if num == "1":
            if not currentUser:
                print("登陆")
                currentUser = ATM.login(userDict)
                if currentUser:
                    print("登陆成功")
                else:
                    print("登录失败")
            else:
                print("当前已有用户登陆，请先注销该用户")
        elif num == "2":
            if not currentUser:
                print("开户")
                ATM.kaihu(userDict)
            else:
                print("当前已有用户登陆，请先注销该用户")
        elif num == "3":
            print("查询")
            if currentUser:
                if not currentUser.card.islock:
                    ATM.search(userDict, currentUser.card.cardNum)
                else:
                    print("此卡处于锁定状态，请先解锁")
            else:
                print("当前未登陆")
        elif num == "4":
            print("取款")
            if currentUser:
                if not currentUser.card.islock:
                    if ATM.takeMoney(currentUser):
                        print("取款成功")
                    else:
                        print("取款失败")
                else:
                    print("此卡处于锁定状态，请先解锁")
            else:
                print("当前未登陆")
        elif num == "5":
            print("存款")
            if currentUser:
                if not currentUser.card.islock:
                    if ATM.saveMoney(currentUser):
                        print("存款成功")
                    else:
                        print("存款失败")
                else:
                    print("此卡处于锁定状态，请先解锁")
            else:
                print("当前未登陆")
        elif num == "6":
            if currentUser:
                currentUser = None
                print("当前用户已注销")
            else:
                print("ATM系统关闭,正在保存所有信息……")
                with open("user.txt", "w", encoding="utf-8") as f2:
                    # 获取所有用户
                    for userobj in userDict.values():
                        res = json.dumps(userobj, default=user2dict)
                        f2.write(res)
                        f2.write("\n")
                break
        elif num == "7":
            if currentUser:
                print("锁卡")
                if ATM.lockCard(currentUser):
                    print("锁卡成功")
                else:
                    print("锁卡失败")
            else:
                print("当前未登陆")
        elif num == "8":
            if currentUser:
                print("解锁")
                if ATM.unlockCard(currentUser):
                    print("解锁成功")
                else:
                    print("解锁失败")
            else:
                print("当前未登陆")
        elif num == "9":
            if currentUser:
                if not currentUser.card.islock:
                    print("转账")
                    toUserCardNum = input("请输入对方的银行卡号：")
                    if userDict.get(toUserCardNum):
                        toUser = userDict.get(toUserCardNum)
                        if ATM.transMoney(currentUser, toUser):
                            print("转账成功")
                        else:
                            print("转账失败")
                    else:
                        print("对方卡号不存在，无法转账")
                else:
                    print("此卡处于锁定状态，请先解锁")
            else:
                print("当前未登陆")
        elif num == "10":
            if currentUser:
                if not currentUser.card.islock:
                    print("改密")
                    if ATM.changePassword(currentUser):
                        print("改密成功")
                    else:
                        print("改密失败")
                else:
                    print("此卡处于锁定状态，请先解锁")
            else:
                print("当前未登陆")
        else:
            print("无效的选项，请重新输入")

        time.sleep(1)
