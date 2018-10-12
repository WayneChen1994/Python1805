#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：Wayne


'''
首单下划线：_foo保护类型，虽然我可以直接被访问，但是请你把我当成私有属性

首双下划线：__foo私有属性，只允许本类使用

首尾双下划线：__foo__定义特殊的方法与变量，一般用于定义系统函数以及变量
'''


class Person:
    def __init__(self, name, age, money):
        self.name = name
        self._age = age
        self.__money = money


if __name__ == "__main__":
    per = Person("lili", 18, 1000)
    print(per._age)
