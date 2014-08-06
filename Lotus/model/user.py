# -*- coding: utf-8 -*-
from Lotus.app import db


class User(db.Model):
    userid = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(16), unique=True)
    avatar = db.Column(db.String(64))
    description = db.Column(db.String(128))
    type = db.Column(db.String(16))
    email = db.Column(db.String(32), unique=True)
    psw = db.Column(db.String(32))
    '''
    constant
    '''
    CONST_TYPE_USER = 'user'
    CONST_TYPE_ADMIN = 'admin'
    CONST_DEFAULT_PASSWORD = '12345678'

    def __init__(self):
        self.userid = None
        self.nickname = None
        self.username = None
        self.avatar = None
        self.description = None
        self.type = None

    def __repr__(self):
        return '<User %r>' % self.username



