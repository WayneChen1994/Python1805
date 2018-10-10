#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：Wayne


import unittest
from day16.testdemo import add, jiecheng, Person


class Test(unittest.TestCase):
    # 一般情况下，若需要数据库连接的时候
    # 我们在setUp中进行数据库的连接
    # 在tearDown进行数据库的断开
    def setUp(self):
        print("开始测试的时候自动调用")

    def tearDown(self):
        print("测试结束的时候自动调用")

    def test_add(self):
        self.assertEqual(add(1, 2), 3, "加法有误")

    '''
    测试函数语法
    test_要测试的函数名
    '''
    def test_jiecheng(self):
        # 断言
        # 参数一：要测试的函数
        # 参数二：断言的结果【一定要保证断言的结果是正确的】
        # 参数三：测试失败的时候，打印的提示信息
        self.assertEqual(jiecheng(5), 120, "阶乘计算有误")

    '''
    对于类的单元测试，说白了还是对于函数的单元测试
    测试类属性，函数名test_init()
    并且需要创建对象/实例化对象
    '''
    def test_init(self):
        per = Person("李磊", 28)
        self.assertEqual(per.age, 28, "年龄属性有误")

    '''
    测试类中的函数：
    test_函数名
    若测试的是成员方法，需要先创建对象【实例化对象】
    '''
    def test_getAge(self):
        per = Person("jerry", 3)
        self.assertEqual(per.getAge(), 3, "获取年龄有误")


if __name__ == "__main__":
    unittest.main()
