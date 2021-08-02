#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from main import scheduler
from flask import Blueprint
from flask_restful import Api

from .urls import ApiJobs, ApiJob

from .test import job

# 创建 scheduler 资源蓝图
Scheduler = Blueprint('scheduler', __name__)
api = Api(Scheduler)

# 将导入的 Restful API 资源注册到蓝图中
api.add_resource(ApiJobs, '/jobs', endpoint='jobs')
api.add_resource(ApiJob, '/job/<name>', endpoint='job')


def job2():
    import time
    time.sleep(4)
    print('Running job2.')


# scheduler.add_job(id='job1', func='schedulers.test:job, name='mytestjob', args=(
#     '循环任务',), trigger='interval', seconds=5)

# scheduler.add_job(id='job2', func="schedulers:job2", name='testjob2',
#                   trigger='interval', seconds=5)


__all__ = ['Scheduler']
