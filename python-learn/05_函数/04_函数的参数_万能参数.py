#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Desc    : 演示函数使用万能参数
    Author  : Lu Li (李露)
    File    : 04_函数的参数_万能参数.py
    Date    : 2023/10/27 15:01
    Site    : https://gitee.com/voishion
    Project : zhiliaooa
"""


def args_func(a, b, c=None, *args, **kwargs):
    """
    方法调用参数传递
    :param a: 关键字参数
    :param b: 普通参数
    :param c: 默认参数
    :param args: 不定长参数，以元组(tuple)的形式接收
    :param kwargs: 不定长参数，以字典(dict)的形式接收
    :return: 结果
    """
    print(f"a:{a}")
    print(f"b:{b}")
    print(f"c:{c}")
    # 遍历元组
    print(f'arg type:{type(args)}')
    for arg in args:
        print(f"arg:{arg}")

    # 遍历字典
    # for key in kwargs:
    #     value = kwargs.get(key)
    #     print(f"key={key},value={value}")
    print(f'kwargs type:{type(kwargs)}')
    for key, value in kwargs.items():
        print(f"key={key},value={value}")

    return "finish"


args_func("a", "b")
args_func("a", "b", "c", 1, name="tom", age=12)
args_func("a", "b", "c", 1, 2, name="tom", age=12)
args_func("a", "b", "c", 1, 2, 3, name="tom", age=12)


def star_func(a, b, *, c):
    """
    声明函数时，参数中星号 * 可以单独出现
    如果单独出现星号 *，则星号 * 后的参数必须用关键字传入
    :param a: 普通参数
    :param b: 普通参数
    :param c: 关键字参数
    :return: 结果
    """
    return a + b + c


result = star_func(1, 2, c=3)
print(result)
