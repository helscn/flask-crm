#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from main import scheduler
from auth import basic_auth

from .test import job


# Schedulers API Token 验证
scheduler.auth = basic_auth


def job2():
    print('job2 started!')


scheduler.add_job(id='job1', func="schedulers.test:job", name='mytestjob', args=(
    '循环任务',), trigger='interval', seconds=5)

scheduler.add_job(id='job2', func="schedulers:job2", name='mytestjob',
                  trigger='interval', seconds=5)


__all__ = ['scheduler']
