# $File: _ext_type.py
# $Date: Wed Feb 22 15:04:06 2012 +0800
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
"""Extra SQLAlchemy ORM types"""

__all__ = ['JSONEncodeDict']

import cjson

from sqlalchemy.types import TypeDecorator, String
from sqlalchemy.ext.mutable import Mutable

from pynojo.exc import PynojoRuntimeError

class JSONEncodeDict(TypeDecorator):
    """Represents an mutable python *dict* as a json-encoded string."""
    # pylint: disable=W0223

    impl = String

    def process_bind_param(self, value, dialect):
        if value is not None:
            value = cjson.encode(value)
            if len(value) > self.length:
                raise PynojoRuntimeError(_(
                        '{class_name}: encoded string too long',
                        class_name = self.__class__.__name__))

        return value

    def process_result_value(self, value, dialect):
        if value is not None:
            value = cjson.decode(value)
        return value



class _JSONEncodeDictMutabilize(Mutable, dict):

    @classmethod
    def coerce(cls, key, value):

        if not isinstance(value, _JSONEncodeDictMutabilize):
            if isinstance(value, dict):
                return _JSONEncodeDictMutabilize(value)

            return Mutable.coerce(key, value)
        else:
            return value

    def __setitem__(self, key, value):
        dict.__setitem__(self, key, value)
        self.changed()

    def __delitem__(self, key):
        dict.__delitem__(self, key)
        self.changed()


_JSONEncodeDictMutabilize.associate_with(JSONEncodeDict)

