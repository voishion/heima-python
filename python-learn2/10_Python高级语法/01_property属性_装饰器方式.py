"""
property属性就是负责把类中的一个方法当做属性进行使用
这样做可以简化代码使用
"""


class Person(object):
    def __init__(self):
        self.__age = 0

    # 获取属性
    # @property
    # 表示把方法当做属性使用, 表示当获取属性时会执行下面修饰的方法
    @property
    def age(self):
        return self.__age

    # 修改属性
    # @方法名.setter
    # 表示把方法当做属性使用, 表示当设置属性时会执行下面修饰的方法
    # 装饰器方式的property属性修饰的方法名一定要一样
    @age.setter
    def age(self, new_age):
        self.__age = new_age


# p = Person()
# age = p.age()
# print(age)

p = Person()
print(p.age)
# 修改属性
p.age = 100
print(p.age)
