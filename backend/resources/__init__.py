#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from flask import Blueprint
from flask_restful import Api

# 从当前路径中导入需要加载的 Restful 资源对象
from .users import ApiUsers
from .roles import ApiRoles
from .customers import ApiCustomers
from .contacts import ApiContacts, ApiCustomerContacts
from .products import ApiProducts, ApiNewProductNo
from .categories import ApiCategories
from .suppliers import ApiSuppliers
from .quotations import ApiQuotations
from .files import ApiFiles
from .images import ApiImages

__all__ = ['Resources']

# 创建资源蓝图
Resources = Blueprint('api', __name__)
api = Api(Resources)

# 将导入的 Restful API 资源注册到蓝图中
api.add_resource(ApiUsers, '/users', '/users/<int:id>', endpoint='users')
api.add_resource(ApiRoles, '/roles', '/roles/<int:id>', endpoint='roles')

api.add_resource(ApiCustomers, '/customers',
                 '/customers/<int:id>', endpoint='customers')
api.add_resource(ApiContacts, '/customers/contacts',
                 '/customers/contacts/<int:id>', endpoint='contacts')
api.add_resource(ApiCustomerContacts, '/customers/<int:id>/contacts',
                 '/customer/<int:id>/contacts', endpoint='customer_contacts')

api.add_resource(ApiNewProductNo, '/products/newno', endpoint='newno')
api.add_resource(ApiProducts, '/products',
                 '/products/<int:id>', endpoint='products')
api.add_resource(ApiCategories, '/products/categories',
                 '/products/categories/<int:id>', endpoint='categories')
api.add_resource(ApiSuppliers, '/products/suppliers',
                 '/products/suppliers/<int:id>', endpoint='suppliers')

api.add_resource(ApiQuotations, '/products/quotations',
                 '/products/quotations/<int:id>', endpoint='quotations')

api.add_resource(ApiFiles, '/files', '/files/<int:id>', endpoint='files')
api.add_resource(ApiImages, '/images', '/images/<int:id>', endpoint='images')
