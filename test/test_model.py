# -*- coding: utf-8 -*-
import unittest

from test import db
from Lotus.model.user import User
from hashlib import md5


class TestModelUser(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_add(self):
        """
        register
        :return:
        """
        m = md5()
        u1 = User(username='jayin', email='tonjayin@gmail.com', description='cool man', psw='273942569')

        u2 = User(username='Mars', email='Mars@gmail.com', psw='273942569')

        admin1 = User(username='admin1', email='admin1@gmail.com', psw='273942569', type=User.CONST_TYPE_ADMIN)

        admin2 = User(username='admin2', email='admin2@gmail.com', description='cool man', psw='273942569',
                      type=User.CONST_TYPE_ADMIN)

        db.session.add(u1)
        db.session.add(u2)
        db.session.add(admin1)
        db.session.add(admin2)
        db.session.commit()

        print '---result---'
        users = User.query.all()
        print users
        print '------------'

    def test_insert(self):
        print 'insert'


if __name__ == '__main__':
    unittest.main()

