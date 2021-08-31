#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from auth import login_required
from models import db, Customer, Contacter
from flask import request
from flask_restful import abort, Resource, reqparse
from sqlalchemy.sql import func
from datetime import datetime


argParser = reqparse.RequestParser()
argParser.add_argument('id', type=int)
argParser.add_argument('ids', type=list, location='json')
argParser.add_argument('company', type=str)
argParser.add_argument('importance', type=int)
argParser.add_argument('country', type=str)
argParser.add_argument('address', type=str)
argParser.add_argument('website', type=str)
argParser.add_argument('comment', type=str)
argParser.add_argument('valid', type=bool)
argParser.add_argument('contacts', type=list, location='json')


class ApiCustomers(Resource):
    decorators = [login_required]

    def get(self, id=None):
        if id:
            customer = Customer.get(id)
            if customer:
                return customer.to_dict()
            else:
                abort(404, message='Customer not exist.')
        else:
            customers = Customer.query.all()
            return {
                'total': len(customers),
                'data': [v.to_dict() for v in customers]
            }

    def delete(self, id=None):
        data = request.get_json()
        if id or data['id']:
            customer = Customer.get(id or data['id'])
            if customer:
                customer.delete()
                return 'Customer deleted.', 204
        elif len(data['ids']) > 0:
            for id in data['ids']:
                customer = Customer.get(id)
                if customer:
                    customer.delete()
            return 'Customer deleted.', 204
        else:
            abort(404, message='Customer not exist.')

    def post(self):
        data = argParser.parse_args()
        customer = Customer.query.filter_by(company=data['company']).first()
        if customer:
            abort(400, message="Duplicate company name.")
        customer = Customer(
            company=data['company'].upper(),
            importance=data['importance'],
            country=data['country'],
            address=data['address'],
            website=data['website'],
            comment=data['comment'],
            valid=data['valid'],
            created_date=datetime.now(),
            modified_date=datetime.now()
        )
        customer.save()
        if data['contacts']:
            for info in data['contacts']:
                contacter = Contacter.query.filter_by(
                    email=info['email']).first()
                if contacter:
                    abort(400, message="Duplicate contact email address.")
                if 'id' in info:
                    del info['id']
            for info in data['contacts']:
                contacter = Contacter(**info)
                contacter.customer_id = customer.id
                contacter.save()
        return {'success': True}, 201

    def put(self, id=None):
        data = argParser.parse_args()
        if id:
            customer = Customer.get(id)
        else:
            customer = Customer.get(data['id'])
        if not customer:
            abort(404, message='Customer not exist.')
        customer.company = data['company']
        customer.importance = data['importance']
        customer.country = data['country']
        customer.address = data['address']
        customer.website = data['website']
        customer.comment = data['comment']
        customer.valid = data['valid']
        customer.modified_date = datetime.now()
        customer.save()
        return {'success': True}, 201
