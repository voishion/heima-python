#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Author  : Lu Li (李露)
    File    : 3-3 python魔法函数一览.py
    Date    : 2023/11/27 08:56
    Site    : https://gitee.com/voishion
    Project : heima-python
"""


class Company:
    def __init__(self, employee=None):
        self.employee = employee

    def __str__(self):
        return ','.join(self.employee)

    def __repr__(self):
        return '[{}]'.format(', '.join(self.employee))

    def __len__(self):
        return len(self.employee)

    def __getitem__(self, item):
        return self.employee[item]


class Nums:
    def __init__(self, num):
        self.num = num

    def __abs__(self):
        return abs(self.num)


class MyVector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return MyVector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return 'x:{x}, y:{y}'.format(x=self.x, y=self.y)


if __name__ == '__main__':
    # company = Company(["tom", "bob", "june"])
    # print(company)
    # print(company.__repr__())
    # print(len(company))
    # print(company[:2])
    # for e in company:
    #     print(e)

    # my_nums = Nums(-1)
    # print(abs(my_nums))

    vector1 = MyVector(1, 2)
    vector2 = MyVector(3, 4)
    print(vector1 + vector2)
    pass
