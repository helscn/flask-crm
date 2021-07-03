#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from datetime import datetime
from .base_model import db, BaseModel
from .images import Image


class Product(BaseModel):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    no = db.Column(db.String(20), unique=True, nullable=False)
    name = db.Column(db.String(256), nullable=False)
    spec = db.Column(db.String(256), nullable=False, default='')
    description = db.Column(db.Text, nullable=False, default='')
    moq = db.Column(db.Integer, nullable=False, default=1)
    purchase_price = db.Column(db.Float, nullable=False, default=0.00)
    refer_price = db.Column(db.Float, nullable=False, default=0.00)
    created_date = db.Column(
        db.DateTime, nullable=False, default=datetime.now())
    valid = db.Column(db.Boolean, nullable=False, default=True)
    category_id = db.Column(db.Integer, db.ForeignKey('product_categories.id'))
    thumbnail_id = db.Column(db.Integer)
    supplier_id = db.Column(db.Integer, db.ForeignKey('suppliers.id'))
    labels = db.relationship(
        'Label', backref='product', lazy='dynamic', cascade='all')
    images = db.relationship(
        'Image', backref='product', lazy='dynamic', cascade='all')

    @staticmethod
    def get(id):
        """根据ID返回对象"""
        if not id:
            return None
        return Product.query.filter_by(id=id).first()

    @property
    def thumbnail(self):
        return Image.get(self.thumbnail_id)
