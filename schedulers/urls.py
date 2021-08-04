#!/usr/bin/python3
# -*- coding: utf-8 -*-

from main import scheduler
from settings import Setting
from auth import login_required
from flask_restful import abort, Resource
from apscheduler.triggers.interval import IntervalTrigger
from apscheduler.triggers.cron import CronTrigger
from apscheduler.triggers.date import DateTrigger
from uuid import uuid1


class ApiJobs(Resource):
    # decorators = [login_required]
    def get(self):
        jobs = scheduler.get_jobs()
        data = [job_to_dict(job) for job in jobs]
        return {
            'total': len(data),
            'data': data
        }

    def delete(self):
        scheduler.remove_all_jobs()
        return {'success': True}


class ApiJob(Resource):
    # decorators = [login_required]
    def get(self, name=None):
        id = uuid1().hex
        scheduler.add_job(id=id, func='schedulers.jobs.'+name, name=name,
                          trigger='interval', seconds=6, replace_existing=True, timezone=Setting.TIME_ZONE)
        return 'OK'

    def delete(self, id):
        try:
            scheduler.remove_job(id)
            return {'success': True}, 201
        except Exception as e:
            abort(404, message=e.args[0])


def trigger_to_dict(trigger):
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
    return {
        'id': job.id,
        'name': job.name,
        'func': job.func_ref,
        'args': job.args,
        'kwargs': job.kwargs,
        'pending': job.pending,
        'trigger': trigger_to_dict(job.trigger),
        'next_run_time': job.next_run_time.strftime(Setting.DATETIME_FORMAT) if job.next_run_time else None,
        'misfire_grace_time': job.misfire_grace_time,
        'coalesce': job.coalesce,
        'max_instances': job.max_instances
    }
