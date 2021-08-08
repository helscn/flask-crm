
from settings import Setting
from apscheduler.triggers.interval import IntervalTrigger
from apscheduler.triggers.cron import CronTrigger
from apscheduler.triggers.date import DateTrigger

'''
计划任务管理器需要使用到的公共函数。
'''

def trigger_to_dict(trigger):
    '''
    将触发器对象转换为字典对象。
    '''
    if type(trigger) is CronTrigger:
        return {
            'type': 'cron',
            'start_date': trigger.start_date.strftime(Setting.DATETIME_FORMAT) if trigger.start_date else None,
            'end_date': trigger.end_date.strftime(Setting.DATETIME_FORMAT) if trigger.end_date else None,
            'fields': {field.name: str(field) for field in trigger.fields}
        }
    elif type(trigger) is IntervalTrigger:
        return {
            'type': 'interval',
            'start_date': trigger.start_date.strftime(Setting.DATETIME_FORMAT) if trigger.start_date else None,
            'end_date': trigger.end_date.strftime(Setting.DATETIME_FORMAT) if trigger.end_date else None,
            'interval': trigger.interval_length
        }

    elif type(trigger) is DateTrigger:
        return {
            'type': 'date',
            'run_date': trigger.run_date.strftime(Setting.DATETIME_FORMAT)
        }
    else:
        return {
            'type': trigger.__module__
        }


def job_to_dict(job):
    '''
    将任务对象转换为字典对象
    '''
    return {
        'id': job.id,
        'name': job.name,
        'func': get_job_func_name(job),
        'args': job.args,
        'kwargs': job.kwargs,
        'pending': job.pending,
        'trigger': trigger_to_dict(job.trigger),
        'next_run_time': job.next_run_time.strftime(Setting.DATETIME_FORMAT) if job.next_run_time else None,
        'misfire_grace_time': job.misfire_grace_time,
        'coalesce': job.coalesce,
        'max_instances': job.max_instances
    }


def get_job_func_name(job):
    '''
    获取任务对象的运行函数名字，省略了任务模块前缀。
    '''
    if job.func_ref.startswith(Setting.SCHEDULER_JOBS_PATH):
        return job.func_ref[(len(Setting.SCHEDULER_JOBS_PATH)+1):]
    else:
        return job.func_ref


def get_job_trigger_type(job):
    '''
    获取任务对象的触发器类型，返回值为 str 类型。
    '''
    trigger = job.trigger
    name = trigger.__module__
    if type(trigger) is CronTrigger:
        name = 'cron'
    elif type(trigger) is IntervalTrigger:
        name = 'interval'
    elif type(trigger) is DateTrigger:
        name = 'date'
    return name
