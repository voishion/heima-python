#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Desc    : 说明
    Author  : Lu Li (李露)
    File    : 4-7 类方法、静态方法和实例方法.py
    Date    : 2023/11/27 11:20
    Site    : https://gitee.com/voishion
    Project : heima-python
"""


class Date:
    def __init__(self, year, month, day):
        """
        构造函数，实例方法
        """
        self.year = year
        self.month = month
        self.day = day

    def tomorrow(self):
        """
        实例方法
        """
        self.day += 1

    def __str__(self):
        """
        实例方法
        """
        return "{}/{}/{}".format(self.year, self.month, self.day)

    @staticmethod
    def parse_from_str(date_str: str):
        """
        静态方法
        """
        year, month, day = tuple(date_str.split('-'))
        return Date(int(year), int(month), int(day))

    @classmethod
    def parse_from_str2(cls, date_str: str):
        """
        类方法
        """
        year, month, day = tuple(date_str.split('/'))
        return cls(int(year), int(month), int(day))


if __name__ == '__main__':
    new_date = Date(2023, 11, 27)
    print(new_date)
    new_date.tomorrow()
    print(new_date)

    # 传递2023-11-28字符串返回Date对象
    new_date = Date.parse_from_str('2023-11-28')
    print(new_date)
    # 传递2023/11/29字符串返回Date对象
    new_date = Date.parse_from_str2('2023/11/29')
    print(new_date)

