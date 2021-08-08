#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from .base_model import db, BaseModel
from datetime import datetime

class SchedulerLog(BaseModel):
    __tablename__ = 'apscheduler_logs'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date = db.Column(db.DateTime)
    type = db.Column(db.String(10), default='')
    name = db.Column(db.String(256), default='')
    func = db.Column(db.String(256), default='')
    trigger = db.Column(db.String(32), default='')
    run_time =db.Column(db.DateTime)
    message = db.Column(db.String(256), default='')
    detail = db.Column(db.Text, default='')

    @staticmethod
    def get(id):
        """根据角色ID返回角色对象"""
        if not id:
            return None
        return SchedulerLog.query.filter_by(id=id).first()
