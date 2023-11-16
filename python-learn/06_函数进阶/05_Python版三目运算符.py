"""
演示Python版三目运算符
格式如下：
    结果 = 条件成立时 if 条件判断 else 条件不成立时
"""


# 定义一个函数，返回最大值
def test_max(x, y):
    # if x > y:
    #     return x
    # else:
    #     return y
    result = x if x > y else y
    return result


max_value = test_max(3, 2)
print("max_value:{}".format(max_value))

# lambda表达式版三元运算
func = lambda x: '太大' if x > 66 else '太小'
print('L3:{}'.format(func(1)))
print('L3:{}'.format(func(100)))
