#!/usr/bin/python3
# -*- coding: utf-8 -*-

from .base_model import db, BaseModel

from werkzeug.security import check_password_hash
from werkzeug.security import generate_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer
from settings import Setting


class User(BaseModel):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    nickname = db.Column(db.String(20), nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey(
        'roles.id'), nullable=False, default=2)

    def __init__(self, username, nickname, password, id=None, role_id=None):
        super().__init__()
        self.username = username
        self.nickname = nickname
        self.password_hash = generate_password_hash(password)
        if id:
            self.id = id
        if role_id:
            self.role_id = role_id

    def __repr__(self):
        return '<User:{}>'.format(self.username)

    @staticmethod
    def get(user_id):
        """根据用户ID返回用户对象，为 login_user 方法提供支持"""
        if not user_id:
            return None
        return User.query.filter(User.id == user_id).first()

    @property
    def password(self):
        raise AttributeError('Password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def generate_token(self):
        """返回当前User对象的验证token"""
        s = TimedJSONWebSignatureSerializer(
            Setting.SECRET_KEY, expires_in=Setting.TOKEN_EXPIRATION)
        return s.dumps({'id': self.id}).decode('utf-8')

    def generate_response(self):
        response = self.to_dict()
        response['token'] = self.generate_token()
        response['role_name'] = self.role.name
        return response

    @staticmethod
    def verify_token(token):
        """验证 token 是否有效,验证通过时返回User对象"""
        s = TimedJSONWebSignatureSerializer(Setting.SECRET_KEY)
        try:
            data = s.loads(token)
        except:
            return None
        return User.query.get(data['id'])

    def to_dict(self):
        columns = list(
            filter(lambda c: ('password' not in c.name), self.__table__.columns))
        return {c.name: getattr(self, c.name) for c in columns}
