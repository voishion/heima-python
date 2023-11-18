#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Desc    : 演示内置函数
    Author  : Lu Li (李露)
    File    : 07_内置函数.py
    Date    : 2023/11/18 09:52
    Site    : https://gitee.com/voishion
    Project : heima-python
"""


def group01():
    """
    第1组
    """
    print('----{}----'.format('第1组'))
    # abs，绝对值
    v = abs(-10)
    print('abs, value:{}'.format(v))

    # pow，指数
    v = pow(2, 5)  # 2的5次方 ==> 2 ** 5
    print('pow, value:{}'.format(v))
    print('pow, value:{}'.format(2 ** 5))

    # sum，求和
    v = sum([-1, 0, 1, 2, 3])  # 可以被迭代的容器
    print('sum, value:{}'.format(v))
    print('sum, value:{}'.format(v))

    # divmod，求商和余数
    v1, v2 = divmod(9, 2)
    print('divmod, 商:{}，余数:{}'.format(v1, v2))

    # round，小数点后n位（四舍五入）
    v = round(4.11786, 2)
    print('round, value:{}'.format(v))


def group02():
    """
    第2组
    """
    print('----{}----'.format('第2组'))
    # min，最小值
    v = min(11, 2, 3, 4, 5, 56)
    print('min, value:{}'.format(v))
    v = min([11, 12, 33, 55, 6, 23])
    print('min, value:{}'.format(v))
    v = min([11, 12, -33, 55, 2, 23], key=lambda x: abs(x))
    print('min, value:{}'.format(v))  # 2

    # max，最大值
    v = max(11, 2, 3, 4, 5, 56)
    print('max, value:{}'.format(v))
    v = max([11, 12, 33, 55, 6, 23])
    print('max, value:{}'.format(v))
    v = max([11, 12, -33, 78, 2, 23], key=lambda x: x * 10)
    print('max, value:{}'.format(v))  # 78

    # all，是否全部为True
    v = all([1, 2, 0, None])
    print('all, value:{}'.format(v))

    # any，是否存在True
    v = any([0, None, False, '', ""])
    print('any, value:{}'.format(v))


def group03():
    """
    第3组
    """
    print('----{}----'.format('第3组'))
    # bin，十进制转二进制
    v = bin(1024)
    print('bin, value:{}'.format(v))

    # oct，十进制转八进制
    v = oct(1024)
    print('oct, value:{}'.format(v))

    # hex，十进制转十六进制
    v = hex(1024)
    print('hex, value:{}'.format(v))


def group04():
    """
    第4组
    """
    print('----{}----'.format('第4组'))
    # ord，获取字符对应的unicode码点（十进制）
    v = ord('李')
    print('ord, value:{}'.format(v))

    # chr，根据码点（十进制）获取对应字符
    v = chr(26446)
    print('chr, value:{}'.format(v))


def group05():
    """
    第5组
    """
    print('----{}----'.format('第5组'))
    # int
    v = int('26494675')
    print('int, value:{}'.format(v))

    # float
    v = float('96678547.36743')
    print('float, value:{}'.format(v))

    # str
    v = str('329864897')
    print('str, value:{}'.format(v))

    # bytes
    v = bytes('李闲鱼', encoding='UTF-8')
    print('bytes, value:{}'.format(v))

    # bool
    v = bool('')
    print('bool, value:{}'.format(v))
    v = bool("")
    print('bool, value:{}'.format(v))
    v = bool(None)
    print('bool, value:{}'.format(v))
    v = bool(0)
    print('bool, value:{}'.format(v))

    # list
    v = list({0})
    print('list, value:{}'.format(v))

    # dict
    v = dict({(0, 1), (1, 1)})
    print('dict, value:{}'.format(v))

    # tuple
    v = tuple({(0, 1), (1, 1)})
    print('tuple, value:{}'.format(v))

    # set
    v = set([1, 1, 346, 85])
    print('set, value:{}'.format(v))


def group06():
    """
    第6组
    """
    print('----{}----'.format('第6组'))
    # len
    v = len([1, 1, 346, 85])
    print('len, value:{}'.format(v))

    # open
    with open("test.txt", "r", encoding="UTF-8") as f:
        for line in f:
            print('open, value:{}'.format(line))

    # type
    v = type(9)
    print('type, value:{}'.format(v))

    # range
    v = [item for item in range(1, 11, 2)]
    print('range, value:{}'.format(v))

    # enumerate
    list_data = ['刘能', '赵四', '谢广坤', '王老七']
    # for index, value in enumerate(list_data):
    for index, value in enumerate(list_data, 1):
        print('enumerate, index:{}, value:{}'.format(index, value))

    # id
    v = id('李')  # 内存地址
    print('id, value:{}'.format(v))

    # callable，判断是否可执行，后面是否可以加括号
    func = lambda x: x * 5
    v = callable(func)
    print('callable, value:{}'.format(v))

    # sorted
    v = sorted([11, 22, 33, 0, 3, 6])
    print('sorted, value:{}'.format(v))

    info = {'A': {'id': 0, 'age': 19}, 'B': {'id': 1, 'age': 18}, 'C': {'id': 2, 'age': 29}}
    v = sorted(info.items(), key=lambda x: x[1]['age'])
    print('sorted, value:{}'.format(v))

    # N0-N1 xxxx.mp4，按照N1排序
    data_list = [
        '1-5 编译器和解释器.mp4',
        '1-17 今日作业.mp4',
        '1-9 Python解释器种类.mp4',
        '1-16 今日总结.mp4',
        '1-2 课堂笔记的创建.mp4',
        '1-15 Pycharm使用和破解(win系统).mp4',
        '1-12 python解释器的安装(mac系统).mp4',
        '1-13 python解释器的安装(win系统).mp4',
        '1-8 Python介绍.mp4',
        '1-7 编程语言的分类.mp4',
        '1-3 常见计算机基本概念.mp4',
        '1-14 Pycharm使用和破解(mac系统).mp4',
        '1-10 CPython解释器版本.mp4',
        '1-1 今日概要.mp4"',
        '1-6 学习编程本质上的三件事.mp4',
        '1-18 作业答案和讲解.mp4',
        '1-4 编程语言.mp4',
        '1-11 环境搭建说明.mp4'
    ]
    v = sorted(data_list, key=lambda x: int(x.split(' ')[0].split('-')[1]))
    print('sorted, value:{}'.format(v))


if __name__ == '__main__':
    group01()
    group02()
    group03()
    group04()
    group05()
    group06()




