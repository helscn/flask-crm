from main import db
from settings import Setting

# 在此处导入需要使用的数据库对象模型
from .roles import Role
from .permissions import Permission
from .users import User
from .products import Product
from .categories import Category
from .labels import Label
from .suppliers import Supplier
from .images import Image
from .files import File


def init_db():
    """删除数据库中所有数据并初始化"""
    db.drop_all()
    db.create_all()

    admins = Role(id=1, name='管理员')
    admins.save()

    admins.set_permission('user')
    admins.set_permission('users')

    users = Role(id=2, name='普通用户')
    users.save()

    admin = User(id=1, username='admin', nickname='Administrator',
                 password='123456', role_id=admins.id)
    admin.save()

    print("The database has been created.")
