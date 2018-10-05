#! /usr/bin/env python
# -*- coding: utf-8 -*-
# author: Wayne


str1 = '''
how
are you ?
you am
fine
you you'''
print(str1.splitlines())
print(str1.splitlines(keepends=True))
'''
str1.splitlines([keepends=False])
功能：按行分割
注意：当keepends取值为False的时候，则不保留换行【默认为False】
当取值为True的时候，则保留换行符
'''

'''
str1.join(iterable)
要求参数为可迭代对象，string、list、tuple、set、dict
'''
print("".join(["1", "2", "3", "4"]))
print("".join(("1", "2", "3", "4")))


'''
max(str)
功能：获取字符串中ASCII值最大的字符
min(str)
功能：获取字符串中ASCII值最小的字符
'''
print(max("hello"))
print(min("hello"))

'''
str.replace(old,new,count)
old：被替换的子串
new：要替换的新串
count：指定替换的次数，若不指定则匹配到的全部替换，
若指定的次数大于可匹配的次数，则全部替换。
'''
print(str1)
print(str1.replace("you", "me", 1))

str3 = "hello"
str4 = "good lili!hehe"
# 获取一个映射表
dic = str3.maketrans("loa", "896")
print(dic)
# 使用映射表来进行转换
str5 = str4.translate(dic)
print(str5)

# 判断电话号码是否以134开头
'''
str1.startswith(str2,start,end)
判断str1是否以str2开头，若是则返回True否则返回False
start和end我们可以指定范围，若不指定则默认整个字符串。
'''
phoneNum = "13499922201"
print(phoneNum[:3] == "134")
print(phoneNum.startswith("134", 5, 10))

'''
str1.endswith(str2,start,end)
判断str1是否以str2结尾，若是则返回True，否则返回False
start和end也可自己指定
'''
email = "112233@qq.com"
print(email[-7:] == "@qq.com")
print(email.endswith("@qq.com"))

'''
str.encode(encoding,errors)
功能：对指定的字符串进行编码，encoding一般情况下为utf-8，errors="ignore"可以忽略编码出现的错误
str.decode(encoding, errors)
功能：对编码的字符串来进行解码，encoding与编码的encoding保持一致，当errors="ignore"，可以忽略解码的时候编码错误。
'''
china = "中国"
chi = china.encode(encoding="gbk")
print(chi)
print(chi.decode(errors="ignore"))


'''
判断是否全部为字母
注意：中文没有考虑到
str.isalpha()
若全部为字母则返回True，否则返回False
'''
print("hello".isalpha())
print("h1ello".isalpha())
print("he llo".isalpha())
print("hello\n".isalpha())
print("hello你好".isalpha())
print("Hello你好".isalpha())
print("Hello&你好".isalpha())

print("*" * 50)

'''
判断是否只有数字和字母
str.isalnum()
若只有数字和字母，则返回True【没有考虑中文】，否则返回False
'''
print("hello".isalnum())
print("h1ello".isalnum())
print("he llo".isalnum())
print("hello\n".isalnum())
print("hello你好".isalnum())
print("Hello你好".isalnum())
print("Hello&你好".isalnum())

'''
str.isupper()
功能：str至少有一个字母，并且存在的字母必须是大写，这时候才返回True，否则返回False
'''
print("*" * 50)
print("hello".isupper())
print("Hello".isupper())
print("H111".isupper())
print("111".isupper())
print("H中国111".isupper())
print("H中国&&111".isupper())
print("*" * 50)

'''
str.lower()
功能：str中至少存在一个字母，并且所有存在的字母都是小写的，这时候返回True，否则返回False
'''
print("hello".islower())
print("Hello".islower())
print("h中国ello".islower())
print("h%￥#×ello".islower())
print("*" * 50)

'''
str.istitle()
功能：判断str是否为标题化的字符串，所谓的标题化则为单词首字母大写，是则返回True，否则返回False
'''
print("Hello world".istitle())
print("Hello World".istitle())
print("Hello USA".istitle())
print("Hello Usa".istitle())
