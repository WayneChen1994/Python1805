#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：Wayne


import logging


'''
当程序没有进行异常捕捉的时候，Python解释器会自己将错误的堆栈信息打印出来。
但是，工作中我们需要查看错误的信息还需要使程序继续运行，也就是说，我们既需要捕捉错误，也需要打印错误信息以便对错误进行处理。
这时候，我们可以使用logging模块来打印错误信息。
logging.exception(e)
'''


def func(a, b):
    try:
        return a / b
    except Exception as e:
        # 使用logging打印错误信息
        logging.exception(e)


print(func(1, 0))
print("***********")
