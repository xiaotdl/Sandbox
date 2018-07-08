# -*- coding: utf-8 -*-
from app import db
from datetime import datetime


class User(db.Model): # 用户
    id = db.Column(db.Integer, primary_key=True) # ID
    username = db.Column(db.String(128), index=True, unique=True) # 用户名
    password = db.Column(db.String(128)) # 密码
    name = db.Column(db.String(64)) # 姓名
    id_card_num = db.Column(db.String(128)) # 身份证
    created_at = db.Column(db.DateTime, default=datetime.utcnow) # 注册日期

    # tasks = db.relationship('Task', backref='user', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.name)

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'password': self.password,
            'name': self.name,
            'id-card-num': self.id_card_num,
            'created-at': self.created_at
        }


class Product(db.Model): # 商品
    id = db.Column(db.Integer, primary_key=True) # ID
    name = db.Column(db.String(64), index=True, unique=True) # 名称
    tag = db.Column(db.String(128)) # 标签
    code = db.Column(db.String(128), index=True, unique=True) # 商品码
    created_at = db.Column(db.DateTime, default=datetime.utcnow) # 生产日期
    batch = db.Column(db.Integer) # 批次
    spec = db.Column(db.String(128)) # 规格

    def __repr__(self):
        return '<Product {}>'.format(self.name)

    def to_dict(self):
        return {
            'id': self.id,
            'tag': self.tag,
            'name': self.name,
            'code': self.code,
            'created-at': self.created_at,
            'batch': self.batch,
            'spec': self.spec
        }


class Factory(db.Model): # 厂家
    id = db.Column(db.Integer, primary_key=True) # ID
    name = db.Column(db.String(64), index=True, unique=True) # 名称
    code = db.Column(db.String(128), index=True, unique=True) # 代码
    address = db.Column(db.String(256)) # 地址

    def __repr__(self):
        return '<Factory {}>'.format(self.name)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'code': self.code,
            'address': self.address
        }
