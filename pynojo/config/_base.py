# $File: _base.py
# $Date: Mon Feb 06 14:41:53 2012 +0800
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

# pylint: disable=C0111

from pynojo.exception import StoojInnerError

_init_done = False
class ConfigBase(object):
    """configuration base class. If any attribute of an instance of this class
    is modified after :func:`set_init_finished` called,
    :exc:`pynojo.exception.StoojInnerError` whould be raised."""

    def __setattr__(self, name, value):
        if _init_done:
            raise StoojInnerError('attempt to change static configuration')
        object.__setattr__(self, name, value)

    def __repr__(self):
        return '<pynojo {0} object>' . format(self.__class__.__name__)

    __str__ = __repr__


def set_init_finished():
    """Call this function if configuration initialization finished, i.e.
    further modifications to config would cause an error."""
    global _init_done
    _init_done = True

