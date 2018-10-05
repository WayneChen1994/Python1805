#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author：zhangjiao

class Card:
    # 卡号 密码 余额  是否锁卡
    def __init__(self,cardNum,psd,money,islock=False):
        self.cardNum = cardNum
        self.psd = psd
        self.money = money
        self.islock = islock