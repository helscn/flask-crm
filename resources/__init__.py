#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from flask import Blueprint
from flask_restful import Api

# 从当前路径中导入需要加载的 Restful 资源对象
from .users import ApiUser, ApiUsers
from .roles import ApiRole, ApiRoles
from .files import ApiFile, ApiFiles
from .images import ApiImage, ApiImages


# 创建资源蓝图
Resources = Blueprint('api', __name__)

# 将导入的 Restful API 资源注册到蓝图中
api = Api(Resources)
api.add_resource(ApiUser, '/user/<int:id>', endpoint='user')
api.add_resource(ApiUsers, '/users')
api.add_resource(ApiRole, '/role/<int:id>', endpoint='role')
api.add_resource(ApiRoles, '/roles')
api.add_resource(ApiFile, '/file/<int:id>', endpoint='file')
api.add_resource(ApiFiles, '/files')
api.add_resource(ApiImage, '/image/<int:id>', endpoint='image')
api.add_resource(ApiImages, '/images')

__all__ = ['Resources']
