#!/usr/bin/python3
# -*- coding: utf-8 -*-

from main import scheduler
from models import SchedulerLog
from .func import get_job_trigger_type,get_job_func_name
from apscheduler.events import EVENT_JOB_ERROR, EVENT_JOB_MISSED, EVENT_JOB_EXECUTED
from datetime import datetime

'''
计划任务的事件监听函数，用于将任务事件信息保存至数据库。
'''

def job_executed_listener(Event):
    job = scheduler.get_job(Event.job_id)
    log = SchedulerLog(
        date=datetime.now(),
        type='消息',
        name=job.name,
        trigger=get_job_trigger_type(job),
        func=get_job_func_name(job),
        run_time=Event.scheduled_run_time,
        message='任务执行完毕。',
        detail= '触发器：'+str(job.trigger) +
                '\n位置参数：'+str(job.args) +
                '\n命名参数：'+str(job.kwargs)
    )
    log.save()


def job_missed_listener(Event):
    job = scheduler.get_job(Event.job_id)
    log = SchedulerLog(
        date=datetime.now(),
        type='警告',
        name=job.name,
        trigger=get_job_trigger_type(job),
        func=get_job_func_name(job),
        run_time=Event.scheduled_run_time,
        message='计划时间过期，任务未执行。',
        detail= '触发器：'+str(job.trigger) +
                '\n位置参数：'+str(job.args) +
                '\n命名参数：'+str(job.kwargs)
    )
    log.save()


def job_error_listener(Event):
    job = scheduler.get_job(Event.job_id)
    log = SchedulerLog(
        date=datetime.now(),
        type='错误',
        name=job.name,
        trigger=get_job_trigger_type(job),
        func=get_job_func_name(job),
        run_time=Event.scheduled_run_time,
        message='任务异常停止：' + str(Event.exception),
        detail= '触发器：'+str(job.trigger) +
                '\n位置参数：'+str(job.args) +
                '\n命名参数：'+str(job.kwargs) +
                '\n错误回溯：\n'+str(Event.traceback)
    )
    log.save()

scheduler.add_listener(job_missed_listener, EVENT_JOB_MISSED)
scheduler.add_listener(job_executed_listener, EVENT_JOB_EXECUTED)
scheduler.add_listener(job_error_listener, EVENT_JOB_ERROR)

