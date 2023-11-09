"""
演示：定义函数返回值的语法格式
"""


# 定义一个函数，完成2数相加功能
def add(a, b):
    result = a + b
    # 通过返回值，将相加的结果返回给调用者
    return result
    # 返回结果后，还想输出一句话
    print("我完事了")


def add_finally(a, b):
    try:
        result = a + b
        # 通过返回值，将相加的结果返回给调用者
        return result
    finally:
        # 返回结果后，还想输出一句话
        print("我完事了")


# 函数的返回值，可以通过变量去接收
r = add(5, 6)
print(r)

r = add_finally(5, 6)
print(f"add_finally:{r}")
