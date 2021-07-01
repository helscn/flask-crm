#!/usr/bin/python3
# -*- coding: utf-8 -*-

from main import app
from auth import UserLogin
from resources import Resources
from utils import Utils
from flask import send_from_directory, render_template
import html

# 注册登录 login 蓝图
app.register_blueprint(UserLogin, url_prefix='/auth')

# 注册 Restful API 蓝图
app.register_blueprint(Resources, url_prefix='/api')

# 注册 Utils 蓝图
app.register_blueprint(Utils, url_prefix='/utils')


# 注册前端主页路由
@app.route('/')
@app.route('/index')
def index():
    return send_from_directory(app.config['FRONTEND_FOLDER'], 'index.html')


# 注册前端文件打包路径
@app.route('/<path:filename>')
def frontend(filename):
    return send_from_directory(app.config['FRONTEND_FOLDER'], filename)


# # 默认的错误页面请求处理
# @app.errorhandler(404)
# def page_not_found(e):
#     return render_template('404.html'), 404

# @app.errorhandler(500)
# def internal_server_error(e):
#     return render_template('500.html'), 500
