#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Desc    : 传参陷阱示例
    Author  : Lu Li (李露)
    File    : 7-4 一个经典的参数错误.py
    Date    : 2023/12/1 09:03
    Site    : https://gitee.com/voishion
    Project : heima-python
"""


def add(a, b):
    """
    1、传入的参数是可变类型时，一定要注意引用地址对应值的变化
    2、传入的参数是不可变类型时，就不用担心这个问题
    """
    a += b
    return a


# 传入int值，正常
a = 1
b = 2
c = add(a, b)
print("正常情况[str]：a={a}, b={b}, c={c}".format(a=a, b=b, c=c))
# 传入tuple
a = (1,)
b = (2,)
c = add(a, b)
print("正常情况[tuple]：a={a}, b={b}, c={c}".format(a=a, b=b, c=c))

# 传入list，a的值被改变
a = [1]
b = [2]
c = add(a, b)
print("异常情况：a={a}, b={b}, c={c}".format(a=a, b=b, c=c))

