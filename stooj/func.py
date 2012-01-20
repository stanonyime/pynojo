# $File: func.py
# $Date: Fri Jan 20 10:25:52 2012 +0800
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
"""common functions used by stooj"""

class Const(object):
    """A class implementing constants in Python.
    The attributes of classes derived from this class
    could only be set once, otherwise ConstError would be raised"""

    class ConstError(TypeError):
        """exception raised when tring to modify constants"""
        pass

    def __setattr__(self, name, value):
        try:
            object.__getattribute__(self, name)
            raise self.ConstError('can not rebind const {name}' . format(name = name))
        except AttributeError:
            object.__setattr__(self, name, value)



_route_list = list()    # list(kargs:dict)
_route_cnt = 0

def mkroute(**kargs):
    """Return a route name that can be passed to pyramid.config.add_view, 
    and setup_pyramid_route should be called to add these routes to a config
    
    Keyword argument:
        kargs: keyword arguments passed to add_route. Note that it might be changed"""
    global _route_list, _route_cnt
    name = 'mkrt-' + str(_route_cnt)
    _route_cnt += 1
    kargs['name'] = name
    _route_list.append(kargs)
    return name


def setup_pyramid_route(conf):
    """Setup pyramid routes used by mkroute
    
    Keyword argument:
        conf: an instance of pyramid.conf.Configurator to be configured
    """

    global _route_list
    for i in _route_list:
        conf.add_route(**i)


