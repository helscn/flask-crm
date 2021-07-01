#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

import html


def text(text):
    '''安全转换为HTML显示文本，但会额外将换行符替换为<br />，和 safe 过滤器一起使用'''
    safe_text = html.escape(str(text))
    safe_text = safe_text.replace('\n', '<br />')
    return safe_text
