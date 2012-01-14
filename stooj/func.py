# $File: func.py
# $Date: Sun Jan 15 01:45:33 2012 +0800
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



# list(kargs:dict)
_route_list = list()    
_view_list = list()     
_subscriber_list = list()

def setup_pyramid(conf):
    """Setup pyramid route, views and subscribers.
    
    Keyword arguments:
        conf: an instance of pyramid.conf.Configurator to be configured
    """

    global _route_list, _view_list
    for i in _route_list:
        conf.add_route(**i)
    global _view_list
    for i in _view_list:
        conf.add_view(**i)
    for i in _subscriber_list:
        conf.add_subscriber(**i)



_route_cnt = 0
def view_config(**kargs):
    """view_config for stooj, similar to pyramid.view.view_config, but there are two differences:

    1. keyword argument ``route`` must be supplied, which is the route pattern
    2. there are two forms of the view callable:
        func(_, request) or func(_, context, request),
        where _ is the function for l10n translation"""

    def f(func):
        global _route_list, _view_list, _route_cnt
        from config import config
        name = str(_route_cnt)
        _route_cnt += 1
        _route_list.append({'name': name, 'pattern': config.PREFIX + kargs['route']})
        del kargs['route']

        def newfunc(context, request):
            from i18n import translators    # XXX
            if func.func_code.co_argcount == 2:
                return func(translators, request)
            return func(translators, context, request)

        kargs['view'] = newfunc
        kargs['route_name'] = name
        try:
            kargs['renderer'] = 'stooj:view/template/' + kargs['renderer']
        except KeyError:
            pass
        _view_list.append(kargs)
        return newfunc

    return f


def subscriber(*iface):
    def f(func):
        global _subscriber_list
        for i in iface:
            _subscriber_list.append({'subscriber': func, 'iface': i})
        return func
    return f
