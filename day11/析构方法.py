#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：Wayne


'''
析构函数/方法，也是系统提供的，这个也不需要我们手动调用。
当对象销毁的时候，它会自动的调用

总结：当程序执行结束的时候，或是使用del删除对象的时候，对象所占用的这块内存都会被回收，当对象占用的这块内存被回收的时候，就会调用析构函数。

使用场景：
1、对象销毁之后，销毁一些不用的变量
2、若类中有使用到数据库，在对象销毁的时候，断开数据库连接
'''


class Person():
    def __init__(self, name, age, sex):
        print("构造方法被调用了。。。。")
        self.name = name
        self.age = age
        self.sex = sex

    def introduce(self):
        print("我叫%s，今年%d岁，我是%s" % (self.name, self.age, self.sex))

    def __del__(self):
        print("析构函数被调用了。。。。")


if __name__ == "__main__":
    per1 = Person("lili", 18, "girl")
    del per1
    while True:
        pass
