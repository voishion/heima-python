#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Desc    : 说明
    Author  : Lu Li (李露)
    File    : 4-6 类和实例属性的查找顺序—mro查找.py
    Date    : 2023/11/27 11:04
    Site    : https://gitee.com/voishion
    Project : heima-python
"""


class A:
    name = "A"

    def __init__(self):
        self.name = "obj"


a = A()
print(a.name)


# C3算法

class D:
    pass


class E:
    pass


class C(E):
    pass


class B(D):
    pass


class A(B, C):
    pass


# (
# <class '__main__.A'>,
# <class '__main__.B'>,
# <class '__main__.D'>,
# <class '__main__.C'>,
# <class '__main__.E'>,
# <class 'object'>
# )
print(A.__mro__)


class D:
    pass


class C(D):
    pass


class B(D):
    pass


class A(B, C):
    pass


# (
# <class '__main__.A'>,
# <class '__main__.B'>,
# <class '__main__.C'>,
# <class '__main__.D'>,
# <class 'object'>
# )
print(A.__mro__)
