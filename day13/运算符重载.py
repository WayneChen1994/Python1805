#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：Wayne


'''
当我们在类中重写了__add__方法后，我们使用对象相加的时候
【在我们使用加号的时候，自动的调用__add__这个方法】
加号两边的两个参数会自动地传入__add__方法中
'''


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 方法的重写
    def __str__(self):
        # return "%s-%d" % (self.name, self.age)
        return str(self.age)

    # def __repr__(self):
    #     return "%s-%d" % (self.name, self.age)
    # __repr__ = __str__

    def __add__(self, other):
        age = self.age + other.age
        return Person(self.name, age)

    def __gt__(self, other):
        return True if (self.age>other.age) else False

    def __lt__(self, other):
        return True if (self.age<other.age) else False

if __name__ == "__main__":
    per = Person("lili", 18)
    per2 = Person("李磊", 18)
    per3 = Person("李名", 18)
    per4 = Person("李当", 18)
    per5 = Person("李特", 18)
    # print(per + per2)
    # print(type(per + per2))
    print(per+per2+per3+per4+per5)
    print(per>per2)
    print(per<per2)
