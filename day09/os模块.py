import os
'''
os模块：
当我们需要读取文件信息的时候，或者是读取一些配置文件的时候，我们需要对我们的文件路径进行一系列操作，这时候我们就依赖于os模块
注意：使用os模块的时候需要先导入
'''

'''
os.getcwd()
功能：查看当前路径
'''
# print(os.getcwd())

'''
os.listdir(path)
功能：列举指定路径下，所有的文件名
注意：path不写的时候，默认为当前路径
'''
# print(os.listdir(r"/home/wayne/PythonCode/Python1805"))

'''
os.path.abspath(path)
功能：返回指定路径或文件的绝对路径
绝对路径：以盘符开头或者以\\开头
相对路径：以.开头【当前路径】或以..【上一级目录】开头
注意：此功能并不会判断文件是否真的存在，它只起到了路径的拼接作用
'''
# print(os.path.abspath("../demo/mysum.py"))
# print(os.path.abspath("demo.py"))

'''
os.path.split(path)
功能：将指定路径分割为文件夹与文件名，并且作为元组返回
注意：此功能不会判断文件是否是目录，根据路径最后一个\\来切分，当\\不存在的时候，默认为文件名，当\\后文件名不存在的时候，则默认文件名为空
'''
# print("*" * 50)
# print(os.path.split(r"/home/wayne/PythonCode/Python1805/day09/mysum.py"))
# print(os.path.split(r"/home/wayne/PythonCode/Python1805/day09//"))
# print(os.path.split(r"/home/wayne/PythonCode/Python1805/day09"))
# print(os.path.split(r"."))
# print(os.path.split(r"./demo.py"))
# print(os.path.split(r"demo.py"))

'''
os.path.join(path, *paths)
功能：将指定的路径进行拼接，当路径中出现绝对路径的时候，它会将绝对路径之前的所有路径删除，只保留之后的。
'''
# print("*" * 50)
# print(os.path.join("demo"))
# print(os.path.join(os.getcwd(), "demo.py", "qq"))
# print(os.path.join(os.getcwd(), "/test/demo.py", "qq"))

'''
os.path.dirname(path)
功能：返回指定路径中文件夹部分，不包括最后的\\
'''
# print("*" * 50)
# print(os.path.dirname(r"/home/wayne/PythonCode/Python1805/day09/mysum.py"))
# print(os.path.dirname(r"/home/wayne/PythonCode/Python1805/day09//"))
# print(os.path.dirname(r"/home/wayne/PythonCode/Python1805/day09"))
# print(os.path.dirname(r"."))
# print(os.path.dirname(r"./demo.py"))
# print(os.path.dirname(r"demo.py"))

'''
os.path.basename(path)
功能：返回指定路径，文件名部分
'''
# print("*" * 50)
# print(os.path.basename(r"/home/wayne/PythonCode/Python1805/day09/mysum.py"))
# print(os.path.basename(r"/home/wayne/PythonCode/Python1805/day09//"))
# print(os.path.basename(r"/home/wayne/PythonCode/Python1805/day09"))
# print(os.path.basename(r"."))
# print(os.path.basename(r"./demo.py"))
# print(os.path.basename(r"demo.py"))


'''
os.path.getsize(path)
功能：获取指定路径下的文件大小，若此路径为文件，则返回0
或此路径不存在，则报错
'''
# print("*" * 50)
# print(os.path.getsize(r"/home/wayne/PythonCode/Python1805/day09/mysum.py"))
# print(os.path.getsize(r"/home/wayne/PythonCode/Python1805/day09/"))

'''
os.path.exists(path)
功能：判断指定路径是否存在，若存在则返回True，否则返回False
'''
# print("*" * 50)
# print(os.path.exists(r"/home/wayne/PythonCode/Python1805/day09/mysum.py"))
# print(os.path.exists(r"/home/wayne/PythonCode/Python1805/day09/mysum1.py"))
# print(os.path.exists(r"/home/wayne/PythonCode/Python1805/day09/"))
# print(os.path.exists(r"/home/wayne/PythonCode/Python1805/day09"))
# print(os.path.exists(r"/home/wayne/PythonCode/Python1805/day99"))

'''
os.path.isdir(path)
功能：判断路径是否为目录
os.path.isfile(path)
功能：判断路径是否为文件
'''
# print("*" * 50)
# print(os.path.isdir(r"/home/wayne/PythonCode/Python1805/day09/mysum.py"))
# print(os.path.isdir(r"/home/wayne/PythonCode/Python1805/day09/mysum1.py"))
# print(os.path.isdir(r"/home/wayne/PythonCode/Python1805/day09/"))
# print(os.path.isdir(r"/home/wayne/PythonCode/Python1805/day09"))
# print(os.path.isdir(r"/home/wayne/PythonCode/Python1805/day99"))

'''
需求：打印指定目录下所有的文件夹以及文件名
'''
def getAll(path, indent):
    indent = "    "
    filesList = os.listdir(path)
    for filename in filesList:
        absFilePath = os.path.join(path, filename)
        if os.path.isdir(absFilePath):
            print("目录：" + filename)
            getAll(absFilePath, indent)
        else:
            print(indent + "文件：" + filename)

getAll(r"/home/wayne/PythonCode/Python1805", "")
