import sys

print(sys.argv)
# 当前文件的路径
print(sys.argv[0])
# 传递进来的第一个参数
print(sys.argv[1])
# 传递进来的第二个参数
print(sys.argv[2])

'''
sys.argv可以接收从外部传进来的参数
'''

'''
sys.platform 获取当前执行代码的环境平台
'''
print(sys.platform)

'''
path是目录列表，供python从中查找第三方拓展模块
'''
print(sys.path)
