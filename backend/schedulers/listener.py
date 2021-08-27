#!/usr/bin/python3
# -*- coding: utf-8 -*-

from main import scheduler
from models import SchedulerLog
from .func import get_job_trigger_type, get_job_func_name
from apscheduler.events import EVENT_JOB_ADDED, EVENT_JOB_REMOVED, EVENT_JOB_SUBMITTED, EVENT_JOB_EXECUTED, EVENT_JOB_ERROR, EVENT_JOB_MAX_INSTANCES, EVENT_JOB_MISSED
from datetime import datetime

'''
计划任务的事件监听函数，用于将任务事件信息保存至数据库。
'''


def job_added(Event):
    job = scheduler.get_job(Event.job_id)
    log = SchedulerLog(
        date=datetime.now(),
        type='消息',
        name=Event.job_id,
        trigger=get_job_trigger_type(job),
        func=get_job_func_name(job),
        message='新建计划任务',
        detail='触发器：'+str(job.trigger) +
                '\n位置参数：'+str(job.args) +
                '\n命名参数：'+str(job.kwargs)
    )
    log.save()


def job_removed(Event):
    log = SchedulerLog(
        date=datetime.now(),
        type='消息',
        name=Event.job_id,
        trigger='（未知）',
        func='（未知）',
        message='已删除计划任务。',
        detail='当前任务已被删除，无法获取详细的任务信息。'
    )
    log.save()


def job_max_instances(Event):
    job = scheduler.get_job(Event.job_id)
    if job:
        log = SchedulerLog(
            date=datetime.now(),
            type='警告',
            name=Event.job_id,
            trigger=get_job_trigger_type(job),
            func=get_job_func_name(job),
            message='超过计划任务最大实例上限，任务执行被跳过!',
            detail='触发器：'+str(job.trigger) +
                    '\n位置参数：'+str(job.args) +
                    '\n命名参数：'+str(job.kwargs)
        )
    else:
        log = SchedulerLog(
            date=datetime.now(),
            type='警告',
            name=Event.job_id,
            trigger='（未知）',
            func='（未知）',
            message='超过计划任务最大实例上限，任务执行被跳过!',
            detail='当前任务已被删除，无法获取详细的任务信息。'
        )
    log.save()


def job_submitted_listener(Event):
    job = scheduler.get_job(Event.job_id)
    if job:
        log = SchedulerLog(
            date=datetime.now(),
            type='消息',
            name=Event.job_id,
            trigger=get_job_trigger_type(job),
            func=get_job_func_name(job),
            message='计划任务开始执行...',
            detail='触发器：'+str(job.trigger) +
                    '\n位置参数：'+str(job.args) +
                    '\n命名参数：'+str(job.kwargs)
        )
    else:
        log = SchedulerLog(
            date=datetime.now(),
            type='消息',
            name=Event.job_id,
            trigger='（未知）',
            func='（未知）',
            message='计划任务开始执行...',
            detail='当前任务已被删除，无法获取详细的任务信息。'
        )
    log.save()


def job_executed_listener(Event):
    job = scheduler.get_job(Event.job_id)
    if job:
        log = SchedulerLog(
            date=datetime.now(),
            type='消息',
            name=Event.job_id,
            trigger=get_job_trigger_type(job),
            func=get_job_func_name(job),
            message='任务执行完毕。',
            detail='触发器：'+str(job.trigger) +
                    '\n位置参数：'+str(job.args) +
                    '\n命名参数：'+str(job.kwargs)
        )
    else:
        log = SchedulerLog(
            date=datetime.now(),
            type='消息',
            name=Event.job_id,
            trigger='（未知）',
            func='（未知）',
            message='任务执行完毕。',
            detail='当前任务已被删除，无法获取详细的任务信息。'
        )
    log.save()


def job_missed_listener(Event):
    job = scheduler.get_job(Event.job_id)
    if job:
        log = SchedulerLog(
            date=datetime.now(),
            type='警告',
            name=Event.job_id,
            trigger=get_job_trigger_type(job),
            func=get_job_func_name(job),
            message='计划时间过期，任务未执行。',
            detail='触发器：'+str(job.trigger) +
                    '\n位置参数：'+str(job.args) +
                    '\n命名参数：'+str(job.kwargs)
        )
    else:
        log = SchedulerLog(
            date=datetime.now(),
            type='警告',
            name=Event.job_id,
            trigger='（未知）',
            func='（未知）',
            message='计划时间过期，任务未执行。',
            detail='当前任务已被删除，无法获取详细的任务信息。'
        )
    log.save()


def job_error_listener(Event):
    job = scheduler.get_job(Event.job_id)
    if job:
        log = SchedulerLog(
            date=datetime.now(),
            type='错误',
            name=Event.job_id,
            trigger=get_job_trigger_type(job),
            func=get_job_func_name(job),
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
            message='任务异常停止！',
            detail='当前任务已被删除，无法获取详细的任务信息。'
        )
    log.save()


scheduler.add_listener(job_added, EVENT_JOB_ADDED)
scheduler.add_listener(job_removed, EVENT_JOB_REMOVED)
scheduler.add_listener(job_max_instances, EVENT_JOB_MAX_INSTANCES)
scheduler.add_listener(job_submitted_listener, EVENT_JOB_SUBMITTED)
scheduler.add_listener(job_executed_listener, EVENT_JOB_EXECUTED)
scheduler.add_listener(job_missed_listener, EVENT_JOB_MISSED)
scheduler.add_listener(job_error_listener, EVENT_JOB_ERROR)
