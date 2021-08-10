#!/usr/bin/python3
# -*- coding: utf-8 -*-

from main import scheduler
from models import db, SchedulerLog
from settings import Setting
from auth import login_required
from flask_restful import abort, Resource, reqparse
from sqlalchemy import or_
from uuid import uuid1
from .req_parser import argParser, logParser
from .func import job_to_dict


class ApiLogs(Resource):
    # decorators = [login_required]
    def get(self):
        args = logParser.parse_args()
        query = SchedulerLog.query
        if args['filter']:
            filter = '%'+args['filter']+'%'
            query = query.filter(or_(
                SchedulerLog.name.ilike(filter),
                SchedulerLog.func.ilike(filter),
                SchedulerLog.trigger.ilike(filter),
                SchedulerLog.message.ilike(filter),
                SchedulerLog.detail.ilike(filter)
            ))
        if args['sort_by'] and hasattr(SchedulerLog, args['sort_by']):
            if args['descending']:
                query = query.order_by(
                    getattr(SchedulerLog, args['sort_by']).desc())
            else:
                query = query.order_by(getattr(SchedulerLog, args['sort_by']))
        pagination = query.paginate(
            args['page'], per_page=args['per_page'], error_out=False)
        return {
            'total': pagination.total,
            'page': pagination.page,
            'pages': pagination.pages,
            'per_page': pagination.per_page,
            'sort_by': args['sort_by'],
            'descending': args['descending'],
            'data': [item.to_dict() for item in pagination.items]
        }

    def delete(self):
        try:
            args = logParser.parse_args()
            query = SchedulerLog.query
            if args['filter']:
                filter = '%'+args['filter']+'%'
                logs = SchedulerLog.query.filter(or_(
                    SchedulerLog.name.ilike(filter),
                    SchedulerLog.func.ilike(filter),
                    SchedulerLog.trigger.ilike(filter),
                    SchedulerLog.message.ilike(filter),
                    SchedulerLog.detail.ilike(filter)
                )).all()
                for log in logs:
                    log.delete(commit=False)
            else:
                query.delete()
            db.session.commit()
        except Exception as e:
            abort(400, message=e.args[0])


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
        try:
            data = argParser.parse_args()
            if data['id']:
                id = data['id']
            else:
                id = uuid1().hex
            if not (data['func'] and data['trigger']):
                raise ValueError('Invalid request data.')
            if Setting.SCHEDULER_JOBS_PATH and (not data['func'].lower().startswith(Setting.SCHEDULER_JOBS_PATH)):
                data['func'] = Setting.SCHEDULER_JOBS_PATH.lower() + \
                    '.' + data['func'].lower()
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
                max_instances=data['max_instances'],
                timezone=data['timezone'],
                replace_existing=True,
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

    def put(self, id):
        try:
            argParser = reqparse.RequestParser()
            argParser.add_argument('action', type=str)
            data = argParser.parse_args()
            job = scheduler.get_job(id)
        except Exception as e:
            abort(404, message=e.args[0])
        try:
            action = data.get('action')
            if action.lower() == 'pause':
                job.pause()
            elif action.lower() == 'resume':
                job.resume()
            else:
                raise ValueError('Unvalid argument.')
            return {'success': True}
        except Exception as e:
            abort(400, message=e.args[0])
