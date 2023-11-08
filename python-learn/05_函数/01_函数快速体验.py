"""
演示：快速体验函数的开发及应用
"""
# 需求，统计字符串的长度，不使用内置函数len()
str1 = 'Hello world'
str2 = 'Hello world, Tom'
str3 = 'Hello world, Alex'


def my_len(data):
    count = 0
    for i in data:
        count += 1
    print(f"字符串[{data}]的长度是{count}")


my_len(str1)
my_len(str2)
my_len(str3)

print("欢迎来到黑马程序员！请出示您的健康码以及72小时核酸证明，并配合测量体温！")
print("体温测量中，您的体温是：37.3度，体温正常请进！")
