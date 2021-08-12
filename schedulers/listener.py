#!/usr/bin/python3
# -*- coding: utf-8 -*-

from main import scheduler
from models import SchedulerLog
from .func import get_job_trigger_type, get_job_func_name
from apscheduler.events import EVENT_JOB_SUBMITTED, EVENT_JOB_EXECUTED, EVENT_JOB_ERROR, EVENT_JOB_MISSED
from datetime import datetime

'''
计划任务的事件监听函数，用于将任务事件信息保存至数据库。
'''


def job_submitted_listener(Event):
    job = scheduler.get_job(Event.job_id)
    if job:
        log = SchedulerLog(
            date=datetime.now(),
            type='消息',
            name=job.name,
            trigger=get_job_trigger_type(job),
            func=get_job_func_name(job),
            run_time=Event.scheduled_run_time,
            message='计划任务开始执行...',
            detail='触发器：'+str(job.trigger) +
                    '\n位置参数：'+str(job.args) +
                    '\n命名参数：'+str(job.kwargs)
        )
    else:
        log = SchedulerLog(
            date=datetime.now(),
            type='消息',
            name='（未知）',
            trigger='（未知）',
            func='（未知）',
            message='计划任务开始执行...'
        )
    log.save()


def job_executed_listener(Event):
    job = scheduler.get_job(Event.job_id)
    if job:
        log = SchedulerLog(
            date=datetime.now(),
            type='消息',
            name=job.name,
            trigger=get_job_trigger_type(job),
            func=get_job_func_name(job),
            run_time=Event.scheduled_run_time,
            message='任务执行完毕。',
            detail='触发器：'+str(job.trigger) +
                    '\n位置参数：'+str(job.args) +
                    '\n命名参数：'+str(job.kwargs)
        )
    else:
        log = SchedulerLog(
            date=datetime.now(),
            type='消息',
            name='（未知）',
            trigger='（未知）',
            func='（未知）',
            message='任务执行完毕，当前任务已过期被删除。'
        )
    log.save()


def job_missed_listener(Event):
    job = scheduler.get_job(Event.job_id)
    if job:
        log = SchedulerLog(
            date=datetime.now(),
            type='警告',
            name=job.name,
            trigger=get_job_trigger_type(job),
            func=get_job_func_name(job),
            run_time=Event.scheduled_run_time,
            message='计划时间过期，任务未执行。',
            detail='触发器：'+str(job.trigger) +
                    '\n位置参数：'+str(job.args) +
                    '\n命名参数：'+str(job.kwargs)
        )
    else:
        log = SchedulerLog(
            date=datetime.now(),
            type='警告',
            name='（未知）',
            trigger='（未知）',
            func='（未知）',
            message='计划时间过期，任务未执行且已被删除。'
        )
    log.save()


def job_error_listener(Event):
    job = scheduler.get_job(Event.job_id)
    if job:
        log = SchedulerLog(
            date=datetime.now(),
            type='错误',
            name=job.name,
            trigger=get_job_trigger_type(job),
            func=get_job_func_name(job),
            run_time=Event.scheduled_run_time,
            message='任务异常停止：' + str(Event.exception),
            detail='触发器：'+str(job.trigger) +
                    '\n位置参数：'+str(job.args) +
                    '\n命名参数：'+str(job.kwargs) +
                    '\n错误回溯：\n'+str(Event.traceback)
        )
    else:
        log = SchedulerLog(
            date=datetime.now(),
            type='错误',
            name='（未知）',
            trigger='（未知）',
            func='（未知）',
            message='任务异常停止，当前任务已过期被删除。'
        )
    log.save()


scheduler.add_listener(job_submitted_listener, EVENT_JOB_SUBMITTED)
scheduler.add_listener(job_executed_listener, EVENT_JOB_EXECUTED)
scheduler.add_listener(job_missed_listener, EVENT_JOB_MISSED)
scheduler.add_listener(job_error_listener, EVENT_JOB_ERROR)
