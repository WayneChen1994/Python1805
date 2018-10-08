#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：Wayne


'''
需求1：将Teacher对象写入到文件并且读出。
需求2：将多个对象写入到文件并且读出
'''
import json


class Teacher(object):
    def __init__(self, name, age, sex, major):
        self.name = name
        self.age = age
        self.sex = sex
        self.major = major


# Teacher对象转为字典
def tea2dict(tea):
    return {'name': tea.name, 'age': tea.age, 'sex': tea.sex, 'major': tea.major}


# 字典转为Teacher对象
def dict2tea(dic):
    return Teacher(dic['name'], dic['age'], dic['sex'], dic['major'])


if __name__ == '__main__':
    tea1 = Teacher('wayne1', 23, True, 'python1')
    tea2 = Teacher('wayne2', 23, True, 'python2')
    tea3 = Teacher('wayne3', 23, True, 'python3')

    teaList = [tea1, tea2, tea3]

    # 操作单个对象的情况
    with open('jsondemo3.txt', 'w') as f:
        json.dump(tea1, f, default=tea2dict)

    with open('jsondemo3.txt', 'r') as f2:
        tea2 = json.load(f2, object_hook=dict2tea)
        print(tea2)
        print(tea2.name)


    # 操作多个对象的情况
    with open('jsondemo4.txt', 'w') as f3:
        for t in teaList:
            json.dump(t, f3, default=tea2dict)
            f3.write('\n')

    with open('jsondemo4.txt', 'r') as f4:
        alist = f4.readlines()
        resList = []
        for line in alist:
            resList.append(json.loads(line, object_hook=dict2tea))
        # resList为对象组成的列表
        print(resList)
