'''
模块的概念：
简言之，在Python中一个.py文件就是一个模块
通常情况下，我们的模块会按照函数的功能，将函数分类，放在不同的py文件中，即分成不同的模块

模块优点：
1、便于维护
2、提高代码的复用率
3、可以使用第三方模块
4、可以避免函数名与变量名冲突
'''

'''
在模块中取变量名的时候，尽量不要与内置变量和内置函数的函数名冲突，
取模块名的时候，也尽量不要与内置模块或者是第三方模块的模块名冲突。
'''

'''
模块的引入之整体引入：
import 模块名1,模块名2,……,模块名n

模块中函数的调用：
模块名.函数名（参数列表）
模块名.变量名

模块的引入之局部引入：
from 模块名 import 函数名[变量名],函数名2,类名
局部导入后，函数的调用：
函数名(参数列表)
变量名
注意：使用此方法引入，会使我们函数的调用以及变量的调用更加的简单，我们无须添加模块名，直接调用即可【前提是：此函数或者此变量已被引入】
使用此方法引入，注意变量名或者函数名的冲突问题
'''
# import time
# import zuoye
# from zuoye import pathsplit

# print(zuoye.pathsplit(r'c:\demo'))

'''
设计一个模块：
模块功能：对路径的处理
【给模块取名的时候，尽量避免使用空格或者中文】
用以上两种方式来进行引入
'''
import mypath
from mypath import pathjoin, pathsplit

print(pathjoin('c:\\demo', 'python'))
