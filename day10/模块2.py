#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: Wayne.Chen


'''
模块的引入方式：
1、整体引入
import 模块名1，模块名2，……，模块名n
函数调用：
模块名.函数名
模块名.变量名

2、局部引入
from 模块名 import 函数名，变量名
函数的调用：
函数名（）
变量名

3、通过*号引入【不建议使用】
from 模块名 import *

*代表引入所有的函数、变量以及类，
【容易引起命名冲突】因此不建议使用

4、别名引入
import 模块名 as 别名
函数调用：
别名.函数名()
别名.变量名
功能：当模块名比较长，不好记的时候，我们可以通过as关键字给其起一个别名，然后通过别名来调用模块中的函数

注意：引入模块的时候，不要重复引入
'''


from day10.zuoye import *
import collections as co

co.Iterator
# collections.Iterator
