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
        if not para:
            return None
        else:
            return Config.query.filter_by(name=para).first()

    @staticmethod
    def getValue(para):
        """根据ID返回对象"""
        p = Config.get(para)
        if not p:
            return None
        else:
            return json.loads(p.value)

    @staticmethod
    def setValue(para, value):
        p = Config.get(para)
        if p:
            p.value = json.dumps(value)
        else:
            p = Config(name=para, value=json.dumps(value))
        p.save()
