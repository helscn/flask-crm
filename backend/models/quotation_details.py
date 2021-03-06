#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from datetime import datetime
from .base_model import db, BaseModel
from .products import Product


class QuotationDetails(BaseModel):
    __tablename__ = 'quotation_details'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))
    moq = db.Column(db.Integer, nullable=False)
    purchase_price = db.Column(db.Float, nullable=False)  # RMB
    profit_rate = db.Column(db.Float, nullable=False)
    created_date = db.Column(
        db.DateTime, nullable=False, default=datetime.now())
    modified_date = db.Column(
        db.DateTime, nullable=False, default=datetime.now())
    quotation_id = db.Column(db.Integer, db.ForeignKey('quotations.id'))

    @property
    def quote_price(self):
        # USD
        return round(self.purchase_price*(1+self.profit_rate)/self.quotation.exchange_rate, 2)

    @property
    def profit(self):
        return round(self.purchase_price*self.profit_rate, 2)

    @staticmethod
    def get(id):
        """根据ID返回对象"""
        if not id:
            return None
        return QuotationDetails.query.filter_by(id=id).first()

    def to_dict(self):
        data = super().to_dict()
        data['quote_price'] = self.quote_price
        data['profit'] = self.profit
        data['product_no'] = self.product.no
        data['product_name'] = self.product.name
        return data
