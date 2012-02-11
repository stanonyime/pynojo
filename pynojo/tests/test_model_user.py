# $File: test_model_user.py
# $Date: Sat Feb 11 21:14:22 2012 +0800
#
# Copyright (C) 2012 the pynojo development team <see AUTHORS file>
# 
# Contributors to this file:
#    Kai Jia <jia.kai66@gmail.com>
#
# This file is part of pynojo
# 
# pynojo is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# pynojo is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with pynojo.  If not, see <http://www.gnu.org/licenses/>.
#
import unittest

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from pynojo.model import install_db
from pynojo.model.user import *
from pynojo.model.user_auth_pw import *

class UserUnitTests(unittest.TestCase):

    def setUp(self):
        engine = create_engine('sqlite:///:memory:')
        event.listen(engine, 'connect', lambda con, record:
                con.execute('PRAGMA foreign_keys=ON'))
        self.Session = sessionmaker(bind = engine)
        install_db(engine)

        ses = self.Session()
        self.ses = ses

        g0 = UserGrp(name = 'g0')
        g1 = UserGrp(name = 'g1')
        u0 = User(username = 'u0')

        u0.groups.append(g0)
        u0.groups.append(g1)
        g0.perms.update([1, 2])
        g1.perms.update([2, 3])

        ses.add(u0)
        ses.commit()

    def get_user(self):
        ses = self.ses
        u = ses.query(User).filter(User.username == 'u0').one()
        return u

    def test_user_perms(self):
        u = self.get_user()
        self.assertEqual(u.perms, frozenset([1, 2, 3]))
        self.assertIsNotNone(u._perms_cache)
        self.assertIsNotNone(u._perms_cache_rst)

        u.groups[0].perms.add(9)
        self.check_invalid_cache([1, 2, 3, 9])

        del u.groups[0]
        self.check_invalid_cache([2, 3])

    def check_invalid_cache(self, perms):
        u = self.get_user()
        self.assertIsNone(u._perms_cache)
        self.assertIsNone(u._perms_cache_rst)
        self.assertEqual(u.perms, frozenset(perms))
        self.assertIsNotNone(u._perms_cache)
        self.assertIsNotNone(u._perms_cache_rst)

    def test_user_auth_pw(self):
        u = self.get_user()
        u.auth_pw = UserAuthPW('xx')
        self.assertTrue(u.auth_pw.check('xx'))
        self.assertFalse(u.auth_pw.check('xxx'))
        u.auth_pw.set('xxx')
        self.assertFalse(u.auth_pw.check('xx'))
        self.assertTrue(u.auth_pw.check('xxx'))

    def test_user_auth_code(self):
        u = self.get_user()
        code = u.get_auth_code()
        self.assertEqual(code, u.get_auth_code())
        c1 = u.update_auth_code()
        self.assertNotEqual(code, c1)
        self.assertEqual(c1, u.get_auth_code())


