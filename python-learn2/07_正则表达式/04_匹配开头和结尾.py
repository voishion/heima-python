import re






# ^	          匹配字符串开头
# 匹配数据
# result = re.match("^\ditcast", "22itcast")
#
# # 获取数据
# if result:
#     info = result.group()
#     print(info)
# else:
#     print("没有匹配到")


# 以数字为开头的字符串
# result = re.match("^\d.*", "2itcast")
#
# # 获取数据
# if result:
#     info = result.group()
#     print(info)
# else:
#     print("没有匹配到")


# $	          匹配字符串结尾
# result = re.match(".*\d$", "itcast")
#
# # 获取数据
# if result:
#     info = result.group()
#     print(info)
# else:
#     print("没有匹配到")


# 匹配以数字为开头以数字为结尾
# result = re.match("^\d.*\d$", "11itcast22")
#
# # 获取数据
# if result:
#     info = result.group()
#     print(info)
# else:
#     print("没有匹配到")
#


# [^指定字符]  匹配除了指定字符以外的所有字符
result = re.match("^\d.*[^4]$", "11itcast@")

# 获取数据
if result:
    info = result.group()
    print(info)
else:
    print("没有匹配到")
