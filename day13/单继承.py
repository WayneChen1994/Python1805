#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：Wayne

print()
'''
继承：
两个或者是两个以上的类，我们可以将其公共的部分抽取出来作为父类
被抽取出来的类 --> 父类、超类、基类
其他类 --> 子类、派生类
之间的关系 -- 子类继承父类
注意：若一个类没有继承其他的类，则默认继承object类
换句话说，object是一切类的基类
'''

'''
总结：
1、当子类继承父类的时候，子类可以直接使用父类所有未私有化的属性
【注意：父类私有化的属性子类不能直接使用，
但是可以通过父类的接口来间接使用】

2、父类不能使用子类的属性以及方法

3、子类对象可以调用父类中所有的未私有方法

继承的优点：
1、简化代码
2、提高代码的可维护性
3、提高代码的安全性

继承的缺点：
代码耦合性因继承而增大
'''

class Animal:
    def eat(self):
        print("吃。。。")

    def sleep(self):
        print("睡觉。。。。")

    def run(self):
        print("跑。。。")


class Cat(Animal):
    def getMouse(self):
        print("抓老鼠。。。。。")


# if __name__ == "__main__":
#     cat = Cat()
#     cat.run()
#     cat.getMouse()

'''
人类
特征：name,age,sex
行为：eat sleep

学生类
特征：name,age,sex,score,studentId
行为：eat sleep study

老师类
特征：name,age,sex,project
行为：eat sleep teaching
'''

'''
使用单继承的时候，子类中没有自己独有的属性的时候，
子类中不写__init__函数也可以，
但是实例化子类的时候需要传递父类需要的参数
当子类中存在自己独有的属性的时候，这时候在__init__函数中，
我们需要将父类需要的参数也进行声明，
并且在子类的__init__函数中要初始化父类
super(子类类名, self).__init__(参数列表)
父类类名.__init__(self, 参数列表)
'''

class Person:
    def __init__(self, name, age, sex, money):
        self.name = name
        self.age = age
        self.sex = sex
        self.__money = money

    @property
    def money(self):
        return self.__money

    @money.setter
    def money(self, num):
        self.__money += num

    def eat(self):
        print("吃饭")

    def sleep(self):
        print("睡觉")


class Student(Person):
    def __init__(self, name, age, sex, money, score, studentId):
        super(Student, self).__init__(name, age, sex, money)
        # 多继承的情况下应该写成下面的方式
        # Person.__init__(self, name, age, sex)
        self.score = score
        self.studentId = studentId

    def study(self):
        print("学习。。。。")


class Teacher(Person):
    def __init__(self, name, age, sex, money, project):
        super(Teacher, self).__init__(name, age, sex, money)
        self.project = project

    def teaching(self):
        print("讲课。。。。")


'''
需求：
在Person中添加money，并且将其私有化，
测试子类是否能够直接访问被私有化的money
'''

if __name__ == "__main__":
    stu = Student("wayne", 7, "body", 1000, 90, "001")
    tea = Teacher("lili", 18, "girl", 9999, "python")
    # print(stu.__getMoney())
    print(stu.money)
    stu.money = 333
    print(stu.money)
