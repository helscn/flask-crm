#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from main import db
from datetime import datetime


class BaseModel(db.Model):
    # 当前对象模型类为抽象类，只能被继承使用
    __abstract__ = True

    def save(self):
        # 保存当前对象
        db.session.add(self)
        db.session.commit()

    def delete(self):
        # 删除当前对象
        db.session.delete(self)
        db.session.commit()

    def to_dict(self):
        # 将当前对象转换输出为字典对象
        data = {c.name: getattr(self, c.name) for c in self.__table__.columns}
        for key, item in data.items():
            if type(item) is datetime:
                data[key] = item.strftime('%Y-%m-%d %H:%M:%S')
        return data
