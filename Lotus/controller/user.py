# -*- coding: utf-8 -*-
from . import app, db
from flask import request
from Lotus.model.user import User


@app.route('/user/login', methods=['POST'])
def user_login():
    return "login"


@app.route('/user/register', methods=['POST'])
def user_register():
    # todo 有插入异常怎么办？
    #todo 忘记密码..
    u = User()
    u.username = request.form.get('username', None)
    u.description = request.form.get('description', None)
    u.type = request.form.get('type', User.CONST_TYPE_USER)
    u.email = request.form.get('email', None)
    db.session.add(u)
    db.session.commit()
    return "register is ok"


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
def user_messages(userid, page):
    pass



