# -*- coding: utf-8 -*-
from . import app


@app.route('/user/login', methods=['POST'])
def user_login():
    return "login"


@app.route('/user/register', methods=['POST'])
def user_register():
    return "register"

@app.route('/user/<int:userid>/avatar', methods=['GET', 'POST'])
def user_avatar(userid):
    pass


@app.route('/user/<int:userid>/profile', methods=['GET'])
def user_profile():
    pass


@app.route('/user/<int:userid>/issue/sends/page/<int:page>', methods=['GET'])
def user_issues_send(userid, page):
    pass


@app.route('/user/<int:userid>/issue/favours/page/<int:page>', methods=['GET'])
def user_issues_favour(userid, page):
    pass


@app.route('/user/<int:userid>/issue/favours/page/<int:page>', methods=['GET'])
def user_messages(userid,page):
    pass



