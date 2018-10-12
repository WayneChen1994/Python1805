#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：Wayne


'''
单例模式
一个类只创建一个对象。
'''


class Person:
    # 静态成员属性
    singins = None

    def __new__(cls, name, age):
        if cls.singins is None:
            # 使用new方法调用的时候，需要使用super调用
            cls.singins = super().__new__(cls)
        return cls.singins

    # def __init__(self, name, age):
    #     self.name = name
    #     self.age = age


if __name__ == "__main__":
    per1 = Person("lili", 18)
    print(per1)
    per2 = Person("lili", 19)
    print(per2)
    # print(id(per1))
    # print(id(per2))
    print(per1 is per2)
    # per2.name = "zhangsan"
    # print(per1.name)
