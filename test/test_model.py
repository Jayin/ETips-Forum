# -*- coding: utf-8 -*-
import unittest

from test import db
from Lotus.model.user import User


class TestModelUser(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_add(self):
        u1 = User()
        u1.userid = 1
        u1.username = 'jayin'
        u1.email = 'tonjayin@gmail.com'
        u1.type = 'user'
        u1.description = "cool man"

        u2 = User()
        u2.userid = 2
        u2.username = 'Mars'
        u2.email = 'Mars@gmail.com'
        u2.type = 'user'
        # u2.description ="cool man"

        db.session.add(u1)
        db.session.add(u2)
        db.session.commit()

        print '---result---'
        users = User.query.all()
        print users
        print '------------'


    def test_insert(self):
        print 'insert'


if __name__ == '__main__':
    unittest.main()

