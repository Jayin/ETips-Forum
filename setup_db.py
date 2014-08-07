# -*- coding: utf-8 -*-

from Lotus.application import db, app
from Lotus.config.default_config import DevelopmentConfig

app.config.from_object(DevelopmentConfig)

#see the url
print app.config['SQLALCHEMY_DATABASE_URI']

db.drop_all()
db.create_all()


print 'create tables finished'