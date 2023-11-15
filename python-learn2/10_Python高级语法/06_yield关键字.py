"""
注意点：
① 代码执行到 yield 会暂停，然后把结果返回出去，下次启动生成器会在暂停的位置继续往下执行
② 生成器如果把数据生成完成，再次获取生成器中的下一个数据会抛出一个StopIteration 异常，表示停止迭代异常
③ while 循环内部没有处理异常操作，需要手动添加处理异常操作
④ for 循环内部自动处理了停止迭代异常，使用起来更加方便，推荐大家使用。
"""


def generator(num):
    for i in range(num):
        print("开始")
        yield i
        print("生成完成")


g = generator(5)
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))

# g = generater(5)
# for i in g:
#     print(i)
