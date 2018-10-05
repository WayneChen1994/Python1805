'''
参数的传递分为：
值传递：
指传递的参数为不可变类型，比如：
str/number/bool/None/tuple
引用传递：
指传递的可变类型，比如：
list/dict/set
'''


def func(a):
    print(a)
    print(id(a))


b = 20
print(id(b))
func(b)


def func2(l):
    l = list1
    l[-1] = "hello"
    print(l)
    print(id(l))


list1 = [1, 2, 3, 4]
print(id(list1))
func2(list1)
print(list1)
