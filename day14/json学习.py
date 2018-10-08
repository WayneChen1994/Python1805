#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：Wayne


'''
json是标准模式，并且传输速度快。
所以在不同编程语言交互的时候，我们都会使用json。
json其实就是一个字符串。
'''

import json
#
# class Student(object):
#     def __init__(self, name, age, sex, stuId):
#         self.name = name
#         self.age = age
#         self.sex = sex
#         self.stuId = stuId
#
# stu = Student('lili', 18, 'girl', '110101')
#
# '''
# 将stu存入到文件中，并且读取出来
# '''
#
# def stu2dict(stu):
#     return {'name': stu.name, 'age':stu.age, 'sex': stu.sex, 'stuId':stu.stuId}
#
# def dict2stu(dict1):
#     return Student(dict1['name'], dict1['age'], dict1['sex'], dict1['stuId'])
#
# with open('jsondemo2.txt', 'w') as f:
#     # 参数一：要存储的对象
#     # 参数二：打开的文件
#     # 参数三：将对象转为字典
#     json.dump(stu, f, default=stu2dict)
#
# with open('jsondemo2.txt', 'r') as f2:
#     # 参数一：打开的文件
#     # 参数二：将字典转为对象
#     stu2 = json.load(f2, object_hook=dict2stu)
#     print(stu2)
#     print(type(stu2))
#     print(stu2.name)

# dict1 = {'name': 'lili', 'age': 18, 'sex': True, 'project': None}
#
# with open('jsondemo.txt', 'w') as f:
#     json.dump(dict1, f)
#
# with open('jsondemo.txt', 'r') as f2:
#     print(json.load(f2))


'''
需求1：将Teacher对象写入到文件并且读出。
需求2：将多个对象写入到文件并且读出
'''

class Teacher(object):
    def __init__(self, name, age, sex, major):
        self.name = name
        self.age = age
        self.sex = sex
        self.major = major


def tea2dict(tea):
    return {'name': tea.name, 'age': tea.age, 'sex': tea.sex, 'major': tea.major}

def dict2tea(dic):
    return Teacher(dic['name'], dic['age'], dic['sex'], dic['major'])


if __name__ == '__main__':
    tea1 = Teacher('wayne1', 23, True, 'python1')
    tea2 = Teacher('wayne2', 23, True, 'python2')
    tea3 = Teacher('wayne3', 23, True, 'python3')

    teaList = [tea1, tea2, tea3]

    # with open('jsondemo3.txt', 'w') as f:
    #     json.dump(tea1, f, default=tea2dict)
    #
    # with open('jsondemo3.txt', 'r') as f2:
    #     tea2 = json.load(f2, object_hook=dict2tea)
    #     print(tea2)
    #     print(tea2.name)

    with open('jsondemo4.txt', 'w') as f3:
        for t in teaList:
            json.dump(t, f3, default=tea2dict)
            f3.write('\n')

    with open('jsondemo4.txt', 'r') as f4:
        alist = f4.readlines()
        resList = []
        for line in alist:
            resList.append(json.loads(line, object_hook=dict2tea))
        print(resList)
