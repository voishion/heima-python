#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Desc    : 说明
    Author  : Lu Li (李露)
    File    : 4-2 抽象基类(abc模块).py
    Date    : 2023/11/27 09:36
    Site    : https://gitee.com/voishion
    Project : heima-python
"""
import abc


# 抽象基类不能实例化

class Company(object):
    def __init__(self, employee_list):
        self.employee = employee_list

    def __len__(self):
        return len(self.employee)


# 模拟抽象基类, 只有在调用set方法的时候才会抛出异常，推荐使用这种
# class CacheBase:
#     def get(self, key):
#         raise NotImplementedError
#
#     def set(self, key, value):
#         raise NotImplementedError
#
#
# class RedisCache(CacheBase):
#     def set(self, key, value):
#         pass


# 使用abc模块, 在初始化的时候就会去判断有没有重载基类的方法,没有就抛异常
class CacheBase(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get(self, key):
        pass

    @abc.abstractmethod
    def set(self, key, value):
        pass


class RedisCache(CacheBase):

    def set(self, key, value):
        print('set, k:{}, v:{}'.format(key, value))
        pass

    def get(self, key):
        pass


if __name__ == '__main__':
    com = Company(["bobby1", "bobby2"])
    print(hasattr(com, "__len__"))
    # 第一种用法: 我们去检查某个类是否有某一种方法
    # 第二种用法: 强制某个子类必须实现某些方法
    from collections.abc import Sized
    print(isinstance(com, Sized))

    redis_cache = RedisCache()
    redis_cache.set("key", "value")
    pass
