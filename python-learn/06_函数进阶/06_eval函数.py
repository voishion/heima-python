"""
演示eval()函数使用
功能: 将字符串 str 当成有效的表达式来求值并返回计算结果。
语法: eval(source[,globals[,locals]]) -> value
参数:
    source: 一个Python表达或函数 compile()返回的代码对象
    globals: 可选。必须是 dictionary
    locals: 可选。任意映射对象
"""


python_script = 'print("abc")'
eval(python_script)

a = 10
b = 20
c = eval('a + b')
print('c={}'.format(c))

param = dict(a=100, b=200)
d = eval('a+b', param)
print('d={}'.format(d))




