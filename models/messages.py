#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from .base_model import db, BaseModel
from datetime import datetime


class Message(BaseModel):
    __tablename__ = 'messages'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    type = db.Column(db.String(20), default='')
    subject = db.Column(db.String(256), default='')
    sender = db.Column(db.String(256), default='')
    date = db.Column(db.DateTime, default=datetime.now())
    content = db.Column(db.Text, default='')
    addrs = db.relationship(
        'MessageAddress', backref='message', lazy='dynamic', cascade='all')

    @staticmethod
    def get(id):
        """根据ID返回对象"""
        if not id:
            return None
        return Message.query.filter_by(id=id).first()
