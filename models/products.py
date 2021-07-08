#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from os import path, remove
from settings import Setting
from flask import url_for
from datetime import datetime
from .base_model import db, BaseModel
from PIL import Image


class Product(BaseModel):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    no = db.Column(db.String(20), unique=True, nullable=False)
    name = db.Column(db.String(256), nullable=False)
    spec = db.Column(db.String(256), nullable=False, default='')
    description = db.Column(db.Text, nullable=False, default='')
    moq = db.Column(db.Integer, nullable=False, default=1)
    purchase_price = db.Column(db.Float, nullable=False, default=0.00)
    profit_rate = db.Column(db.Float, nullable=False, default=0.00)
    comment = db.Column(db.Text, nullable=False, default='')
    created_date = db.Column(
        db.DateTime, nullable=False, default=datetime.now())
    valid = db.Column(db.Boolean, nullable=False, default=True)
    category_id = db.Column(db.Integer, db.ForeignKey('product_categories.id'))
    thumbnail = db.Column(db.String(256))
    supplier_id = db.Column(db.Integer, db.ForeignKey('suppliers.id'))
    labels = db.relationship(
        'Label', backref='product', lazy='dynamic', cascade='all')
    images = db.relationship(
        'Image', backref='product', lazy='dynamic', cascade='all')

    @staticmethod
    def get(id):
        """根据ID返回对象"""
        if not id:
            return None
        return Product.query.filter_by(id=id).first()

    def set_thumbnail(self, file):
        save_name = None
        mimetype = file.mimetype
        if 'image' in mimetype:
            filename = path.basename(file.filename)
            ext = path.splitext(filename)[1]
            save_name = 'thumb_{id}{ext}'.format(id=self.id, ext=ext)
            save_path = path.join(Setting.UPLOAD_FOLDER, save_name)

            img = Image.open(file)
            w, h = img.size
            while w > 400 or h > 300:
                w = w/2
                h = h/2
            img.resize((int(w), int(h)))
            img.save(save_path)
            self.thumbnail = save_name
            self.save()
        return save_name

    def to_dict(self):
        # 将当前对象转换输出为字典对象
        data = {c.name: getattr(self, c.name) for c in self.__table__.columns}
        if data['thumbnail']:
            data['thumbnail'] = url_for(
                'get_uploads', filename=data['thumbnail'])
        if data['created_date']:
            data['created_date'] = data['created_date'].strftime(
                '%Y-%m-%d %H:%M:%S')
        return data

    def delete(self):
        try:
            for label in self.labes.all():
                db.session.delete(label)
            for image in self.images.all():
                db.session.delete(image)
            if self.thumbnail:
                remove(path.join(Setting.UPLOAD_FOLDER, self.thumbnail))
            db.session.delete(self)
            db.session.commit()
        except:
            db.session.rollback()
