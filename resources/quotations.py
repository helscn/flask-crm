#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from auth import login_required
from models import db, Quotation, QuotationDetails
from flask import request
from flask_restful import abort, Resource, reqparse
from datetime import datetime

quotationParser = reqparse.RequestParser()
quotationParser.add_argument('id', type=int, location='form')
quotationParser.add_argument('no', type=str, location='form')
quotationParser.add_argument('customer', type=str, location='form')
quotationParser.add_argument('status', type=str, location='form')
quotationParser.add_argument('exchange_rate', type=float, location='form')

detailParser = reqparse.RequestParser()
detailParser.add_argument('id', type=int, location='form')
detailParser.add_argument('quotation_id', type=int, location='form')
detailParser.add_argument('product_id', type=int, location='form')
detailParser.add_argument('moq', type=int, location='form')
detailParser.add_argument('purchase_price', type=float, location='form')
detailParser.add_argument('profit_rate', type=float, location='form')


class ApiQuotations(Resource):
    decorators = [login_required]

    def get(self, id=None):
        if id:
            quotation = Quotation.get(id)
            if quotation:
                return quotation.to_dict()
            else:
                abort(404, message='Quotation not exist.')
        else:
            quotations = Quotation.query.all()
            return {
                'total': len(quotations),
                'data': [v.to_dict() for v in quotations]
            }

    def delete(self, id=None):
        if id:
            quotation = Quotation.get(id)
            if quotation:
                quotation.delete()
                return 'Quotation deleted.', 204
            else:
                abort(404, message='Quotation not exist.')
        else:
            data = request.get_json()
            if 'id' in data:
                if type(data['id']) is list:
                    for id in data['id']:
                        quotation = Quotation.get(id)
                        if quotation:
                            quotation.delete()
                else:
                    quotation = Quotation.get(data['id'])
                    if quotation:
                        quotation.delete()
                return 'Quotation deleted.', 204
            else:
                abort(400, message="Invalid request argument.")

    def post(self):
        form = quotationParser.parse_args()
        if not form['no']:
            abort(400, message="Invalid request argument.")
        quotation = Quotation(
            no=form['no'],
            customer=form['customer'],
            status=form['status'],
            exchange_rate=form['exchange_rate']
        )
        quotation.save()
        return {'success': True}, 201

    def put(self, id=None):
        form = quotationParser.parse_args()
        if id:
            quotation = Quotation.get(id)
        else:
            quotation = Quotation.get(form['id'])
        if not quotation:
            abort(404, message='Quotation not exist.')
        quotation.no = form['no']
        quotation.customer = form['customer']
        quotation.status = form['status']
        quotation.exchange_rate = form['exchange_rate']
        quotation.modified_date = datetime.now()
        quotation.save()
        return {'success': True}, 201


class ApiQuotationDetails(Resource):
    decorators = [login_required]
    pass
