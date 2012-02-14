# $File: __init__.py
# $Date: Tue Feb 14 17:01:08 2012 +0800
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
_route_cnt = 0

def mkroute(**kargs):
    """Return a route name that can be passed to
    :meth:`pyramid.config.add_view`. :func:`setup_pyramid_route` should be
    called during initialization to add these routes to a config.
    
    :param kargs: keyword arguments to be passed to
                  :meth:`pyramid.config.add_route`.  Note that it might be
                  modified. If *name* not in *kargs*, a unique name will be
                  assigned. If *pattern* in *kargs*,
                  :attr:`config.ROUTE_PREFIX
                  <pynojo.config.all.AllConfig.ROUTE_PREFIX>` will be added to
                  it."""
    try:
        name = kargs['name']
    except KeyError:
        global _route_list, _route_cnt
        name = 'mkrt-' + str(_route_cnt)
        _route_cnt += 1
        kargs['name'] = name

    try:
        kargs['pattern'] += config.ROUTE_PREFIX
    except KeyError:
        pass
    _route_list.append(kargs)
    return name


def setup_pyramid_route(conf):
    """Setup pyramid routes used by :func:`mkroute`
    
    :param conf: the instance of :class:`pyramid.conf.Configurator` to be configured
    """

    global _route_list
    for i in _route_list:
        conf.add_route(**i)

