#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：Wayne


'''
定义在类中的变量，我们又分为类变量与成员变量

类变量【静态成员变量】：
定义在类中，并且定义在函数体之外，在实例化的过程中，是公用的

成员变量：
定义在类中的函数体里面，并且绑定在self身上的变量，
我们称之为成员变量

区别：
1、定义位置不同
2、调用的方式不同，类变量可以使用对象、类名来调用，
而成员变量只能使用对象来调用
3、使用对象来更改类变量的时候，更改的只是当前对象，
【更改的值，只作用于当前对象】
而使用类名来更改的时候，直接更改的类变量初始值
【更改的值，作用于所有的对象】
4、优先级不同，当我们使用对象来进行调用的时候，类变量与成员变量同名的时候，返回的是成员变量的值。
【使用对象来进行调用的时候，成员变量的优先级高于类变量的优先级】
5、当使用对象来进行调用的时候，成员变量不存在的情况下，
则会调用类变量，若类变量也不存在则报错。
'''


class Person():
    name = "hehe"
    age = 18
    PI = 3.1415926
    def __init__(self, height, weight):
        # self.name = name
        self.height = height
        self.weight = weight


if __name__ == "__main__":
    per = Person(180, 180)
    print(per.name)
    print(Person.name)
    per.sex = "girl"
    print(per.sex)

    per2 = Person(170, 120)
    print(per2.sex)

    # print(per.weight)
    # print(per.height)
    # print(per.name)
    # print(per.age)
    print(Person.age)
    print(Person.name)
    # per.name = "lili"
    Person.name = "lili"
    print(per.name)
    per2 = Person(170, 130)
    print("*", per2.name)
