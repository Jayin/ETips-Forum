# -*- coding: utf-8 -*-
from Lotus.app import app
from flask import render_template


@app.route('/')
def index():
    return 'welcome'


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html')



