#! /usr/bin/env python
# -*- coding: utf-8 -*-
# author: Wayne.Chen


'''
位置参数【传递顺序有关】/必选参数【此参数一定要传递】
'''


def myPrint(name, age):
    print("我是%s，今年%d岁" % (name, age))


myPrint("丽丽", 18)
# myPrint(18,"丽丽")
# myPrint("丽丽")


'''
关键字参数
在函数调用的时候，我们可以通过键值对的方式来进行传参，使函数更加清晰容易调用，使用此参数可以清除位置参数的顺序
'''


myPrint(age=18, name="丽丽")


'''
默认参数：
在函数定义的时候，我们可以给某些参数设置默认值
设置默认值的参数，我们称之为默认参数
调用函数的时候，这些默认参数，我们可以传也可以不传
当不传的时候，则使用默认参数；传递的时候，使用传递的参数即可

注意：
1、使用默认参数的时候，默认参数一定要写在位置参数的后面
2、默认参数指向的一定是不变对象
3、当存在多个默认参数的时候，我们对默认参数进行赋值时，可以使用关键字参数
'''


# def myPrint2(name, addr, age=7):
#     print("我叫%s，今年%d岁，我来自%s" % (name, age, addr))


# myPrint2("小明", "广州")


# def myPrint3(name, addr, age=7,hobby=["打球"]):
#     print("我叫%s，今年%d岁，我来自%s，我的爱好是%s" % (name, age, addr,hobby))


# myPrint3("小明","广州",hobby=["跑步"])


# def func(b, a=[]):
#     a.append(b)
#     print(a)


# func(10)
# func(20)
# func(30)
# [10]
# [10, 20]
# [10, 20, 30]
