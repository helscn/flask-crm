#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from .base_model import db, BaseModel
from datetime import datetime


class Contacter(BaseModel):
    __tablename__ = 'contacts'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64), default='')
    gender = db.Column(db.String(1), default='n')
    title = db.Column(db.String(64), default='')
    department = db.Column(db.String(64), default='')
    email = db.Column(db.String(256), unique=True, index=True)
    phone = db.Column(db.String(30), default='')
    address = db.Column(db.String(256), default='')
    comment = db.Column(db.Text, default='')
    subscription = db.Column(db.Boolean, default=True)
    valid = db.Column(db.Integer, default=2)
    created_date = db.Column(db.DateTime, default=datetime.now())
    last_contact_date = db.Column(db.DateTime)
    last_checked_log = db.Column(db.String(256), default='')
    last_checked_date = db.Column(db.DateTime)
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'))

    @staticmethod
    def get(id):
        """根据ID返回对象"""
        if not id:
            return None
        return Contacter.query.filter_by(id=id).first()

    def to_dict(self):
        data = super().to_dict()
        if self.customer:
            data['company'] = self.customer.company
        else:
            data['company'] = None
        return data
