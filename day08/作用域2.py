#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: Wayne.Chen


'''
测试：全局变量、嵌套变量、局部变量重名的时候
结论：搜索变量名的优先级
局部作用域-->嵌套作用域-->全局作用域-->内置作用域
简称LEGB法则

当这几个作用域中都没有搜索到对应的变量名的时候，程序就会报错
'''


a = 100


def outer():
    # a = 200
    def inner():
        # a = 300
        # b = 400
        global a
        a += 1
        print(a)
    return inner


outer()()


'''
函数中的变量在函数被调用的时候创建，当函数执行结束之后，变量则被销毁
简而言之，在全局作用域中，是无法使用局部变量【函数中的变量】
'''


'''
关键字global的使用
当我们在函数体内，想更改全局变量的时候，直接更改则会报错，此时我们需要在函数体内部使用global声明一下全局变量，
声明之后，我们就可以更改全局变量
'''


for i in range(10):
    pass


print(i)


'''
注意：Python中只有模块【.py文件】，类【class】，函数【def,lambda】
只有这些才会产生新的作用域，
而if/else、while/for、try/except这些代码块不会产生新的作用域，
它的使用范围取决于它定义的位置
'''
