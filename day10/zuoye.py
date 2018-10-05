def pathjoin(path, *paths):
    # 元组
    if len(paths) == 0:
        return path
    res = path
    for x in paths:
        if x[1] == ':': # 绝对路径
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


if __name__ == '__main__':
    print("hello python")
