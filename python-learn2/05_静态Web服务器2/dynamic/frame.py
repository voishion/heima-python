def index():
    # xxxx
    return "index"

def center():
    # xxxx
    return "center"

def error():
    return "404 error"

# 接口 解耦和
def application(request_path):
    if request_path == "/index.html":
        # 应答体
        return index()
    elif request_path == "/center.html":
        # 应答体
        return center()
    else:
        # 应答体
        return error()
#