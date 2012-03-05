# $File: test_user.py
# $Date: Mon Mar 05 22:18:44 2012 +0800
#
# Copyright (C) 2012 the pynojo development team <see AUTHORS file>
# 
# Contributors to this file:
#    Kai Jia	<jia.kai66@gmail.com>
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
from tests.model._base import Base

from pynojo.model import install_db
from pynojo.model.user import *
from pynojo.model.user.auth_pw import *

class UserUnitTests(Base):

    g0_id = None
    g1_id = None

    @classmethod
    def set_up_class(cls):
        grps = cls.session_maker().query(UserGrpMdl).all()
        cls.g0_id = int(grps[0].id)
        cls.g1_id = int(grps[1].id)

    def get_user(self):
        ses = self.session_maker()
        u = ses.query(UserMdl).filter(UserMdl.username == 'user0').one()
        return u

    def test_perms(self):
        u = self.get_user()
        self.assertEqual(u.perms, frozenset([1, 2, 3]))
        self.assertIsNotNone(u._gp_cache)
        self.assertIsNotNone(u._gp_cache_rst)

        def check_invalid_cache(u, perms):
            self.assertIsNone(u._gp_cache)
            self.assertIsNone(u._gp_cache_rst)
            self.assertEqual(u.perms, frozenset(perms))
            self.assertIsNotNone(u._gp_cache)
            self.assertIsNotNone(u._gp_cache_rst)

        g = u.groups[0]
        g.perms.add(9)
        check_invalid_cache(u, [1, 2, 3, 9])

        del u.groups[0]
        check_invalid_cache(u, [2, 3])

        u.groups.append(g)
        g.perms.remove(9)
        self.assertEqual(u.perms, frozenset([1, 2, 3]))
        del u, g

        self.session_maker().commit()
        u = self.get_user()
        self.assertIsNone(u._gp_cache_rst)
        self.assertIsNotNone(u._gp_cache)
        self.assertEqual(u.perms, frozenset([1, 2, 3]))

    def test_grp_ids(self):
        self.assertEqual(self.get_user().grp_ids,
                frozenset([self.g0_id, self.g1_id]))

    def test_auth_pw(self):
        u = self.get_user()
        u.auth_pw = UserAuthPWMdl('xx')
        self.assertTrue(u.auth_pw.check('xx'))
        self.assertFalse(u.auth_pw.check('xxx'))
        u.auth_pw.set('xxx')
        self.assertFalse(u.auth_pw.check('xx'))
        self.assertTrue(u.auth_pw.check('xxx'))

        ses = self.session_maker()
        u.auth_pw = None
        self.assertEqual(ses.query(UserAuthPWMdl).count(), 2)

    def test_auth_code(self):
        u = self.get_user()
        code = u.get_auth_code()
        self.assertEqual(code, u.get_auth_code())
        c1 = u.update_auth_code()
        self.assertNotEqual(code, c1)
        self.assertEqual(c1, u.get_auth_code())


