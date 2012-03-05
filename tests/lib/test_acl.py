# $File: test_acl.py
# $Date: Mon Mar 05 22:27:16 2012 +0800
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
"""tests for :mod:`pynojo.lib.acl`"""

import unittest

from tests.model._base import Base


class UgrpACLUnitTests(Base):

    def setUp(self):
        from pynojo.model.acl import ACLMdl 
        ses = self.session_maker()

        self.acl_id = int(ses.query(ACLMdl)
                .filter(ACLMdl.type == 'UgrpACL').one().id)

    def mkreq(self, username):
        from pynojo import Request
        from pynojo.lib.user import check_login_pw

        req = Request.blank('/')
        req.set_cookie = lambda *args, **kargs: None
        check_login_pw(req, username, '')
        return req

    def test_ugrp_acl(self):
        from pynojo.lib.acl import check

        self.assertTrue(check(self.mkreq('user1'), self.acl_id))
        self.assertFalse(check(self.mkreq('user2'), self.acl_id))

