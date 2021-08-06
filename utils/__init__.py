#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from os import path
from flask import Blueprint

# 从当前路径中导入需要加载的视图对象
from .filters import text
from .createpdf import CreateQuotationPDF
# from .createqrcode import CreateQRCode

CURRENT_FOLDER = path.abspath(path.dirname(__file__))

# 创建 utils 资源蓝图
Utils = Blueprint('utils', __name__,
                  static_folder=path.join(CURRENT_FOLDER, 'static'),
                  template_folder=path.join(CURRENT_FOLDER, 'templates')
                  )

# 将模板过滤器注册到蓝图中
Utils.add_app_template_filter(text, name="text")

# 将导入的函数注册到蓝图中
Utils.add_url_rule('/quotation', view_func=CreateQuotationPDF,
                   endpoint='quotation')
# Utils.add_url_rule('/qrcode', view_func=CreateQRCode, endpoint='qrcode')

__all__ = ['Utils']
