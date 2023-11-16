#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Desc    : 推导式是Python中提供了一个非常方便的功能，可以让我们通过一行代码实现创建list、dict、tuple、set 的同时初始化一些值.
    Author  : Lu Li (李露)
    File    : 11_推导式.py
    Date    : 2023/11/16 10:05
    Site    : https://gitee.com/voishion
    Project : heima-python
"""

# 请创建一个列表，并在列表中初始化: 0、1、2、3、4、5、6、7、8、9...299 整数元素。
data = []
for i in range(300):
    data.append(i)
print("方式1：{}".format(data))

data_list = [i for i in range(300)]
print("方式2：{}".format(data))

# 列表
num_list = [i for i in range(10)]
print("list:{}".format(num_list))
num_list = [[i, i] for i in range(10)]
print("list:{}".format(num_list))
num_list = [[i, i] for i in range(10) if i > 6]
print("list:{}".format(num_list))
num_list = [i + 100 for i in range(10) if i > 6]
print("list:{}".format(num_list))
num_list = ['赵四-{}'.format(i) for i in range(10) if i > 6]
print("list:{}".format(num_list))

# 集合
num_set = {i for i in range(10)}
print('set:{}'.format(num_set))
num_set = {(i, i, i) for i in range(10)}
print('set:{}'.format(num_set))
num_set = {(i, i, i) for i in range(10) if i > 6}
print('set:{}'.format(num_set))

# 字典
num_dict = {i: i for i in range(10)}
print('dict:{}'.format(num_dict))
num_dict = {i: (i, 11) for i in range(10)}
print('dict:{}'.format(num_dict))
num_dict = {i: (i, 11) for i in range(10) if i > 6}
print('dict:{}'.format(num_dict))

# 元组，不同于其他类型，元组不会立即执行内部循环去生成数据，而是得到一个生成器
num_tuple = (i for i in range(10))
print('tuple:{}'.format(num_tuple))
for item in num_tuple:
    print(item)

