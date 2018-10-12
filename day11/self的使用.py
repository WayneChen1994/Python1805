#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：Wayne


'''
self是实例【对象】本身，而不是类
self并不是我们使用的关键字，
但是我们约定俗成的就是使用self
建议使用self。
注意：self在函数声明的时候，需要声明，并且要写在参数列表的第一位
调用的时候并不需要手动地传递self，调用的时候，它会将自己自动地传递进去。
'''


# class Student():
#     def __init__(self):
#         print("self", self)
#
#     def say(self):
#         print("hello")
#
#
#
# if __name__ == "__main__":
#     stu1 = Student()
#     print("stu1", stu1)
#     print("Student", Student)
#     stu1.say()


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
    def __init__(self, brand, price,  performance):
        self.brand = brand
        self.price = price
        self.performance = performance

    def takePhotos(self):
        print("拍照。。。")

    def callTo(self):
        print("打电话。。。")


class Deskmate():
    def __init__(self, money, phone):
        self.money = money
        self.phone = phone

    def showUp(self, phone):
        print("我买了新款的%s手机，不贵才%d元～" % (self.phone.brand, self.phone.price))


if __name__ == "__main__":
    p = Phone("iPhoneXS", 9999, "great")
    dm = Deskmate(9999999, p)
    dm.showUp(p)
