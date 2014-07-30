# -*- coding: utf-8 -*-

from app import app
from config import default_config
from sqlalchemy import create_engine
from model import common

if __name__ == '__main__':
    app.config.from_object(default_config.DevelopmentConfig)
    HOST = app.config.get('HOST')
    PORT = app.config.get('PORT')
    DEBUG = app.config.get('DEBUG')
    app.run(host=HOST, port=PORT, debug=DEBUG)
#     print app.config['SQLALCHEMY_DATABASE_URI']
#     engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'], convert_unicode=True)
#     print engine.execute('select * from test').first()