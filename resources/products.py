#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from auth import login_required
from models import db, Product
from settings import Setting
from flask import g, request
from flask_restful import abort, Resource, reqparse
from sqlalchemy.sql import func
from werkzeug.datastructures import FileStorage
from os import path


class ApiProducts(Resource):
    decorators = [login_required]

    def get(self, id=None):
        if id:
            product = Product.get(id)
            if product:
                return product.to_dict()
            else:
                abort(404, error='Product not exist.')
        else:
            products = Product.query.all()
            return {
                'total': len(products),
                'data': [v.to_dict() for v in products]
            }

    @login_required
    def delete(self, id):
        product = Product.get(id)
        if product:
            product.delete()
            return 'Product deleted.', 204
        else:
            abort(404, error='Product not exist.')

    @login_required
    def post(self):
        formParse = reqparse.RequestParser()
        formParse.add_argument('no', type=str, required=True, location='form')
        formParse.add_argument(
            'name', type=str, required=True, location='form')
        formParse.add_argument('spec', type=str, location='form')
        formParse.add_argument('description', type=str, location='form')
        formParse.add_argument('moq', type=int, location='form')
        formParse.add_argument('purchase_price', type=float, location='form')
        formParse.add_argument('refer_price', type=float, location='form')
        formParse.add_argument('comment', type=str, location='form')
        # formParse.add_argument('created_date', type=str, location='form')
        # formParse.add_argument('valid', type=bool, location='form')
        formParse.add_argument('category_id', type=int, location='form')
        formParse.add_argument('thumbnail', type=FileStorage, location='files')
        formParse.add_argument('supplier_id', type=int, location='form')

        form = formParse.parse_args()

        return {'success': True}, 201


class ApiNewProductNo(Resource):
    # decorators = [login_required]

    def get(self):
        maxNo = db.session.query(func.max(Product.id)).first()[0]
        newNo = maxNo+1 if maxNo else 1
        return {'no': 'DT-{:0>5d}'.format(newNo)}
