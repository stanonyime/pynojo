# $File: __init__.py
# $Date: Fri Feb 03 23:04:43 2012 +0800
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
"""miscellaneous convenience functions"""

def gen_random_binary(length):
    """Return a random string containing *len* bytes,
    which may include non-ASCII characters"""
    # pylint: disable=W0612
    from random import randint
    return ''.join([chr(randint(1, 255)) for i in range(length)])


def stooj_assert(val, msg = None):
    """Raise :exc:`stooj.exception.StoojInnerError` if *val* evaluates to false.

    :param msg: additional message to be added to the exception
    :type msg: str or None
    """

    if val:
        return False
    from traceback import extract_stack, format_list
    from stooj.exception import StoojInnerError
    exc_msg = u"Assertion failed."
    if msg is not None:
        exc_msg += " Additional message: " + msg
    raise StoojInnerError(exc_msg + '\nTraceback (most recent call last):\n' +\
            '' . join(format_list(extract_stack()[:-1])))


def time():
    """Return the time as an integer number expressed in seconds since the
    epoch, in UTC"""
    from time import time as t
    return int(t())

