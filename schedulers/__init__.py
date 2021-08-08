#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from os import path
from main import scheduler
from flask import Blueprint
from flask_restful import Api

from .filelock import FileLock

__all__ = ['Scheduler', 'SchedulerLock', 'scheduler']

# 获取文件锁
BASE_DIR = path.abspath(path.dirname(__file__))
SchedulerLock = FileLock(path.join(BASE_DIR, 'scheduler.lock'))
SchedulerLock.lock()

# 创建 scheduler 资源蓝图
Scheduler = Blueprint('scheduler', __name__)

# 如果获取到文件锁，将导入的 Restful API 资源注册到蓝图中，并启动 scheduler
if SchedulerLock.locked:
    from .api import ApiJobs, ApiJob, ApiLogs
    from . import listener
    api = Api(Scheduler)
    api.add_resource(ApiJobs, '/jobs', endpoint='jobs')
    api.add_resource(ApiJob, '/job/<id>', endpoint='job')
    api.add_resource(ApiLogs, '/logs', endpoint='logs')
    scheduler.start()
