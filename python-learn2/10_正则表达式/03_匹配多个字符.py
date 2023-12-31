import re







# *	匹配前一个字符出现0次或者无限次，即可有可无
# 匹配数据
# result = re.match("itcast\d*itcast", "itcastitcast")
#
# # 获取数据
# if result:
#     info = result.group()
#     print(info)
# else:
#     print("没有匹配到")


# +	匹配前一个字符出现1次或者无限次，即至少有1次
# 匹配数据
# result = re.match("itcast\d+itcast", "itcast12itcast")
#
# # 获取数据
# if result:
#     info = result.group()
#     print(info)
# else:
#     print("没有匹配到")


# ?	匹配前一个字符出现1次或者0次，即要么有1次，要么没有
# result = re.match("itcast\d?itcast", "itcastitcast")
#
# # 获取数据
# if result:
#     info = result.group()
#     print(info)
# else:
#     print("没有匹配到")


# {m}	匹配前一个字符出现m次
# result = re.match("itcast\d{2}itcast", "itcast12itcast")
#
# # 获取数据
# if result:
#     info = result.group()
#     print(info)
# else:
#     print("没有匹配到")


# {m,n}	匹配前一个字符出现从m到n次
result = re.match("itcast\d{2,5}itcast", "itcast12112312312312312itcast")

# 获取数据
if result:
    info = result.group()
    print(info)
else:
    print("没有匹配到")
