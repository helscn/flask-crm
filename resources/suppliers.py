#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from auth import login_required
from models import db, Supplier
from flask import request
from flask_restful import abort, Resource, reqparse

formParse = reqparse.RequestParser()
formParse.add_argument('id', type=int, location='form')
formParse.add_argument('name', type=str, location='form')
formParse.add_argument('contract', type=str, location='form')
formParse.add_argument('address', type=str, location='form')
formParse.add_argument('email', type=str, location='form')
formParse.add_argument('phone', type=str, location='form')
formParse.add_argument('website', type=str, location='form')
formParse.add_argument('comment', type=str, location='form')


class ApiSuppliers(Resource):
    decorators = [login_required]

    def get(self, id=None):
        if id:
            supplier = Supplier.get(id)
            if supplier:
                return supplier.to_dict()
            else:
                abort(404, message='Suppier not exist.')
        else:
            suppliers = Supplier.query.all()
            return {
                'total': len(suppliers),
                'data': [v.to_dict() for v in suppliers]
            }

    def delete(self, id=None):
        if id:
            supplier = Supplier.get(id)
            if supplier:
                supplier.delete()
                return 'Supplier deleted.', 204
            else:
                abort(404, message='Supplier not exist.')
        else:
            data = request.get_json()
            if 'id' in data:
                if type(data['id']) is list:
                    for id in data['id']:
                        supplier = Supplier.get(id)
                        if supplier:
                            supplier.delete()
                else:
                    supplier = Supplier.get(data['id'])
                    if supplier:
                        supplier.delete()
                return 'Supplier deleted.', 204
            else:
                abort(400, message="Invalid request argument.")

    def post(self):
        form = formParse.parse_args()
        if not form['name']:
            abort(400, message="Invalid request argument.")
        supplier = Supplier(
            name=form['name'],
            contract=form['contract'],
            address=form['address'],
            email=form['email'],
            phone=form['phone'],
            website=form['website'],
            comment=form['comment']
        )
        supplier.save()
        return {'success': True}, 201

    def put(self, id=None):
        form = formParse.parse_args()
        if id:
            supplier = Supplier.get(id)
        else:
            supplier = Supplier.get(form['id'])
        if not supplier:
            abort(404, message='Supplier not exist.')
        elif not form['name']:
            abort(400, message="Invalid request argument.")
        supplier.name = form['name']
        supplier.contract = form['contract']
        supplier.address = form['address']
        supplier.email = form['email']
        supplier.phone = form['phone']
        supplier.website = form['website']
        supplier.comment = form['comment']
        supplier.save()
        return {'success': True}, 201
