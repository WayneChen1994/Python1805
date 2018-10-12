#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：Wayne


import datetime


'''
__str__()：函数的重写
当我们调用print打印对象的时候，它会自动调用__str__这个函数，
来打印__str__()函数返回的内容，这个方法是方便用户查看信息。
'''


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 方法的重写
    def __str__(self):
        return "%s-%d" % (self.name, self.age)

    # def __repr__(self):
    #     return "%s-%d" % (self.name, self.age)
    __repr__ = __str__

    def __add__(self, other):
        return self.age + other.age



if __name__ == "__main__":
    per = Person("lili", 18)
    per2 = Person("lili", 18)
    print(per + per2)
