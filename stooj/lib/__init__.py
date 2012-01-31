# $File: __init__.py
# $Date: Tue Jan 31 23:37:59 2012 +0800
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
"""miscellaneous convenience classes and functions"""

from stooj.exception import StoojInnerError

class Const(object):
    """A class implementing constants in Python.
    The attributes of classes derived from this class
    could only be set once, otherwise ConstError would be raised"""

    class ConstError(StoojInnerError):
        """exception raised when tring to modify constants"""
        pass

    def __setattr__(self, name, value):
        try:
            object.__getattribute__(self, name)
            raise self.ConstError('can not rebind const {name}' .
                    format(name = name))
        except AttributeError:
            object.__setattr__(self, name, value)



_route_list = list()    # list(kargs:dict)
_route_cnt = 0

def mkroute(**kargs):
    """Return a route name that can be passed to *pyramid.config.add_view*.
    :func:`setup_pyramid_route` should be called to add these routes to a config
    
    :param kargs: keyword arguments to be passed to *pyramid.config.add_route*.
        Note that it might be modified.  """
    global _route_list, _route_cnt
    name = 'mkrt-' + str(_route_cnt)
    _route_cnt += 1
    kargs['name'] = name
    _route_list.append(kargs)
    return name


def setup_pyramid_route(conf):
    """Setup pyramid routes used by :func:`mkroute`
    
    :param conf: the instance of *pyramid.conf.Configurator* to be configured
    """

    global _route_list
    for i in _route_list:
        conf.add_route(**i)


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
    exc_msg = u"Assertion failed."
    if msg is not None:
        exc_msg += " Additional message: " + msg
    raise StoojInnerError(exc_msg + '\nTraceback (most recent call last):\n' +\
            '' . join(format_list(extract_stack()[:-1])))

