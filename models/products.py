#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from .base_model import db, BaseModel


class Product(BaseModel):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    sku = db.Column(db.String(20), unique=True, nullable=False)
    name = db.Column(db.String(256), nullable=False)
    description = db.Column(db.Text, default='')
    moq = db.Column(db.Integer, nullable=False, default=1)
    purchase_price = db.Column(db.Float, nullable=False, default=0.00)
    sale_price = db.Column(db.Float, nullable=False, default=0.00)
    category_id = db.Column(db.Integer, db.ForeignKey('product_categories.id'))
    image_id = db.Column(db.Integer, db.ForeignKey('images.id'))
    supplier_id = db.Column(db.Integer, db.ForeignKey('suppliers.id'))
    labels = db.relationship(
        'Label', backref='product', lazy='dynamic', cascade='all')

    @staticmethod
    def get(id):
        """根据ID返回对象"""
        if not id:
            return None
        return Product.query.filter_by(id=id).first()
