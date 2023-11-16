#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Desc    : 推导式_练习题[range(3)=>0,1,2; range(1,3)=>1,2;]
    Author  : Lu Li (李露)
    File    : 12_推导式_练习题.py
    Date    : 2023/11/16 10:20
    Site    : https://gitee.com/voishion
    Project : heima-python
"""
# 1.去除列表中每个元素的 mp4 后缀
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
result = [item.rsplit('.', 1)[0] for item in data_list]
print(result)

# 2.将字典中的元素按照 键-值 格式化，并最终使用 ; 连接起来
info = {
    "name": "武沛齐",
    "email": "xxxelive.com",
    "gender": "男"
}
result = ';'.join(['{}-{}'.format(k, v) for k, v in info.items()])
print(result)

# 3.将字典按照键从小到大排序，然后在按照如下格式拼接起来。(微信支付API内部处理需求)a=1&b=2
info = {
    'sign_type': "MD5",
    'out_refund_no': "12323",
    'appid': "wx55cca0b94f723dc7",
    'mch_id': "1526049051",
    'out_trade_no': "ffff",
    'nonce_str': "sdfdffd",
    'total_fee': 9901,
    'refund_fee': 10000
}
# 按照键从小到大排序
# result = sorted(info.items(), key=lambda x: x[0])
# print(result)
result = '&'.join(['{}={}'.format(k, v) for k, v in sorted(info.items(), key=lambda x: x[0])])
print(result)


# 看代码写结果（没有执行的函数都不会有执行结果，只有函数引用地址）
def func():
    print(123)


data_list = [func for i in range(2)]
print(data_list)  # [<function func at 0x7fafe2046320>, <function func at 0x7fafe2046320>]

# 没有执行的函数都不会有执行结果，只有函数引用地址
data_list = [lambda: 100 for i in range(2)]
print(data_list)  # [<function <listcomp>.<lambda> at 0x7fafe20463b0>, <function <listcomp>.<lambda> at 0x7fafe2046440>]


def func(num):
    return num + 100


data_list = [func(i) for i in range(2)]
print(data_list)  # [100, 101]

# 推导式嵌套
data_list = [[i, j] for j in range(5) for i in range(10)]
print(data_list)  # [[0, 0], ..., [9, 4]]

# 一副扑克牌
data_list = [[color, num] for num in range(1, 14) for color in ['红桃', '黑桃', '方块', '梅花']]
print('{}张牌'.format(len(data_list)))
print('牌信息:{}'.format(data_list))

# 新浪微博面试题
data_list = [lambda x: x + i for i in range(4)]
print(data_list)  # [<function <listcomp>.<lambda> at 0x7fd58cc464d0>, <function <listcomp>.<lambda> at 0x7fd58cc463b0>]
v1 = data_list[0](100)
v2 = data_list[3](100)
print('v1={}, v2={}'.format(v1, v2))  # v1=103, v2=103


# 烧脑题
def num():
    return [lambda x: i * x for i in range(4)]


result = [m(2) for m in num()]
"""
i = 3
num() = [lambda x: 3 * x, lambda x: 3 * x, lambda x: 3 * x, lambda x: 3 * x]
result = [lambda x: 3 * 2, lambda x: 3 * 2, lambda x: 3 * 2, lambda x: 3 * 2]
"""
print(result)  # [6, 6, 6, 6]


def num():
    return (lambda x: i * x for i in range(4))


result = [m(2) for m in num()]
"""
元组是生成器方式取值，用时才变化，num()返回的元组是是生成器对象
num() = [lambda x: 0 * x, lambda x: 1 * x, lambda x: 2 * x, lambda x: 3 * x]
result = [lambda x: 0 * 2, lambda x: 1 * 2, lambda x: 2 * 2, lambda x: 3 * 2]
"""
print(result)  # [0, 2, 4, 6]
