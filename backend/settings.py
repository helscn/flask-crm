# -*- coding: utf-8 -*-

from os import path
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore

BASE_DIR = path.abspath(path.dirname(__file__))

# 数据库连接配置
DIALECT = 'mysql'
DRIVER = 'mysqldb'
USERNAME = 'root'
PASSWORD = '123456'
HOST = '127.0.0.1'
PORT = '3306'
DATABASE = 'db_demo1'

# 通过URI连接数据库，已经安装 mysqldb 支持库，如果需要使用其它数据库，可以修改 requirements.txt
SQLALCHEMY_DATABASE_URI = '{dialect}+{driver}://{username}:{password}@{host}:{port}/{database}?charset=utf8'.format(
    dialect=DIALECT, driver=DRIVER, username=USERNAME, password=PASSWORD, host=HOST, port=PORT, database=DATABASE)

# 默认使用 Sqlite3 访问本地 database.db 数据库，可以注释该行使用其它数据库
SQLALCHEMY_DATABASE_URI = 'sqlite:///{}/database.db'.format(BASE_DIR)


class Setting:
    # Flask 静态资源文件目录，引用文件路径需要增加 /static 前缀
    STATIC_FOLDER = path.join(BASE_DIR, 'static')

    # 自定义静态目录设置,设置为前端build目录，引用文件路径不需要增加任何前缀
    FRONTEND_FOLDER = path.join(BASE_DIR, 'frontend/dist/spa')

    # Flask 模板文件夹路径
    TEMPLATE_FOLDER = path.join(BASE_DIR, 'templates')

    # 文件上传的保存目录
    UPLOAD_FOLDER = path.join(BASE_DIR, 'uploads')

    # 文件上传最大文件大小，单位 bytes
    MAX_CONTENT_LENGTH = 64 * 1024 * 1024

    # 是否允许跨源资源共享访问
    SUPPORT_CORS = True

    # 加密密钥，可以通过 secrets 模块的 secrets.token_hex(16) 获得随机密钥
    # 此密钥用于生成 session ID，cookies 等认证模块
    SECRET_KEY = '06a821a89afd0e1a408a283e5737b3b4'

    # Token 验证的失效时间
    TOKEN_EXPIRATION = 24*60*60

    # 前端请求谁时，保存 Token 的位置，如 headers, cookies, args, values 等
    TOKEN_LOCATION = ['headers', 'cookies', 'args']

    # 前端请求认证时，保存 Token 的键值名称
    TOKEN_KEY = 'Token'

    # 链接数据库
    SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI

    # 数据库连接池的大小，Sqlite 数据库不适用
    # SQLALCHEMY_POOL_SIZE = 5

    # 数据库连接池的连接超时时间，Sqlite 数据库不适用
    # SQLALCHEMY_POOL_TIMEOUT = 10

    # 数据库连接池自动回收连接的秒数。MySQL 默认会自动移除闲置 8 小时或以上的连接
    SQLALCHEMY_POOL_RECYCLE = 60

    # 跟踪数据库修改
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # 打印输出SqlAlchemy生成的Sql语句
    SQLALCHEMY_ECHO = False

    # 数据库请求结束之后自动提交
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True

    # 调试模式
    DEBUG = False

    # APScheduler 任务脚本模块路径
    SCHEDULER_JOBS_PATH = 'schedulers.jobs'

    # APScheduler 任务存储器，保存至当前数据库中
    SCHEDULER_JOBSTORES = {
        'default': SQLAlchemyJobStore(url=SQLALCHEMY_DATABASE_URI)
    }

    # APScheduler 执行器
    SCHEDULER_EXECUTORS = {
        'default': {
            'type': 'threadpool',
            'max_workers': 20
        }
    }

    # 项目内置Scheduler API接口，禁用默认的API(无权限认证功能)
    SCHEDULER_API_ENABLED = False

    # 日期时间对象转化为文本时的格式设置
    DATETIME_FORMAT = '%Y-%m-%d %H:%M:%S'
