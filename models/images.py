#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from flask import send_from_directory
from settings import Setting
from urllib.parse import quote
from .base_model import db, BaseModel


class Image(BaseModel):
    __tablename__ = 'images'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(256), nullable=False)
    ext = db.Column(db.String(256), nullable=False)
    mimetype = db.Column(db.String(256))
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))

    @staticmethod
    def get(id):
        """根据文件ID返回文件对象"""
        if not id:
            return None
        return Image.query.filter_by(id=id).first()

    @property
    def save_name(self):
        return 'Img{id}{ext}'.format(id=self.id, ext=self.ext)

    def response(self):
        response = send_from_directory(
            Setting.UPLOAD_FOLDER, self.save_name)
        return response