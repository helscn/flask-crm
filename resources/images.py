#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from auth import login_required
from models import Image
from settings import Setting
from flask import g, request
from flask_restful import abort, Resource
from os import path, remove


class ApiImages(Resource):
    def get(self, id):
        image = Image.get(id)
        if image:
            return image.response()
        else:
            abort(404, error='File not exist.')

    @login_required
    def delete(self, id):
        image = Image.get(id)
        if image:
            try:
                remove(path.join(Setting.UPLOAD_FOLDER, image.save_name))
                image.delete()
            except:
                abort(404, error='File not exist.')
            return 'File deleted.', 204
        else:
            abort(404, error='Unknow file id.')

    @login_required
    def post(self):
        for name in request.files:
            file = request.files.get(name)
            filename = path.basename(file.filename)
            ext = path.splitext(filename)[1]
            mimetype = file.mimetype
            user_id = g.current_user.id
            attachment = Image(
                name=filename, ext=ext, mimetype=mimetype, user_id=user_id)
            attachment.save()
            file.save(path.join(Setting.UPLOAD_FOLDER, attachment.save_name))
        return {'success': True}, 201
