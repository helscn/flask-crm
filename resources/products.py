#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from auth import login_required
from models import db, Product, Category,Supplier
from flask import request
from flask_restful import abort, Resource, reqparse
from sqlalchemy.sql import func
from werkzeug.datastructures import FileStorage
from datetime import datetime

formParse = reqparse.RequestParser()
formParse.add_argument('id', type=int, location='form')
formParse.add_argument('no', type=str,  location='form')
formParse.add_argument('name', type=str,location='form')
formParse.add_argument('spec', type=str, location='form')
formParse.add_argument('unit', type=str, location='form')
formParse.add_argument('description', type=str, location='form')
formParse.add_argument('moq', type=int, default=1, location='form')
formParse.add_argument('purchase_price', type=float,
                        default=0.0, location='form')
formParse.add_argument('profit_rate', type=float,
                        default=0.0, location='form')
formParse.add_argument('supplier', type=str, location='form')
formParse.add_argument('category', type=str, location='form')
formParse.add_argument('thumbnail', type=FileStorage, location='files')

def getNewProductNo():
    maxNo = db.session.query(func.max(Product.id)).first()[0]
    newNo = maxNo+1 if maxNo else 1
    No = 'DT-{:0>5d}'.format(newNo)
    while Product.query.filter_by(no=No).first():
        newNo += 1
        No = 'DT-{:0>5d}'.format(newNo)
    return No


class ApiProducts(Resource):
    decorators = [login_required]

    def get(self, id=None):
        if id:
            product = Product.get(id)
            if product:
                return product.to_dict()
            else:
                abort(404, message='Product not exist.')
        else:
            products = Product.query.all()
            return {
                'total': len(products),
                'data': [v.to_dict() for v in products]
            }

    def delete(self, id=None):
        if id:
            product = Product.get(id)
            if product:
                product.delete()
                return 'Product deleted.', 204
            else:
                abort(404, message='Product not exist.')
        else:
            data = request.get_json()
            if 'id' in data:
                for id in data['id']:
                    product = Product.get(id)
                    if product:
                        product.delete()
                return 'Product deleted.', 204
            else:
                abort(400, message="Invalid request argument.")

    def post(self):
        form = formParse.parse_args()
        if not form['no']:
            form['no'] = getNewProductNo()
        supplier=Supplier.query.filter_by(name=form['supplier']).first()
        if supplier:
            supplier_id=supplier.id
        else:
            supplier_id=None
        category=Category.query.filter_by(name=form['category']).first()
        if category:
            category_id=category.id
        else:
            category_id=None
        product = Product(
            no=form['no'].upper(),
            name=form['name'],
            spec=form['spec'],
            unit=form['unit'],
            description=form['description'],
            moq=form['moq'],
            purchase_price=form['purchase_price'],
            profit_rate=form['profit_rate'],
            category_id=category_id,
            supplier_id=supplier_id
        )
        product.save()
        if form['thumbnail']:
            product.set_thumbnail(form['thumbnail'])
        return {'success': True}, 201

    def put(self,id=None):
        form = formParse.parse_args()
        if id:
            product = Product.get(id)
        else:
            product = Product.get(form['id'])
        if not product:
            abort(404, message='Product not exist.')
        supplier=Supplier.query.filter_by(name=form['supplier']).first()
        if supplier:
            supplier_id=supplier.id
        else:
            supplier_id=None
        category=Category.query.filter_by(name=form['category']).first()
        if category:
            category_id=category.id
        else:
            category_id=None
        product.no=form['no'].upper()
        product.name=form['name']
        product.spec=form['spec']
        product.unit=form['unit']
        product.description=form['description']
        product.moq=form['moq']
        product.purchase_price=form['purchase_price']
        product.profit_rate=form['profit_rate']
        product.category_id=category_id
        product.supplier_id=supplier_id
        product.modified_date=datetime.now()
        if form['thumbnail']:
            product.set_thumbnail(form['thumbnail'])
        product.save()
        return {'success': True}, 201

class ApiNewProductNo(Resource):
    decorators = [login_required]

    def get(self):
        return {'no': getNewProductNo()}


