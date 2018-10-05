#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：Wayne


'''
多继承：
1、子类可以继承多个父类中的属性以及方法
2、一个子类可以有多个父类，一个父类也可以有多个子类
3、当一个子类继承多个父类的时候，多个父类中出现同名方法
子类使用此方法的时候，调用的是写在小括号里面，
最前面那个拥有此方法的类中的方法。
【小括号中写在前面的优先级高于后面的】
'''
class GrandFather:
    def dance(self):
        print("广场舞。。。")


class Father(GrandFather):
    def __init__(self, name, money):
        self.name = name
        self.money = money

    def drive(self):
        print("开车。。。")

    def sing(self):
        print("娘子，啊哈。。。")


class Mother:
    def __init__(self, name, faceValue):
        self.name = name
        self.faceValue = faceValue

    def sing(self):
        print("唱歌。。。")

    def dance(self):
        print("恰恰。。。")


class Chind(Father, Mother):
    def __init__(self, name, money, faceValue):
        Father.__init__(self, name, money)
        Mother.__init__(self, name, faceValue)


if __name__ == "__main__":
    child1 = Chind("小明", 100000000, 90)
    print(child1.faceValue)
    child1.sing()
    child1.dance()
    child1.drive()
    print(child1.money)
