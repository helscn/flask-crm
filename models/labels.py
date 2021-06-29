#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from .base_model import db, BaseModel


class Label(BaseModel):
    __tablename__ = 'product_labels'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))

    @staticmethod
    def get(id):
        """根据ID返回对象"""
        if not id:
            return None
        return Label.query.filter_by(id=id).first()
