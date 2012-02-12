# $File: __init__.py
# $Date: Sun Feb 12 23:27:57 2012 +0800
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

"""pynojo package. Use pynojo.get_app() to get the WSGI application."""

from pyramid.request import Request as OrigRequest
from pynojo.config import config as config

class Request(OrigRequest):
    """request factory class for pynojo. This class also includes two methods
    *_* and *_pl*, see :ref:`devnotes-nls` for details."""

    # pylint: disable=C0301
    charset = 'utf-8'
    """see http://docs.pylonsproject.org/projects/pyramid/en/1.3-branch/narr/webob.html#unicode ."""

    pynojo_cache = None
    """a *dict*, various cache related to this request. It is recommended to
    use the function object itself as the key. See the source of
    :func:`pynojo.nls.get_translator` for example."""

    def __init__(self, *args, **kargs):
        # pylint: disable=E1003
        self.pynojo_cache = dict()
        super(self.__class__, self).__init__(*args, **kargs)

    def set_cookie(self, key, value, max_age = None, **kargs):
        """A convenient function for setting cookies, with *path*, *secure* set
        properly.
        
        :param kargs: other arguments passed to
                      :meth:`pyramid.response.Response.set_cookie` to overwrite
                      the pynojo defaults. Note that it might be modified."""
        kargs.setdefault('path', config.PREFIX)
        kargs.setdefault('secure', config.USE_HTTPS)
        self.response.set_cookie(key, value, max_age, **kargs)

    def del_cookie(self, key):
        """Delete a cookie from the client."""
        from pynojo.lib import time
        self.set_cookie(key, '', 0, expires = time() - 3600)

def get_app():
    """Return the WSGI application for pynojo"""
    from pyramid.config import Configurator
    from pynojo.view import setup_pyramid_route
    from pynojo import nls

    nls.init(Request)
    conf = Configurator(request_factory = Request)
    conf.scan('pynojo')
    setup_pyramid_route(conf)
    
    return conf.make_wsgi_app()

