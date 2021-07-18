#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from auth import login_required
from models import db, Category
from flask_restful import abort, Resource, reqparse

class ApiCategories(Resource):
    decorators=[login_required]
    def get(self, id=None):
        if id:
            category = Category.get(id)
            if category:
                return category.to_dict()
            else:
                abort(404, message='Category not exist.')
        else:
            categories = Category.query.all()
            return {
                'total': len(categories),
                'data': [v.to_dict() for v in categories]
            }

    def post(self):
        Parser = reqparse.RequestParser()
        Parser.add_argument('name', type=str, required=True)
        args = Parser.parse_args()
        name = args.get('name')
        if Category.query.filter_by(name=name).first():
            abort(400, message="Category already exist.")
        else:
            category = Category(name=name)
            category.save()
            return {'success': True}, 201
