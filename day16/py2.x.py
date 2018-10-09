#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：Wayne


print()

# 关于Python2与Python3的区别

'''
1、性能：Python3起始比Python2效率低，但是Python3有极大的优化空间，效率正在追赶

2、编码：Python3原码文件默认使用utf-8编码，使变量名更为广阔

3、Python3语法：
    a、去除了<>，改用!=
    b、加入as和with关键字，还有True，False，None
    c、整型除法返回浮点数，整除请使用//
    d、加入了nonlocal语句
    e、去除print语句，加入print()函数
    f、去除了raw_input，加入input()函数
    g、新的super()，可以不再给super()传参数
    h、改变了顺序操作符的行为，例如x<y，当x和y类型不匹配时抛出TypeError而不是返回随即的bool值
    i、新式的8进制字变量，如0o666代表八进制的666

4、字符串和字节串：
    a、Python2：字符串以8-bit字符串存储
    b、Python3：字符串以16-bit Unicode字符串存储，现在字符串只有str一种类型

5、数据类型：
    a、Python3去除了long类型，现在只有一种整型int，但它的行为就像Python2中的long
    b、新增了bytes类型，对应Python2中的八位串
    c、str对象和bytes对象可以使用encode和decode进行相互转化

6、面向对象：引入抽象基类

7、异常：
    a、所有异常都从BaseException继承，并删除了StandardError
    b、Python2：except Exception, e
       Python3: except Exception as e

8、其他：
    a、xrange()改名为range()，要想使用range()获得一个list，必须显式调用
    b、file类被废弃（Python2打开文件可以用file(path)）
'''
