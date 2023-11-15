"""
copy函数是浅拷贝，只对可变类型的第一层对象进行拷贝，
对拷贝的对象开辟新的内存空间进行存储，不会拷贝对象内部的子对象。
"""
import copy

# 1 普通赋值
# a = [1, 2, 3]
# b = [11, 22, 33]
# c = [a, b]
#
# d = c
#
# print(id(d))
# print(id(c))

# 2 浅拷贝可变类型
a = [1, 2, 3]
b = [11, 22, 33]
c = [a, b]

d = copy.copy(c)

print("浅拷贝可变类型")
print(id(d))
print(id(c))

# 3 浅拷贝-深层数据
a = [1, 2, 3]
b = [11, 22, 33]
c = [a, b]

d = copy.copy(c)

print("浅拷贝-深层数据")
print(id(a))
print(id(c[0]))
print(id(d[0]))

# 4 浅拷贝不可变类型
a = (1, 2, 3)
b = (11, 22, 33)
c = (a, b)

d = copy.copy(c)

print("浅拷贝不可变类型")
print(id(d))
print(id(c))
