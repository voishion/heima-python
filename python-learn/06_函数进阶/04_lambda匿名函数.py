"""
演示lambda匿名函数，在编写匿名函数时，由于受限 函数体只能写一行，所以展名函数只能处理非常简单的功能。
格式如下：
    lambda 参数列表: 执行体，并将结果返回
"""


# 定义一个函数，接受其它函数输入
def test_func(compute):
    result = compute(1, 2)
    print(f"结果是:{result}")


# 通过lambda匿名函数的形式，将匿名函数作为参数传入
def add(x, y):
    return x + y


test_func(add)
test_func(lambda x, y: x + y)


# 练习题
# 根据函数写出其匿名函欧的表达方式
def func(a1, a2):
    return a1 + a2
print("F1_N:{}".format(func(1, 2)))

func = lambda a1, a2: a1 + a2
print("F1_L:{}".format(func(1, 2)))


def func(data):
    return data.replace("苍老师", "***")
print("F2_N:{}".format(func("苍老师的法术高超")))

func = lambda data: data.replace("苍老师", "***")
print("F2_L:{}".format(func("苍老师的法术高超")))

def func(data):
    name_list = data.split(".")
    return name_list[-1]
print("F3_N:{}".format(func("苍老师的法术高超.mp4")))

func = lambda data: data.split(".")[-1]
print("F3_L:{}".format(func("苍老师的法术高超.mp4")))
