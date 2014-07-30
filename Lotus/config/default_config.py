# -*- coding: utf-8 -*-


class Config(object):
    DEBUG = False
    TESTING = False
    PORT = 8000
    HOST = u'127.0.0.1'
    SECRET_KEY = u'adfO823nlDjkfo283r'


class DevelopmentConfig(Config):
    DEBUG = True
    TESTING = True
    # mysql://username:password@server:port/db
    username = u'root'
    password = u''
    server = u'localhost'
    port = u'3306'
    db = u'forum'
    SQLALCHEMY_DATABASE_URI = u'mysql://{username}:{password}@{server}:{port}/{db}'.format(
        username=username, password=password, server=server, port=port, db=db)

