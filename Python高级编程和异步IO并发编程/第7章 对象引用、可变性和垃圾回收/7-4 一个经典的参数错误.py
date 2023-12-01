#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Desc    : 传参陷阱示例
    Author  : Lu Li (李露)
    File    : 7-4 一个经典的参数错误.py
    Date    : 2023/12/1 09:03
    Site    : https://gitee.com/voishion
    Project : heima-python
"""


def add(a, b):
    """
    内部使用的是+=, 内存地址不变, 所以在执行a+=b的前后a指向的是同一个地址, 只不过地址里面的值发生改变.

    1、传入的参数是可变类型时，一定要注意引用地址对应值的变化
    2、传入的参数是不可变类型时，就不用担心这个问题
    """
    a += b
    return a


# 传入int值，正常
a = 1
b = 2
c = add(a, b)
print("正常情况[str]：a={a}, b={b}, c={c}".format(a=a, b=b, c=c))

# 传入tuple
a = (1,)
b = (2,)
c = add(a, b)
print("正常情况[tuple]：a={a}, b={b}, c={c}".format(a=a, b=b, c=c))

# 传入list，a的值被改变
a = [1]
b = [2]
c = add(a, b)
print("异常情况：a={a}, b={b}, c={c}".format(a=a, b=b, c=c))


class Company:
    """
    开始体验陷阱
    总结，在调用方法或函数时，传入参数为列表等可变序列时要注意传入参数有可能在函数内部被改变。
    """

    def __init__(self, name, staffs=[]):
        self.name = name
        self.staffs = staffs

    def add(self, staff_name):
        self.staffs.append(staff_name)

    def remove(self, staff_name):
        self.staffs.remove(staff_name)


if __name__ == '__main__':
    company = Company("象牙山村", ["赵四", "刘能"])
    company.add("谢广坤")
    company.remove("赵四")
    print("村民正常：{}".format(company.staffs))

    company1 = Company("温泉度假村1")
    company1.add("王大拿")
    print("温泉度假村1员工正常：{}".format(company1.staffs))

    company2 = Company("温泉度假村2")
    company2.add("刘大脑袋")

    print("\n奇怪，温泉度假村1和温泉度假村2的员工相互竟然相互影响了，太坑了……\n")

    print("温泉度假村1员工异常：{}".format(company1.staffs))
    print("温泉度假村2员工异常：{}".format(company2.staffs))
    print("温泉度假村2员工异常判断：{}".format(company1.staffs is company2.staffs))
    print(Company.__init__.__defaults__)

"""
    想要解决这个问题，Company类的构造函数需要改成如下:
    def __init__(self, name, staffs=None):
        if staffs is None:
            staffs = []
        self.name = name
        self.staffs = staffs
"""