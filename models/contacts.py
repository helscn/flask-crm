#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from .base_model import db, BaseModel


class Contact(BaseModel):
    __tablename__ = 'contacts'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64), default='')
    title = db.Column(db.String(64), default='')
    department = db.Column(db.String(64), default='')
    email = db.Column(db.String(256), unique=True)
    phone = db.Column(db.String(30), default='')
    address = db.Column(db.String(256), default='')
    comment = db.Column(db.Text, default='')
    valid = db.Column(db.Integer, default=2)
    last_contact_date = db.Column(db.DateTime)
    last_checked_log = db.Column(db.String(256), default='')
    last_checked_date = db.Column(db.DateTime)
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'))

    @staticmethod
    def get(id):
        """根据ID返回对象"""
        if not id:
            return None
        return Contact.query.filter_by(id=id).first()
