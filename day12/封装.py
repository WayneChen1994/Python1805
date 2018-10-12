#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：Wayne


'''
面向对象的三大特征：
封装、继承、多态
广义的封装：类与函数就是封装的体现
狭义的封装：类中的某些属性，我们不希望外界直接访问，
我们只让此属性在本类中持有，外界访问的时候，我们可以留一个接口访问即可

封装的本质，属性私有化的过程
封装的好处：
1、提高数据的复用性
2、保证数据的安全性
'''


'''
@property的作用：
1、将函数变成属性来进行调用
2、首先@property添加在getter方法上，
同时它又会创建出另外一个装饰器@方法名.setter，
将此装饰器添加给setter，此时，我们就可以将getter与setter变成属性来进行调用
3、将调用者的代码写得更加简单，增加数据的过滤
'''


class Person:
    def __init__(self, name, age, money):
        self.name = name
        self.__age = age
        self.__money = money

    @property   # get方法添加@property，并且方法名为去掉下划线的属性名
    def money(self):
        return self.__money

    @money.setter   # set方法添加@属性名.setter【去掉下划线的属性名】
    def money(self, mon):
        if mon < 0:
            print("钱的数值不对，存储失败")
        else:
            self.__money = mon

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, a):
        if a > 160 or a <= 0:
            print("年龄的数值不对，设置失败")
        else:
            self.__age = a


if __name__ == "__main__":
    per = Person("lili", 18, 100)
    per.money = -666
    print(per.money)
    per.money = 1000
    print(per.money)
    per.age = -99
    print(per.age)
    per.age = 88
    print(per.age)
