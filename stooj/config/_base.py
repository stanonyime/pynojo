# $File: _base.py
# $Date: Fri Feb 03 11:16:50 2012 +0800
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

# pylint: disable=C0111

from stooj.exception import StoojInnerError

_init_done = False
class ConfigBase(object):
    """configuration base class. If any attribute of an instance of this class
    is modified after :func:`set_init_finished` called,
    :exc:`stooj.exception.StoojInnerError` whould be raised."""

    def __setattr__(self, name, value):
        if _init_done:
            raise StoojInnerError('attempt to change static configuration')
        object.__setattr__(self, name, value)

    def __repr__(self):
        return 'stooj {0} object' . format(self.__class__.__name__)

    def __str__(self):
        return repr(self)


def set_init_finished():
    """Call this function if configuration initialization finished, i.e.
    further modifications to config would cause an error."""
    global _init_done
    _init_done = True

