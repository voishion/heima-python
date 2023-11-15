# 路由列表
func_list = {}


# 路由装饰器 向列表中添加数据
def route(data):  # data=>/index.html

    def func_out(func):  # func=> index
        # 添加数据
        func_list[data] = func

        def func_inner():
            pass

        return func_inner

    return func_out


@route("/index.html")  # 1 @func_out  2 index = func_out(index)
def index():
    # 读取模板数据返回给浏览器
    with open("./template/index.html") as f:
        file_data = f.read()

    # 模板中的数据替换
    content = file_data.replace("{%content%}", "stock_data", 1)

    return content


@route("/center.html")
def center():
    # 读取模板数据返回给浏览器
    with open("./template/center.html") as f:
        file_data = f.read()

    # 模板中的数据替换
    content = file_data.replace("{%content%}", "stock_data", 1)

    return content


def error():
    return "404 error"

# 向路由列表中添加数据
# func_list["/index.html"] = index
# func_list["/center.html"] = center
# 列表中的数据
# {
#     "/index.html":index,
#     "/center.html":center
# }


# 接口 解耦和
def application(request_path):
    # if request_path == "/index.html":
    #     # 应答体
    #     return index()
    # elif request_path == "/center.html":
    #     # 应答体
    #     return center()
    # else:
    #     # 应答体
    #     return error()
    try:
        # 正确的结果
        # index         "/index.html"
        func = func_list[request_path]
        #     index()
        ret = func()
        # 返回对动态数据的处理结果
        return ret
    except Exception as e:
        # 出现错了
        return error()
