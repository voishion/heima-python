#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Desc    : 使用zip()并行迭代
    Author  : Lu Li (李露)
    File    : 11_使用zip()并行迭代.py
    Date    : 2023/12/2 22:55
    Site    : https://gitee.com/voishion
    Project : heima-python
"""
# 可以使用zip()函数对多个序列进行并行迭代，zip()函数在最短序列“用完”时就会停止。
names = ("赵四", "刘能", "谢广坤", "王老七", "徐支书")
ages = (18, 16, 23, 45)
jobs = ("花匠", "参谋", "收山货")

for name, age, job in zip(names, ages, jobs):
    print(f'{name}--{age}--{job}')
