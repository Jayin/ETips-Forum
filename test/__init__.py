# -*- coding: utf-8 -*-

"""
test for Lotus
"""

# test for DevelopmentConfig
from Lotus.config.default_config import DevelopmentConfig

from Lotus.application import app, db

app.config.from_object(DevelopmentConfig)



