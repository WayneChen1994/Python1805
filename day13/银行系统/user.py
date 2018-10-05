#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author：zhangjiao

class User:
    #用户名 身份证 手机号  卡
    def __init__(self,username,idCard,phone,card):
        self.username = username
        self.idCard = idCard
        self.phone = phone
        self.card = card
