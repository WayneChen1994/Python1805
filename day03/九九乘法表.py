#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: Wayne.Chen


'''
嵌套循环
'''


n = 1
while n <= 9:
    m = 1
    while m <= n:
        print("%dx%d=%d" % (m, n, n*m), end=" ")
        m += 1
    print()
    n += 1
