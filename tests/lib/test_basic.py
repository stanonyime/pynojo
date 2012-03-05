# $File: test_basic.py
# $Date: Mon Mar 05 20:08:37 2012 +0800
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
"""Test basic functions of :mod:`pynojo.lib`."""
import unittest

class LibUnitTests(unittest.TestCase):

    def test_pynojo_assert(self):
        """test :func:`pynojo.lib.pynojo_assert`"""
        from pynojo.lib import pynojo_assert
        from pynojo.exc import PynojoInternalError
        pynojo_assert(True)
        with self.assertRaises(PynojoInternalError) as exc:
            pynojo_assert(False)


    def test_enum(self):
        """test :mod:`pynojo.lib.enum`"""
        from pynojo.lib.enum import get_base
        from pynojo.exc import PynojoInternalError

        Base = get_base(start = 42, step = 8)

        class Enum0(Base):
            VAL0 = Base.enum
            VAL1 = Base.enum
            VAL2 = 'str'
            DATA0 = Base.enum('d0')

        class Enum1(Enum0):
            VAL3 = Base.enum
            DATA1 = Base.enum('d1')

        class Enum2(Base):
            VAL4 = Base.enum

        with self.assertRaises(PynojoInternalError):
            class MultipleBase(Enum1, Enum2):
                pass

        def check(e0, e1, e2):
            self.assertEqual(e0.VAL0, 42)
            self.assertEqual(e0.VAL1, 50)
            self.assertEqual(e0.VAL2, 'str')
            self.assertEqual(e0.DATA0, 58)

            self.assertEqual(e1.VAL3, 66)
            self.assertEqual(e1.DATA1, 74)

            self.assertEqual(e2.VAL4, 42)

            with self.assertRaises(PynojoInternalError):
                e0.VAL0 = 0
            with self.assertRaises(PynojoInternalError):
                e0.vnew = 0

            self.assertEqual(e0.get_data(e0.DATA0), 'd0')

            self.assertEqual(e1.get_data(e1.DATA0), 'd0')
            self.assertEqual(e1.get_data(e1.DATA1), 'd1')

            with self.assertRaises(PynojoInternalError):
                e0.get_data(e1.DATA1)

        check(Enum0, Enum1, Enum2)
        check(Enum0(), Enum1(), Enum2())


