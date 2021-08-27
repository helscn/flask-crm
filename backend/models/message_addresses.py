#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from .base_model import db, BaseModel
from datetime import datetime


class MessageAddress(BaseModel):
    __tablename__ = 'msg_addrs'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    address = db.Column(db.String(256), index=True, default='')
    msg_id = db.Column(db.Integer, db.ForeignKey('messages.id'))

    @staticmethod
    def get(id):
        """根据ID返回对象"""
        if not id:
            return None
        return MessageAddress.query.filter_by(id=id).first()
