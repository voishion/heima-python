#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Desc    : 说明
    Author  : Lu Li (李露)
    File    : 4-1 鸭子类型和多态.py
    Date    : 2023/11/27 09:20
    Site    : https://gitee.com/voishion
    Project : heima-python
"""


class Cat(object):
    def say(self):
        print("i am a cat")


class Dog(object):
    def say(self):
        print("i am a fish")


class Duck(object):
    def say(self):
        print("i am a duck")


class Company(object):
    def __init__(self, employee_list):
        self.employee = employee_list

    def __getitem__(self, item):  # 可迭代
        return self.employee[item]


if __name__ == '__main__':
    # animal_list = [Cat, Dog, Duck]  # 类也是对象, 可以被添加到列表中, 而且python是动态语言, 对于变量不需要指定类型
    # for animal in animal_list:
    #     animal().say()

    # company = Company(["tom", "bob", "jane"])
    # a = ["bobby1", "bobby2"]
    # a.extend(company)
    # print(a) # ['bobby1', 'bobby2', 'tom', 'bob', 'jane']
    pass
