# $File: test_lib.py
# $Date: Tue Feb 07 11:29:20 2012 +0800
#
# This file is part of stooj
# 
# stooj is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# stooj is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with stooj.  If not, see <http://www.gnu.org/licenses/>.
#
import unittest

class LibUnitTests(unittest.TestCase):

    def test_stooj_assert(self):
        """test :func:`stooj.lib.stooj_assert`"""
        from stooj.lib import stooj_assert
        from stooj.exception import StoojInnerError
        stooj_assert(True)
        with self.assertRaises(StoojInnerError) as exc:
            stooj_assert(False)


    def test_enum(self):
        """test :mod:`stooj.lib.enum`"""
        from stooj.lib.enum import get_base
        from stooj.exception import StoojInnerError

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

        with self.assertRaises(StoojInnerError):
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

            with self.assertRaises(StoojInnerError):
                e0.VAL0 = 0
            with self.assertRaises(StoojInnerError):
                e0.vnew = 0

            self.assertEqual(e0.get_data(e0.DATA0), 'd0')

            self.assertEqual(e1.get_data(e1.DATA0), 'd0')
            self.assertEqual(e1.get_data(e1.DATA1), 'd1')

            with self.assertRaises(StoojInnerError):
                e0.get_data(e1.DATA1)

        check(Enum0, Enum1, Enum2)
        check(Enum0(), Enum1(), Enum2())


