# -*- coding: utf-8 -*-
from Lotus.app import db
import hashlib


class User(db.Model):
    userid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(16), unique=True, nullable=False)
    avatar = db.Column(db.String(64))
    description = db.Column(db.String(128))
    type = db.Column(db.String(16), nullable=False, default='user')
    email = db.Column(db.String(32), unique=True, nullable=False)
    psw = db.Column(db.String(32), nullable=False)
    '''
    constant
    '''
    CONST_TYPE_USER = 'user'
    CONST_TYPE_ADMIN = 'admin'
    CONST_DEFAULT_PASSWORD = 'haha12345678'

    def __init__(self, **kwargs):
        """
        init a user(include 'user' and 'admin')

        :param userid: autoincrement ,mostly you should not to apply it
        :param username: username of the user
        :param avatar: the user's avatar
        :param description: the description of a user
        :param type: 'user'(default) or 'admin' see:User.CONST_TYPE_USER and  User.CONST_TYPE_ADMIN
        :param email: not be null
        :param psw: encrypt by hashlib.md5(),defalut User.CONST_DEFAULT_PASSWORD
        :return:
        """
        if 'email' in kwargs:
            self.email = kwargs.pop('email').lower()

        if 'psw' in kwargs:
            self.psw = hashlib.md5(kwargs.pop('psw')).hexdigest()
        else:
            self.psw = hashlib.md5(User.CONST_DEFAULT_PASSWORD).hexdigest()

        if 'type' in kwargs:
            self.type = kwargs.pop('type').lower()

        for k, v in kwargs.items():
            setattr(self, k, v)

    def __repr__(self):
        return '<User %r>' % self.username



