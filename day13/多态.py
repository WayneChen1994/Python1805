#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：Wayne

'''
鸭子模型：
“当看到一只鸟走起来像鸭子、游泳起来像鸭子、
叫起来也叫鸭子，那么这只鸟就可以被称为鸭子。”
这就是鸭子模型。

[Python中的多态不算真正意义上的多态，
它的多态的表现形式，就是人们常说的鸭子模型]

多态：
当在类中定义了一个方法，并且指定的该方法的类型，
那么当我们调用此方法的时候，我们只需要传入这个指定参数的类型，或者这个参数的子类即可。

优点：
1、使我们函数的使用更加灵活
2、增强函数的复用性
注意：多态依赖于继承，没有继承就没有多态。
'''

class Animal:
    def __init__(self, name):
        self.name = name

    # 成员方法
    def run(self):
        print(self.name, "run .... ")

    @staticmethod
    def run2(ani):
        if isinstance(ani, Animal):
            print(ani.name, "run .... ")
        else:
            print("参数有误")

class Dog(Animal):
    # def run(self):
    #     print("dog run .... ")
    pass

class Cat(Animal):
    # def run(self):
    #     print("cat run .... ")
    pass


class Mouse(Animal):
    pass


if __name__ == "__main__":
    dog = Dog("jerry")
    cat = Cat("tom")
    dog.run()
    cat.run()
    Animal.run2(dog)
    Animal.run2(cat)
    mou = Mouse("bob")
    Animal.run2(mou)
    Animal.run2(123)
    # print(type(dog))
    # print(type(cat))
    # print(isinstance(dog, Animal))
    # print(isinstance(cat, Animal))
    # a = list()
    # print(isinstance(a, list))
    # print(isinstance(dog, Dog))
    # print(isinstance(dog, Animal))
    # print(isinstance(cat, Animal))
    print(dir(dog))
