#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from auth import login_required
from models import db, Customer, Contacter
from flask_restful import abort, Resource, reqparse
from sqlalchemy.sql import func
from datetime import datetime


argParser = reqparse.RequestParser()
argParser.add_argument('id', type=int)
argParser.add_argument('ids', type=list, location='json', default=[])
argParser.add_argument('name', type=str)
argParser.add_argument('gender', type=int)
argParser.add_argument('title', type=str)
argParser.add_argument('department', type=str)
argParser.add_argument('email', type=str)
argParser.add_argument('phone', type=str)
argParser.add_argument('address', type=str)
argParser.add_argument('comment', type=str)
argParser.add_argument('subscription', type=bool, default=True)
argParser.add_argument('valid', type=int, default=2)
argParser.add_argument('customer_id', type=int)


class ApiCustomerContacts(Resource):
    # decorators = [login_required]

    def get(self, id):
        customer = Customer.get(id)
        if customer:
            contacts = customer.contacts.all()
            return {
                'total': len(contacts),
                'data': [v.to_dict() for v in contacts]
            }
        else:
            abort(404, message='Customer not exist.')


class ApiContacts(Resource):
    # decorators = [login_required]

    def get(self, id=None):
        if id:
            contacter = Contacter.get(id)
            if contacter:
                return Contacter.to_dict()
            else:
                abort(404, message='Contacter not exist.')
        else:
            contacts = Contacter.query.all()
            return {
                'total': len(contacts),
                'data': [v.to_dict() for v in contacts]
            }

    def delete(self, id=None):
        data = argParser.parse_args()
        if id or data['id']:
            contacter = Contacter.get(id or data['id'])
            if contacter:
                contacter.delete()
                return 'Contacter deleted.', 204
        elif len(data['ids']) > 0:
            for id in data['ids']:
                contacter = Contacter.get(id)
                if contacter:
                    contacter.delete()
            return 'Contacter deleted.', 204
        else:
            abort(404, message='Contacter not exist.')

    def post(self):
        data = argParser.parse_args()
        contacter = Contacter.query.filter_by(company=data['company']).first()
        if contacter:
            abort(400, message="Duplicate company name.")
        contacter = Contacter(
            name=data['name'],
            gender=data['gender'],
            title=data['name'],
            department=data['country'],
            email=data['address'],
            phone=data['website'],
            address=data['comment'],
            comment=data['valid'],
            subscription=data['subscription'],
            valid=data['valid'],
            created_date=datetime.now(),
            customer_id=data['customer_id']
        )
        contacter.save()
        return {'success': True}, 201

    def put(self, id=None):
        data = argParser.parse_args()
        if id:
            contacter = Contacter.get(id)
        else:
            contacter = Contacter.get(data['id'])
        if not contacter:
            abort(404, message='Contacter not exist.')
        contacter.name = data['name']
        contacter.gender = data['gender']
        contacter.title = data['title']
        contacter.department = data['department']
        contacter.email = data['email']
        contacter.phone = data['phone']
        contacter.address = data['address']
        contacter.comment = data['comment']
        contacter.subscription = data['subscription']
        contacter.valid = data['valid']
        contacter.save()
        return {'success': True}, 201
