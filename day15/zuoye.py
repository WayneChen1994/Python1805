#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：Wayne


import json


class Teacher(object):
    def __init__(self, name, age, sex, project):
        self.name = name
        self.age = age
        self.sex = sex
        self.project = project


def tea2dict(tea):
    return {"name": tea.name, "age": tea.age, "sex": tea.sex, "project": tea.project}


def dict2tea(dict1):
    return Teacher(dict1["name"], dict1["age"], dict1["sex"], dict1["project"])


tea = Teacher("里斯", 26, "boy", "云计算")
tea2 = Teacher("里斯2", 26, "boy", "云计算")

'''写入单个对象'''
# with open("tea.txt", "w", encoding="utf-8") as f:
#     json.dump(tea, f, default=tea2dict)
#
#
# with open("tea.txt", "r", encoding="utf-8") as f2:
#     # json.load(f2)
#     print(json.load(f2, object_hook=dict2tea))


'''写入多个对象'''
with open("tea1.txt", "a", encoding="utf-8") as f:
    json.dump(tea2, f, default=tea2dict)
    f.write("\n")


with open("tea1.txt", "r", encoding="utf-8") as f2:
    print(json.load(f2, object_hook=dict2tea))
    for line in f2.readlines():
        print(json.loads(line, object_hook=dict2tea))
