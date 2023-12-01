#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Desc    : 使用bisect插入数据会将数据按顺序排序(升序)，bisect利用二分查找来维护排序序列
    Author  : Lu Li (李露)
    File    : 5-5 bisect维护已排序序列.py
    Date    : 2023/12/1 13:03
    Site    : https://gitee.com/voishion
    Project : heima-python
"""
import bisect

int_list = []

bisect.insort(int_list, 3)
bisect.insort(int_list, 1)
bisect.insort(int_list, 4)
bisect.insort(int_list, 6)
bisect.insort(int_list, 7)
bisect.insort(int_list, 5)
bisect.insort(int_list, 4)

print(int_list)

# 其中默认插入是右边插入insort = insort_right
bisect.insort(int_list, 6.0)
print(int_list)

bisect.insort_left(int_list, 1.0)
print(int_list)

# 查找将会插入的位置
print("将会插入的位:{}".format(bisect.bisect(int_list, 2.0)))
print(int_list)
