list1 = [1, 2, 3, 4]
tuple1 = (1, 2, 3, 4)
dict1 = {1: 2, 3: 4}
set1 = {1, 2, 3, 4}

# 转为list
print(list(tuple1))
# 将dict转为list的时候，只转了key，没有转value
print(list(dict1))
print(list(set1))
print("*" * 50)


# 转为tuple
print(tuple(list1))
# 将dict转为tuple的时候，只转了key，没有转value
print(tuple(dict1))
print(tuple(set1))

# 转为dict ==> 不支持直接转换
# print(dict1(list1))
# print(dict1(tuple1))
# print(dict1(set1))
print("*" * 50)

# 转为set
print(set(list1))
print(set(tuple1))
# 将dict转为set的时候，只转了key，没有转value
print(set(dict1))

'''
总结：list、tuple、set可以直接相互转换
dict可以转为list、tuple、set【默认只转key，没有value】
不支持直接将list、tuple、set直接转为dict
'''
