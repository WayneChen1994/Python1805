#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author：Wayne


'''
构造方法，主要用于初始化对象的，
当实例化对象的时候会自动地调用构造方法

总结：在创建类的时候，如果需要初始化参数的时候，我们需要将参数的初始化放在__init__函数中，并且绑定在self身上。

__init__() 系统提供的函数
'''
class Person():
    def __init__(self, name, age, sex):
        print("构造方法被调用了。。。。")
        self.name = name
        self.age = age
        self.sex = sex

    def introduce(self):
        print("我叫%s，今年%d岁，我是%s" % (self.name, self.age, self.sex))

if __name__ == "__main__":
    per1 = Person("lili", 18, "girl")
    print(per1.name)
    print(per1.age)
    print(per1.sex)
    per1.introduce()
    list1 = list()
    list2 = list((1, 2, 3))
