#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author：Wayne


'''
class 类名:
    类体

说明：
1、使用关键字class声明
2、类名命名使用驼峰式命名：
大驼峰【单词的首字母大写，类名】，Student
小驼峰【第一个单词的首字母小写，其他单词的首字母大写，变量名或者函数名】,getClass
3、见名知义【取名尽可能简短】
'''

class demo():
    print("hello world")

'''
类的设计：
1、类名 ---> Person
2、特征 ---> 【名词】name,age,facevalue,money 
3、行为 ---> 【动词】eat,speak,run,study,sleep
'''

'''
类的属性 <---> 特征
类的方法 <---> 行为
'''

class Person:
    name = "lili"
    age = 18
    facevalue = 90
    money = 5000

    def eat(self, food):
        print("吃%s。。。"%food)

    def sleep(self):
        print("睡觉。。。")

    def study(self):
        print("学习。。。")


'''
若需要使用类中的函数，需要先实例化对象
实例化对象：
对象名 = 类名()
类中属性的访问：
对象名.属性名
类中的成员方法的方法的访问
对象名.方法名()
'''
# list1 = list()
per = Person()
print(per)
print(per.name)
print(per.age)
per.eat("蛋炒饭")
per.sleep()
per.study()

'''
需求：创建一个学生类：
1、类名
2、特征 学号，姓名，班级，性别，分数
3、行为 学习，吃饭，睡觉，敲代码
'''
