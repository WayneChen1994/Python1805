#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author：Wayne


'''
动态绑定属性以及方法
在Python中，当我们实例化完对象之后，我们可以给我们的对象绑定任意的属性以及方法，这就是Python动态语言的灵活性。

注意：我们动态绑定的属性以及方法，只作用于当前对象，对其他对象不起作用

当我们使用类名来动态绑定属性的时候，绑定给这个类的，
因此它绑定的这个属性为类变量，类变量为公用的，
因此对所有的对象都起作用。

给对象动态绑定函数，只需要将函数名绑定给对象即可，
调用的时候，若需要参数传递即可。

动态绑定在类身上的函数使用对象来进行调用的时候会出一些小问题，
【对象进行调用的时候会将自己自动的传递进去，参数调用会出现问题】

__slots__限制对象动态添加属性以及函数，限制初始化添加的一些属性
动态添加的属性以及函数的函数名，只能是在__slots__声明过的。
__slots__使用元组进行初始化，元组中是我们添加的限制。

总结：
为了限制对象动态添加属性以及方法，
我们可以使用__slots__来进行声明此类中的可以添加的成员变量以及函数的函数名，起到限制的作用。
'''


class Student:
    __slots__ = ("name", "age")

    def __init__(self, weight=120):
        # self.weight = weight
        pass
    def say(self):
        print("say hello")
    pass


stu = Student()
stu.name = "lili"
stu.age = 18
# stu.sex = "girl"
print(stu.name)
print(stu.age)

stu.say()

# print(stu.weight)
# print(stu.sex)

def say(string):
    print("say", string)

# stu.say2 = say
# stu.say2("byebye")

Student.say = say
Student.say("hello")

Student.name = "haha"
stu2 = Student()
print(stu2.name)
# stu2.say()

stu3 = Student()
print(stu3.name)
# stu3.name = "hehe"
print(stu3.name)

'''
需求：创建一个老师类，动态添加属性以及方法
限制：
属性：name,sex,科目
方法：eat sleep teaching
'''
class Teacher:
    __slots__ = ("name", "sex", "subject", "eat", "sleep", "teaching")
    pass

te = Teacher()
te.name = "lili"
te.sex = "girl"
te.subject = "python"

def eat(food):
    print("吃", food)

def sleep():
    print("睡觉")

def teaching():
    print("上课")

# def test():
#     print("testing")
# te.test = test

te.eat = eat
te.sleep = sleep
te.teaching = teaching

te.eat("香蕉")
te.sleep()
te.teaching()
print(te.name)
print(te.sex)
print(te.subject)
