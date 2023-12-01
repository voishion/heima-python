#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Desc    : 语音转换
    Author  : Lu Li (李露)
    File    : voice_convert.py
    Date    : 2023/11/30 18:15
    Site    : https://gitee.com/voishion
    Project : whisperX
"""
import json

import datetime


class VoiceConvert:

    def __init__(self, voice_json_file, txt_result_file):
        self.__voice_json_file = voice_json_file
        self.__txt_result_file = txt_result_file

    def convert(self):
        self.__write_file(self.__read_file())

    def __seconds_to_string(self, seconds):
        # 将秒数转换为 timedelta 对象
        delta = datetime.timedelta(seconds=seconds)

        # 提取小时、分钟和秒
        hours, remainder = divmod(delta.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)

        # 格式化字符串
        time_string = "{:02}:{:02}:{:06.3f}".format(hours, minutes, seconds + delta.microseconds / 1e6)

        return time_string

    def __convert_to_dict(self, item: dict) -> dict:
        return {
            'start': self.__seconds_to_string(item['start']),
            'end': self.__seconds_to_string(item['end']),
            'text': item['text'],
            'speaker': item.get('speaker', 'SPEAKER_未识别'),
        }

    def __convert_to_str(self, element: dict) -> str:
        return '{new_sir}  {start} ~ {end}\n{text}\n\n'.format(
            new_sir=element.get('speaker').replace('SPEAKER', '说话人'),
            start=element.get('start'),
            end=element.get('end'),
            text=element.get('text')
        )

    def __read_file(self) -> list:
        try:
            result = None
            with open(self.__voice_json_file, "r", encoding="UTF-8") as f:
                content = f.read()
                if content:
                    data = json.loads(content)
                    result = [self.__convert_to_dict(item) for item in data['segments'] if 'speaker' in item]

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

    def __write_file(self, data_list):
        try:
            with open(self.__txt_result_file, "w", encoding="UTF-8") as f:
                lines = [self.__convert_to_str(element) for element in data_list]
                lines[-1] = lines[-1].rstrip()[:]
                f.writelines(lines)
        except FileNotFoundError as fife:
            print(f"文件未找到：{fife}")
        except IOError as ioe:
            print(f"IO错误：{ioe}")
        except Exception as e:
            print(f"程序出现异常：{e}")
        else:
            print('写入文件成功')
        finally:
            print('无论如何都会执行的部分')


if __name__ == '__main__':
    convert = VoiceConvert(voice_json_file='demo2.json', txt_result_file='demo2.txt')
    convert.convert()
