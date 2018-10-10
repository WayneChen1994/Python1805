#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：Wayne


from functools import reduce


def add(a, b):
    return a + b


def jiecheng(n):
    return reduce(lambda x,y:x*y, range(1, n+1))


class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getAge(self):
        return self.age
