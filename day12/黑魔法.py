#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author：Wayne


class Student:
    def __init__(self, name, age):
        self.name = name
        self.__age = age


if __name__ == "__main__":
    stu = Student("lili", 18)
    # print(stu.__age)
    print(stu._Student__age)
