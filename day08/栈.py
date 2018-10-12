#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: Wayne.Chen


'''
在Python中的栈是通过列表实现的
栈的特点：先进后出
'''


myStack = []


# 进栈
myStack.append(1)
myStack.append(2)
myStack.append(3)
myStack.append(4)
myStack.append(5)


# 出栈
print(myStack.pop())
print(myStack.pop())
print(myStack.pop())
print(myStack.pop())
print(myStack.pop())
