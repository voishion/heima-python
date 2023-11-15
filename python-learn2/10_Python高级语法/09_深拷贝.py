"""
①浅拷贝使用copy.copy函数
    深拷贝使用copy.deepcopy函数
②不管是给对象进行深拷贝还是浅拷贝，只要拷贝成功就会开辟新的内存空间存储拷贝的对象
③浅拷贝和深拷贝的区别是:
    浅拷贝最多拷贝对象的一层，深拷贝可能拷贝对象的多层。
"""
import copy

# 深拷贝可变类型
a = [1, 2, 3]
b = [11, 22, 33]
c = [a, b]

d = copy.deepcopy(c)

print("深拷贝可变类型")
print(id(c))
print(id(d))

# 深拷贝-深层数据
a = [1, 2, 3]
b = [11, 22, 33]
c = [a, b]

d = copy.deepcopy(c)

print("深拷贝-深层数据")
print(id(a))
print(id(c[0]))
print(id(d[0]))

# 深拷贝不可变类型
a = (1, 2, 3)
b = (11, 22, 33)
c = (a, b)

d = copy.deepcopy(c)

print("深拷贝不可变类型")
print(id(c))
print(id(d))
