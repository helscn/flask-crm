#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from .base_model import db, BaseModel
import json


class Config(BaseModel):
    __tablename__ = 'config'
    name = db.Column(db.String(64), primary_key=True)
    value = db.Column(db.Text)

    @staticmethod
    def get(para):
        """根据ID返回对象"""
        if not para:
            return None
        p = Config.query.filter_by(name=para).first()
        if not p:
            return None
        else:
            return json.loads(p.value)

    @staticmethod
    def set(para, value):
        p = Config.query.filter_by(name=para).first()
        if p:
            p.value = json.dumps(value)
        else:
            p = Config(name=para, value=json.dumps(value))
        p.save()
