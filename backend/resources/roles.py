#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from auth import login_required
from models import Role
from flask_restful import abort, Resource, reqparse


class ApiRoles(Resource):

    # @login_required
    def get(self, id=None):
        if not id:
            roles = Role.query.all()
            return {
                'total': len(roles),
                'data': [v.to_dict() for v in roles]
            }
        role = Role.get(id)
        if role:
            return {'data': role.to_dict()}
        else:
            abort(404, error='Role not exist.')

    @login_required
    def delete(self, id):
        role = Role.get(id)
        if role:
            role.delete()
            return '', 204
        else:
            abort(404, error='Role not exist.')

    @login_required
    def post(self):
        roleParse = reqparse.RequestParser()
        roleParse.add_argument('name', type=str)
        args = roleParse.parse_args()
        role_name = args.get('name')
        if not role_name:
            abort(400, error='Need to provide rolename.')
        role = Role.query.filter_by(name=role_name).first()
        if role:
            abort(406, error='The rolename already exists.')
        role = Role(name=role_name)
        role.save()
        return {'success': True}, 201
