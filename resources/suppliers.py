#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from auth import login_required
from models import db, Supplier
from flask import request
from flask_restful import abort, Resource, reqparse


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
                for id in data['id']:
                    supplier = Supplier.get(id)
                    if supplier:
                        supplier.delete()
                return 'Supplier deleted.', 204
            else:
                abort(400, message="Invalid request argument.")

    def post(self):
        formParse = reqparse.RequestParser()
        formParse.add_argument(
            'name', type=str, required=True, location='form')
        formParse.add_argument('contract', type=str, location='form')
        formParse.add_argument('address', type=str, location='form')
        formParse.add_argument('email', type=str, location='form')
        formParse.add_argument('phone', type=str, location='form')
        formParse.add_argument('website', type=str, location='form')
        formParse.add_argument('comment', type=str, location='form')
        form = formParse.parse_args()

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
