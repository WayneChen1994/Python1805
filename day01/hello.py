print("hello world!!!")
print('hello')
print('''
good
nice
great
''')
print("hello", "world")

# print(123)
# a = 10
# print(a)

# 30 计算得到的
# 10 + 20 = 30
a = 10
b = 20
# print(a, "+", b, "=", a+b)

# 格式化输出
# 整数%d  浮点数%f 字符串%s
print("%d + %d = %d" % (a, b, a+b))

# 阻塞式线程
# name = input("请输入您的用户名：")
# print(name)

'''
需求：写一个自我介绍：
要求从控制台输入，输入完毕之后，打印结果
姓名、年龄、籍贯、兴趣爱好
'''
# name = input("请输入您的名字：")
age = input("请输入您的年龄：")
# address = input("请输入您的籍贯：")
# hobby = input("请输入您的兴趣爱好：")
print("我今年%s岁" % age)
print(type(age))
# print("我是%s，今年%s岁，来自于%s，我喜欢%s" % (name, age, address, hobby))

# 结论：从input获取的内容类型都为字符串类型

