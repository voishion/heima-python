#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Desc    : 说明
    Author  : Lu Li (李露)
    File    : file_process.py
    Date    : 2023/12/1 14:39
    Site    : https://gitee.com/voishion
    Project : heima-python
"""
import json


def read_file(file_path) -> str:
    try:
        result = None
        with open(file_path, "r", encoding="UTF-8") as f:
            result = f.read()

        return result
    except FileNotFoundError as fife:
        print(f"文件未找到：{fife}")
    except IOError as ioe:
        print(f"IO错误：{ioe}")
    except Exception as e:
        print(f"程序出现异常：{e}")
    else:
        print('读取文件成功')
    finally:
        print('无论如何都会执行的部分')


if __name__ == '__main__':
    file_content = read_file('/Users/voishion/Downloads/低代码交流.txt')
    print(json.dumps({'content': file_content}, ensure_ascii=False))
