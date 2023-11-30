#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Desc    : 说明
    Author  : Lu Li (李露)
    File    : 面试题.py
    Date    : 2023/11/30 10:35
    Site    : https://gitee.com/voishion
    Project : heima-python
"""


def do_something(a, b, *, c, d):
    print('{},{},{},{}'.format(a, b, c, d))


def do_something(*args, **kwargs):
    print(type(args))
    print(type(kwargs))


do_something(1, 2, 3, 4, keyword='L')



print(do_something(1, 2, c=3, d=4))

data_list = [lambda x: x + i for i in range(4)]
v1 = data_list[0](100)
v2 = data_list[3](100)
print('v1={}, v2={}'.format(v1, v2))


# [<function <listcomp>.<lambda> at 0x7faa2a37f6d0>, <function <listcomp>.<lambda> at 0x7faa2e145b40>, <function <listcomp>.<lambda> at 0x7faa2e146200>, <function <listcomp>.<lambda> at 0x7faa2e146290>]
# v1=103, v2=103


def num():
    return (lambda x: i * x for i in range(4))


result = [m(2) for m in num()]
print(result)


class Person:
    name = None

    def __init__(self):
        self.name = 'A'

    def change(self, name):
        self.name = name


person = Person()
person.change('B')
Person.name = 'A'
print(person.name)
