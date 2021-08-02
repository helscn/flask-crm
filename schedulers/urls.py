#!/usr/bin/python3
# -*- coding: utf-8 -*-

from main import scheduler
from auth import login_required
from flask_restful import abort, Resource


class ApiJobs(Resource):
    # decorators = [login_required]
    def get(self):
        jobs = scheduler.get_jobs()
        print(jobs[0].pending)

        return (dir(jobs[0]))


class ApiJob(Resource):
    # decorators = [login_required]
    def get(self, name=None):
        scheduler.add_job(id=name, func=name, name=name,
                          trigger='interval', seconds=6)
        return 'OK'
