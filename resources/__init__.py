#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from flask import Blueprint
from flask_restful import Api

# 从当前路径中导入需要加载的 Restful 资源对象
from .users import ApiUsers
from .roles import ApiRoles
from .files import ApiFiles
from .images import ApiImages

__all__ = ['Resources']

# 创建资源蓝图
Resources = Blueprint('api', __name__)
api = Api(Resources)

# 将导入的 Restful API 资源注册到蓝图中
api.add_resource(ApiUsers, '/users/', '/users/<int:id>', endpoint='users')
api.add_resource(ApiRoles, '/roles/', '/roles/<int:id>', endpoint='roles')
api.add_resource(ApiFiles, '/files/', '/files/<int:id>', endpoint='files')
api.add_resource(ApiImages, '/images/', '/images/<int:id>', endpoint='images')
