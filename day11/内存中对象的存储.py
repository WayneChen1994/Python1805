#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author：Wayne


'''
注意：当我们创建对象的时候，即使创建的对象参数相同，
但是我们创建的仍然不是同一个对象，
'''


list1 = list()
list2 = list()
print(list1 is list2)
print(id(list1))
print(id(list2))


class Student():
    def __init__(self, name, age=18):
        self.name = name
        self.age = age

    def say(self):
        print("hello")


stu1 = Student("lili")
stu1.age = 20
print(stu1.name)
print(stu1.age)


stu3 = stu1
print(stu1 is stu3)
del stu1


stu2 = Student("lili", 20)
print(stu2.name)
print(stu2.age)


print(stu1 is stu2)
