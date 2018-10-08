#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author：Wayne


import time
import os
from day15.atmpickle.atm import ATM


if __name__ == "__main__":
    ATM.welcome()
    # 如果文件不存在则先进行创建
    if not os.path.exists('atmdb.txt'):
        with open('atmdb.txt', 'w'):
            pass
    # 每次运行程序都从先文件中读取内容
    userDict = ATM.loadATMDict()
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
                print("ATM系统关闭")
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
        # 每当执行完一次操作后，都进行一次文件数据的同步
        ATM.saveDict2File(userDict)
        time.sleep(1)
