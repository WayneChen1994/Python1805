#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author：Wayne


'''
人拿枪射击子弹

人：
特征：name，有枪
行为：射击

枪：
特征：型号，弹夹
行为：上膛，发射子弹

弹夹：
特征：子弹【八发】
行为：装弹，减少子弹
'''


class Danjia:
    def __init__(self, dan=8):
        self.dan = dan

    def zhuangdan(self, zidan=8):
        self.dan += zidan

    def jiandan(self):
        if self.dan > 0:
            self.dan -= 1
            print("砰～～～")
        else:
            print("没有子弹了")


class Gun:
    def __init__(self, xinghao, danjia):
        self.xinghao = xinghao
        self.danjia = danjia

    def shangtang(self):
        print("上膛")
        self.danjia.zhuangdan()

    def shoot(self):
        self.danjia.jiandan()



class Person():
    def __init__(self, name, gun):
        self.name = name
        self.gun = gun

    def sheji(self):
        self.gun.shoot()

    def shangtang(self):
        self.gun.shangtang()


if __name__ == "__main__":
    danjia = Danjia()
    gun = Gun("AK-47", danjia)
    per = Person("铁牛", gun)
    per.sheji()
    per.sheji()
    per.sheji()
    per.sheji()
    per.sheji()
    per.sheji()
    per.sheji()
    per.sheji()
    per.sheji()
    per.shangtang()
    per.sheji()
    per.sheji()
