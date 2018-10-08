#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：Wayne


'''
对象存入到文件，并且将对象从文件中取出
'''
import pickle

class Student(object):
    def __init__(self, name, age, sex, stuId):
        self.name = name
        self.age = age
        self.sex = sex
        self.stuId = stuId


if __name__ == '__main__':
    stu = Student('lili', 18, 'girl', '110101')

    with open('user.txt', 'wb') as f:
        pickle.dump(stu, f)

    with open('user.txt', 'rb') as f2:
        stu2 = pickle.load(f2)
        print(stu2)
        print(type(stu2))
        print(stu2.name)
        print(stu2.age)


'''
需求：创建一个老师对象
属性：姓名、年龄、性别、专业
分别使用pickcle模块，或者自己的方法，
将对象存入到文件中，并且取出。
'''

class Teacher(object):
    def __init__(self, name, age, sex, major):
        self.name = name
        self.age = age
        self.sex = sex
        self.major = major


if __name__ == '__main__':
    te = Teacher('wayne', 23, 'boy', 'python')
    te2 = Teacher('wayne2', 232, 'boy2', 'python2')
    list2 = [te, te2]
    dict2 = {te.name:te, te2.name:te2}
    # 使用pickle模块进行对象序列化和反序列化操作
    with open('teacher.txt', 'wb') as f:
        # pickle.dump(te, f)
        # pickle.dump(te2, f)
        # pickle.dump(list2, f)
        pickle.dump(dict2, f)
        # res = pickle.dumps(te, f)
        # f.write(res)

    with open('teacher.txt', 'rb') as f2:
        # te3 = pickle.load(f2)
        # pickle.loads(f2.read())
        # print(te3.name)
        # tealist = pickle.load(f2)
        teadict = pickle.load(f2)
        # print(tealist)
        # print(tealist[0].name)
        # print(tealist[1].name)
        print(teadict)
