import os


def getAllDG(path, treeshow):
    treeshow += "    "
    fileList = os.listdir(path)
    for filename in fileList:
        absPath = os.path.join(path, filename)
        if os.path.isdir(absPath):
            print("%s目录：%s" % (treeshow, filename))
            getAll(absPath, treeshow)
        else:
            print("%s文件：%s" % (treeshow, filename))


# getAll(r"/home/wayne/PythonCode/Python1805", "")

def getAllStack(path, treeshow):
    treeshow += "    "
    stack = []
    stack.append(path)
    while len(stack) != 0:
        dirPath = stack.pop()
        fileList = os.listdir(dirPath)
        for filename in fileList:
            absPath = os.path.join(dirPath, filename)
            if os.path.isdir(absPath):
                print("目录：%s" % filename)
                stack.append(absPath)
            else:
                print("%s文件：%s" % (treeshow, filename))


# getAllStack(r"/home/wayne/PythonCode/Python1805", "")

import collections


def getAllQueue(path):
    queue = collections.deque()
    queue.append(path)
    while len(queue) != 0:
        dirPath = queue.popleft()
        fileList = os.listdir(dirPath)
        for filename in fileList:
            absPath = os.path.join(dirPath, filename)
            if os.path.isdir(absPath):
                print("目录：%s" % filename)
                queue.append(absPath)
            else:
                print("文件：%s" % filename)


getAllQueue(r"/home/wayne/PythonCode/Python1805")
