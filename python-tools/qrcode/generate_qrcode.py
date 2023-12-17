#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Desc    : 说明
    Author  : Lu Li (李露)
    File    : generate_qrcode.py
    Date    : 2023/12/16 18:31
    Site    : https://gitee.com/voishion
    Project : heima-python
"""
import qrcode


def generate_qrcode(content, output_path):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=14,
        border=2,
    )
    qr.add_data(content)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(output_path)


def main():
    # 生成分享链接和二维码
    generate_qrcode("https://lightpdf.cn/docs/pwwbb9h", 'SUPTECH 公司资料2024.pdf.png')
    print("二维码已生成为 SUPTECH 公司资料2024.pdf.png")


if __name__ == '__main__':
    main()
