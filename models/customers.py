#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from .base_model import db, BaseModel
from datetime import datetime


class Customer(BaseModel):
    __tablename__ = 'customers'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    company = db.Column(db.String(128), index=True, default='')
    importance = db.Column(db.Integer, default=1)
    country = db.Column(db.String(30), default='')
    address = db.Column(db.String(256), default='')
    website = db.Column(db.String(256), default='')
    comment = db.Column(db.Text, default='')
    valid = db.Column(db.Integer, default=1)
    last_contact_date = db.Column(db.DateTime)
    created_date = db.Column(
        db.DateTime, default=datetime.now())
    contacts = db.relationship(
        'Contact', backref='company', lazy='dynamic', cascade='all')

    @staticmethod
    def get(id):
        """根据ID返回对象"""
        if not id:
            return None
        return Customer.query.filter_by(id=id).first()
