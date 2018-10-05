#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author：Wayne


class Pizza:
    price = 20

    def __init__(self, t):
        self.t = t

    @staticmethod
    def getSize(r):
        return 3.14*pow(r/2, 2)

    @classmethod
    def getPrice(cls, size):
        # 硬编码
        # return Pizza.price * size
        # 软编码
        return cls.price * size


if __name__ == "__main__":
    res = Pizza.getPrice(10)
    print(res)
    res2 = Pizza.getSize(10)
    print(res2)
