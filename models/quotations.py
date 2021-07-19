#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from datetime import datetime
from .base_model import db, BaseModel


class Quotation(BaseModel):
    __tablename__ = 'quotations'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    no = db.Column(db.String(20), unique=True)
    customer = db.Column(db.String(256))
    status = db.Column(db.String(20))
    exchange_rate = db.Column(db.Float)
    created_date = db.Column(
        db.DateTime, nullable=False, default=datetime.now())
    modified_date = db.Column(
        db.DateTime, nullable=False, default=datetime.now())
    details = db.relationship(
        'QuotationDetails', backref='quotation', lazy='dynamic', cascade='all')

    @staticmethod
    def get(id):
        """根据ID返回对象"""
        if not id:
            return None
        return Quotation.query.filter_by(id=id).first()
