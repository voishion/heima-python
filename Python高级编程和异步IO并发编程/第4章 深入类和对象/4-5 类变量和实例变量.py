#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Desc    : 说明
    Author  : Lu Li (李露)
    File    : 4-5 类变量和实例变量.py
    Date    : 2023/11/27 10:40
    Site    : https://gitee.com/voishion
    Project : heima-python
"""


class A:
    aa = 1  # 类变量，所有实例化对象共享的变量

    def __init__(self, x, y):
        self.x = x  # 实例变量
        self.y = y


a = A(2, 3)
print(a.x, a.y, a.aa)  # a.aa首先会去实例a的内存中找是否有aa, 如果没有再去类A的内存中找

# 内变量和实例变量是分开存在的
A.aa = 11  # 会将类A内存中的的aa修改为11
a.aa = 22  # 会在实例a内存中创建一个变量aa赋值22, 类A内存中的aa还是11
print(a.x, a.y, a.aa)  # a.aa首先会去实例a的内存中找是否有aa, 如果没有再去类A的内存中找
print(A.aa)  # 去类A的内存中找aa, 值为11

b = A(3, 5)
print(b.aa)  # 类A内存中aa已经修改为11

