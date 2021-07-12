#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from auth import login_required
from models import db, Product
from settings import Setting
from flask import g, request
from flask_restful import abort, Resource, reqparse
from sqlalchemy.sql import func
from werkzeug.datastructures import FileStorage
from PIL import Image
from os import path


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
                    print(id, type(id), product)
                    if product:
                        product.delete()
                return 'Product deleted.', 204
            else:
                abort(400, message="Invalid request argument.")

    def post(self):
        formParse = reqparse.RequestParser()
        formParse.add_argument('no', type=str, required=True, location='form')
        formParse.add_argument(
            'name', type=str, required=True, location='form')
        formParse.add_argument('spec', type=str, location='form')
        formParse.add_argument('description', type=str, location='form')
        formParse.add_argument('moq', type=int, default=1, location='form')
        formParse.add_argument('purchase_price', type=float,
                               default=0.0, location='form')
        formParse.add_argument('profit_rate', type=float,
                               default=0.0, location='form')
        formParse.add_argument('comment', type=str,
                               default='', location='form')
        # formParse.add_argument('created_date', type=str, location='form')
        # formParse.add_argument('valid', type=bool, location='form')
        formParse.add_argument('category_id', type=int, location='form')
        formParse.add_argument('thumbnail', type=FileStorage, location='files')
        formParse.add_argument('supplier_id', type=int, location='form')
        form = formParse.parse_args()
        if not form['no']:
            form['no'] = getNewProductNo()
        product = Product(
            no=form['no'],
            name=form['name'],
            spec=form['spec'],
            description=form['description'],
            moq=form['moq'],
            purchase_price=form['purchase_price'],
            profit_rate=form['profit_rate'],
            comment=form['comment']
        )
        product.save()
        if form['thumbnail']:
            product.set_thumbnail(form['thumbnail'])

        return {'success': True}, 201


class ApiNewProductNo(Resource):
    decorators = [login_required]

    def get(self):
        return {'no': getNewProductNo()}
