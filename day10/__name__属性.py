#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: Wayne.Chen


'''
每个模块中，都有一个变量名为__name__的内置变量，
当模块在其内部执行的时候__name__的值为__main__，
当模块作为其他模块的模块引入的时候，__name__的值为其模块的模块名。

通过此变量，我们可以区分模块是被引入还是在自身执行，因此通常情况下，我们在模块运行程序的时候会添加一下代码：
if __name__ == '__main__':
而作为我们整个程序的一个入口
'''


def main():
    pass


if __name__ == '__main__':
    main()
