#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：Wayne


class Student():
    def __init__(self, stuId, name, classname, sex, score):
        self.stuId = stuId
        self.name = name
        self.classname = classname
        self.sex = sex
        self.score = score
        self.introduce()

    def study(self):
        print('学习。。。。')

    def eat(self):
        print('吃饭。。。。')

    def sleep(self):
        print("睡觉。。。。")

    def introduce(self):
        print('''大家好！我是%s班的%s生一枚，我叫%s，学号为%s，我的成绩是%d分。。。''' % (self.classname, self.sex, self.name, self.stuId, self.score))


if __name__ == '__main__':
    stu1 = Student("001", "张三", "py1806", "男", 70)
    stu2 = Student("002", "李四", "py1805", "女", 66)
