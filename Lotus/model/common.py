# -*- coding: utf-8 -*-
from Lotus.app import app


@app.route('/')
def index():
    return 'welcome'
