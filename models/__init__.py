from main import db
from settings import Setting

# 在此处导入需要使用的数据库对象模型
from .roles import Role
from .permissions import Permission
from .users import User
from .products import Product
from .categories import Category
from .suppliers import Supplier
from .quotation_details import QuotationDetails
from .quotations import Quotation
from .customers import Customer
from .contacts import Contacter
from .messages import Message
from .message_addresses import MessageAddress
from .config import Config
from .images import Image
from .files import File
from .scheduler_logs import SchedulerLog


def init_db():
    """删除数据库中所有数据并初始化"""
    db.create_all()

    admins = Role(id=1, name='管理员')
    admins.save()

    users = Role(id=2, name='普通用户')
    users.save()

    admin = User(id=1, username='admin', nickname='Administrator',
                 password='123456', role_id=admins.id)
    admin.save()

    print("The database has been created.")
