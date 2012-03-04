# $File: test_acl.py
# $Date: Sun Mar 04 19:12:46 2012 +0800
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
from pynojo.tests.model._base import Base

from pynojo.exc import PynojoRuntimeError
from pynojo.model.acl import *

class ACLUnitTests(Base):

    @classmethod
    def set_up_class(cls):
        ses = cls.session_maker()
        ses.query(ACLMdl).delete()

        a = [ACLMdl(type = str(i), data = str(i)) for i in range(3)]
        for i in a:
            ses.add(i)

        for i in range(2):
            a[i].dep.append(a[i + 1])

        ses.commit()

    def get_obj(self, num):
        ses = self.session_maker()
        return ses.query(ACLMdl).filter(ACLMdl.data == str(num)).one()

    def test_used_by(self):
        for i in range(1, 3):
            self.assertEqual(self.get_obj(i).used_by.one().data, str(i - 1))

    def test_circle_dep(self):
        a = self.get_obj(0)
        with self.assertRaises(PynojoRuntimeError):
            a.dep.append(a)
        b = self.get_obj(2)
        with self.assertRaises(PynojoRuntimeError):
            b.dep.append(a)

    def test_circle_used_by(self):
        a = self.get_obj(0)
        with self.assertRaises(PynojoRuntimeError):
            a.used_by.append(a)
        b = self.get_obj(2)
        with self.assertRaises(PynojoRuntimeError):
            a.used_by.append(b)
