#!/usr/bin/python3
# -*- coding: utf-8 -*-

from main import scheduler
from auth import login_required
from flask_restful import abort, Resource
from apscheduler.triggers.interval import IntervalTrigger
from apscheduler.triggers.cron import CronTrigger
from apscheduler.triggers.date import DateTrigger

from uuid import uuid1


def trigger_to_dict(trigger):
    if type(trigger) is IntervalTrigger:
        return {
            'type': 'interval',
            'start_date': trigger.start_date.strftime('%Y-%m-%d %H:%M:%S %z') if trigger.start_date else None,
            'end_date': trigger.end_date.strftime('%Y-%m-%d %H:%M:%S %z') if trigger.end_date else None,
            'interval': trigger.interval_length
        }

    elif type(trigger) is CronTrigger:
        return {
            'type': 'cron',
            'start_date': trigger.start_date.strftime('%Y-%m-%d %H:%M:%S %z') if trigger.start_date else None,
            'end_date': trigger.end_date.strftime('%Y-%m-%d %H:%M:%S %z') if trigger.end_date else None,
            'interval': trigger.interval_length
        }
    elif type(trigger) is DateTrigger:
        return {
            'type': 'date',
            'run_date': trigger.run_date.strftime('%Y-%m-%d %H:%M:%S %z')
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
        'next_run_time': job.next_run_time.strftime('%Y-%m-%d %H:%M:%S %z'),
        'misfire_grace_time': job.misfire_grace_time,
        'coalesce': job.coalesce,
        'max_instances': job.max_instances
    }


class ApiJobs(Resource):
    # decorators = [login_required]
    def get(self):
        jobs = scheduler.get_jobs()
        return [job_to_dict(job) for job in jobs]


class ApiJob(Resource):
    # decorators = [login_required]
    def get(self, name=None):
        id = uuid1().hex
        scheduler.add_job(id=id, func='schedulers.jobs.'+name, name=name,
                          trigger='interval', seconds=6)
        return 'OK'
