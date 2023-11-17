#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Desc    : 推导式_练习题2[range(3)=>0,1,2; range(1,3)=>1,2;]
    Author  : Lu Li (李露)
    File    : 12_推导式_练习题2.py
    Date    : 2023/11/16 10:20
    Site    : https://gitee.com/voishion
    Project : heima-python
"""
# 请用列表推导式实现，踢出列表中的字符串，最终生成一个新的列表保存
data_list = [11, 22, 33, '赵四', 455, '刘能']
data_list_new = [item for item in data_list if type(item) == int]
print('data_list_new:{}'.format(data_list_new))

# 请用列表推导式实现，对data_list中的每个元素判断，如果是字符串类型，则计算长度作为元素放在新列
# 表的元素中；如果是整型，则让其值+100作为元素放在新的列表的元素中。
data_list = [11, 22, 33, '赵四', 455, '谢广坤']
data_list_new = [item + 100 if type(item) == int else len(item) for item in data_list]
print('data_list_new:{}'.format(data_list_new))

# 请使用字典推导式实现，将如果列表构造成指定格式字典
data_list = [
    (1, '刘能', 46),
    (2, '赵四', 45),
    (3, '谢广坤', 48)
]
# ---> 请使用推导式将data_list构造成如下格式：
"""
info_dict = {
    1: (1, '刘能', 46),
    2: (2, '赵四', 45),
    3: (3, '谢广坤', 48)
}
"""
info_dict = {item[0]: item for item in data_list}
print('info_dict:{}'.format(info_dict))

# 有5个人玩扑克牌比大小，请对比字典中每个人的牌的大小，并输入优胜者的姓名（值大的胜利，不必考虑A）。
player = {
    '刘能': ['红桃', 10],
    '赵四': ['黑桃', 8],
    '谢广坤': ['梅花', 3],
    '王老七': ['方块', 12]
}
player_name = sorted(player.items(), key=lambda x: x[-1][-1])[-1][0]
print('player_name_1:{}'.format(player_name))
player_name = sorted(player.items(), key=lambda x: x[1][1], reverse=True)[0][0]
print('player_name_2:{}'.format(player_name))

# 请编写一个生成器函数实现生成n个斐波拉契数列的值
"""
    什么是斐波拉契数列？==>前两个数相加的结果，就是下一个数
    1 1 2 3 5 8 13 21 34 55 ...
"""
def fib(max_count):
    first = 1
    second = 0
    count = 0
    while count < max_count:
        next_value = first + second
        first = second
        second = next_value
        yield next_value
        count += 1


fib_generator = fib(10)
for num in fib_generator:
    print(num, end=' ')
