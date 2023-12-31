# 定义装饰器
def logging(fn):  # fn = sum_num
    def inner(*args, **kwargs):
        result = fn(*args, **kwargs)
        return result

    return inner  # sum_num = inner

# 使用装饰器装饰函数
@logging
def sum_num(*args, **kwargs):
    print(args, kwargs)


num = sum_num(1, 2, 3, age="18")
print(num)
