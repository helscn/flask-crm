#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from enum import unique
from .base_model import db, BaseModel
from datetime import datetime


class Supplier(BaseModel):
    __tablename__ = 'suppliers'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(128), unique=True, nullable=False)
    contract = db.Column(db.String(32))
    address = db.Column(db.String(256))
    email = db.Column(db.String(128))
    phone = db.Column(db.String(30))
    website = db.Column(db.String(256))
    comment = db.Column(db.Text)
    created_date = db.Column(
        db.DateTime, nullable=False, default=datetime.now())
    modified_date = db.Column(
        db.DateTime, nullable=False, default=datetime.now())
    products = db.relationship(
        'Product', backref='supplier', lazy='dynamic', cascade='all')

    @staticmethod
    def get(id):
        """根据ID返回对象"""
        if not id:
            return None
        return Supplier.query.filter_by(id=id).first()
