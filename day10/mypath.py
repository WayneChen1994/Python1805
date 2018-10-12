#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: Wayne.Chen


def pathjoin(path, *paths):
    if len(paths) == 0:
        return path
    res = path
    for x in paths:
        if x[1] == ':':
            res = x
        elif x.startswith('\\'):
            res = res[:2] + x
        else:
            res += '\\' + x
    return res


def pathsplit(path):
    if path == '.':
        return ("", '.')
    else:
        pathList = path.rsplit('\\', maxsplit=1)
        return tuple(pathList)


def pathdirname(path):
    if path == '.':
        return ""
    else:
        pathList = path.rsplit('\\', maxsplit=1)
        return pathList[0]


def pathbasename(path):
    if path == '.':
        return '.'
    else:
        pathList = path.rsplit('\\', maxsplit=1)
        return pathList[1]

print(__name__)
if __name__ == '__main__':
    print(pathjoin('E:\\demo', 'python'))
