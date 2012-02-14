# $File: __init__.py
# $Date: Tue Feb 14 21:57:50 2012 +0800
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
"""
This module define the views for pynojo. When initializing the application,
:meth:`pyramid.config.Configurator.scan` should be called on this module.

The following globals will be added to Chameleon templates:
    * *_*: normal translation function (see
      :meth:`pynojo.nls.Translator.get_translation`)
    * *_pl*: plural translation function (see
      :meth:`pynojo.nls.Translator.get_plural_translation`)
"""

from pyramid.events import subscriber, BeforeRender, NewRequest

from pynojo.lib import register_thread_request
from pynojo.config import config

@subscriber(BeforeRender)
def _add_global(event):
    # pylint: disable=W0212
    req = event['request']
    event['_'] = req._
    event['_pl'] = req._pl


@subscriber(NewRequest)
def _new_request(event):
    register_thread_request(event.request)



_route_list = list()    # list(kargs:dict)

def mkroute(**kargs):
    """Return a route name that can be passed to
    :meth:`pyramid.config.add_view`. :func:`setup_pyramid_conf` should be
    called during initialization to add these routes to a config.
    
    :param kargs: keyword arguments to be passed to
                  :meth:`pyramid.config.add_route`.  Note that it might be
                  modified. If *name* not in *kargs*, a unique name will be
                  assigned. If *pattern* in *kargs*,
                  :attr:`config.path.ROUTE_PREFIX
                  <pynojo.config.path.PathConfig.ROUTE_PREFIX>` will be added to
                  it."""
    name = kargs.get('name')
    if name is None:
        global _route_list
        name = 'mkrt-' + str(len(_route_list))
        kargs['name'] = name

    pattern = kargs.get('pattern')
    if pattern is not None:
        kargs['pattern'] = config.path.ROUTE_PREFIX + pattern
    _route_list.append(kargs)
    return name


def _cjson_renderer_factory(info):
    import cjson
    def _render(value, system):
        request = system.get('request')
        if request is not None:
            response = request.response
            ct = response.content_type
            if ct == response.default_content_type:
                response.content_type = 'application/json'
        return cjson.encode(value)
    return _render



def setup_pyramid_conf(conf):
    """Setup pyramid configuration *conf*"""
    global _route_list
    for i in _route_list:
        conf.add_route(**i)

    conf.add_renderer('cjson', _cjson_renderer_factory)

