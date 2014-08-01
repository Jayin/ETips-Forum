# -*- coding: utf-8 -*-
from Lotus.app import db

class User(db.Model):
    userid = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(16), unique=True)
    username = db.Column(db.String(16), unique=True)
    avatar = db.Column(db.String(64), unique=True)
    description = db.Column(db.String(128), unique=True)
    type = db.Column(db.String(16))

    def __init__(self):
        self.userid = None
        self.nickname = None
        self.username = None
        self.avatar = None
        self.description = None
        self.type = None



