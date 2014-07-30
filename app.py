#!/usr/bin/env python
# coding=utf-8
__author__ = 'Jayin Ton'

from flask import Flask
from config import default_config
from sqlalchemy import create_engine

app = Flask(__name__)


@app.route('/')
def index():
    return 'welcome'


if __name__ == '__main__':
    app.config.from_object(default_config.DevelopmentConfig)
    HOST = app.config.get('HOST')
    PORT = app.config.get('PORT')
    DEBUG = app.config.get('DEBUG')
    # app.run(host=HOST, port=PORT, debug=DEBUG)
    print app.config['SQLALCHEMY_DATABASE_URI']
    # engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'], convert_unicode=True)
    # print engine.execute('select * from test').first()