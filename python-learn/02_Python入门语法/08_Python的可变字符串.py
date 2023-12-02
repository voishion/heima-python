# Python的可变字符串，相当于Java的StringBuffer和StringBuilder
import io

content = 'Hello world'

sio = io.StringIO(content)

print(type(sio))
print(sio)
print(sio.getvalue())

# 实现替换功能
# 将指针移动到指定位置，从1开始，
sio.seek(7)
sio.write('gss')
print(sio.getvalue())








