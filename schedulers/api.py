#!/usr/bin/python3
# -*- coding: utf-8 -*-

from main import scheduler
from settings import Setting
from auth import login_required
from flask_restful import abort, Resource, reqparse
from apscheduler.triggers.interval import IntervalTrigger
from apscheduler.triggers.cron import CronTrigger
from apscheduler.triggers.date import DateTrigger
from uuid import uuid1


argParser = reqparse.RequestParser()
argParser.add_argument('id', type=str)
argParser.add_argument('name', type=str)
argParser.add_argument('func', type=str)
argParser.add_argument('args',  type=list, location='json')
argParser.add_argument('kwargs', type=dict, location='json')
argParser.add_argument('start_date', type=str)
argParser.add_argument('end_date', type=str)
argParser.add_argument('misfire_grace_time', type=int, default=1)
argParser.add_argument('coalesce', type=bool, default=True)
argParser.add_argument('trigger', type=str)
argParser.add_argument('fields', type=dict, location='json')

# # date trigger
# argParser.add_argument('run_date', type=str)

# # interval trigger
# argParser.add_argument('interval', type=str)
# argParser.add_argument('seconds', type=int)

# # cron trigger
# argParser.add_argument('year', type=str)
# argParser.add_argument('month', type=str)
# argParser.add_argument('day', type=str)
# argParser.add_argument('week', type=str)
# argParser.add_argument('day_of_week', type=str)
# argParser.add_argument('hour', type=str)
# argParser.add_argument('minute', type=str)
# argParser.add_argument('second', type=str)


class ApiJobs(Resource):
    # decorators = [login_required]
    def get(self):
        jobs = scheduler.get_jobs()
        data = [job_to_dict(job) for job in jobs]
        return {
            'total': len(data),
            'data': data
        }

    def post(self):
        id = uuid1().hex
        try:
            data = argParser.parse_args()
            if not (data['func'] and data['trigger']):
                raise ValueError('Invalid request data.')
            if not data['func'].startswith(Setting.SCHEDULER_JOBS_PATH):
                data['func'] = Setting.SCHEDULER_JOBS_PATH + '.' + data['func']
            if not data['args']:
                data['args'] = None
            else:
                data['args'] = set(data['args'])
            if not data['kwargs']:
                data['kwargs'] = None

            scheduler.add_job(
                id=id,
                name=data['name'],
                func=data['func'],
                args=data['args'],
                kwargs=data['kwargs'],
                trigger=data['trigger'],
                start_date=data['start_date'],
                end_date=data['end_date'],
                misfire_grace_time=data['misfire_grace_time'],
                coalesce=data['coalesce'],
                replace_existing=True,
                timezone=Setting.TIME_ZONE,
                **data['fields']
            )

        except Exception as e:
            abort(400, message=e.args[0])
        return {'success': True}, 201

    def delete(self):
        scheduler.remove_all_jobs()
        return {'success': True}


class ApiJob(Resource):
    # decorators = [login_required]
    def get(self, id):
        try:
            job = scheduler.get_job(id)
            return job_to_dict(job)
        except Exception as e:
            abort(400, message=e.args[0])

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
