#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author：Wayne


import time
'''
练习：
同桌炫耀新买的iPhoneXS

对象1：同桌
行为：炫耀
特征：有钱，有手机

对象2：手机
特征：品牌，价钱，性能
行为：拍照，打电话
'''

class Phone():
    def __init__(self, pinpai, jiage, xingneng):
        self.pinpai = pinpai
        self.jiage = jiage
        self.xingneng = xingneng

    def paizhao(self):
        print("前后5000万像素，照亮你的美。。。")

    def call(self):
        print("打电话给同桌。。。。")

class Person():
    def __init__(self, name, money, iphone):
        self.name = name
        self.money = money
        self.iphone = iphone

    def xuxiao(self):
        print(self.name, "炫耀", self.iphone.pinpai)


# if __name__ == "__main__":
#     iphone = Phone("iphonexs", "11111", 90)
#     per = Person("狗蛋", 10000000, iphone)
#     per.xuxiao()
#     per.iphone.paizhao()
#     per.iphone.call()
    # iphone.paizhao()
