#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：Wayne


'''
需求1：判断QQ号是否合法：
1、必须全部为数字
2、不能以0开头
3、长度5~12
写成函数
'''


def isqq(s):
    if s.isdigit() and 5 <= len(s) <= 12 and not s.startswith("0"):
        return True
    else:
        return False

# if __name__ == "__main__":
#     astr = "1231434"
#     astr2 = "0231434"
#     astr3 = "123"
#     astr4 = "12345678a"
#     print(isqq(astr))
#     print(isqq(astr2))
#     print(isqq(astr3))
#     print(isqq(astr4))


'''
判断手机号码是否是合法的电信号码：
1、11位
2、数字
3、前三位：189，133,153,181,180,177
'''


def istelecom(s):
    if s.isdigit() and len(s) == 11 and \
        s[:3] in ["189", "133", "153", "181", "180", "177"]:
        return True
    else:
        return False


# if __name__ == "__main__":
#     phone1 = "18927106340"
#     phone2 = "38927106340"
#     phone3 = "13327106340"
#     phone4 = "133271063"
#     phone5 = "18027106332"
#     phone6 = "12345678901"
#     phone7 = "12345a78901"
#     print(istelecom(phone1))
#     print(istelecom(phone2))
#     print(istelecom(phone3))
#     print(istelecom(phone4))
#     print(istelecom(phone5))
#     print(istelecom(phone6))
#     print(istelecom(phone7))
