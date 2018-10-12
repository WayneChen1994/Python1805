#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: Wayne.Chen


'''
队列特点：
先进先出
'''


# queue = []
# queue.append(1)
# queue.append(2)
# queue.append(3)
# queue.append(4)
# print(queue)
# print(queue.pop(0))
# print(queue.pop(0))
# print(queue.pop(0))
# print(queue.pop(0))


import collections


queue = collections.deque([])
print(queue)


# 进队
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)
print(queue)


# 出队
print(queue.popleft())
print(queue.popleft())
print(queue.popleft())
print(queue.popleft())
