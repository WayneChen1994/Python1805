#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author：zhangjiao
from day13.银行系统.atm import ATM
import time



if __name__ == "__main__":
    ATM.welcome()
    userDict={}
    while True:
        print(userDict)
        time.sleep(1)
        num = ATM.select()
        if num == "2":
            print("开户")
            ATM.kaihu(userDict)
        elif num == "1":
            print("登陆")
            login = ATM.login()

