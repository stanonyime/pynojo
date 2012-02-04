# $File: __init__.py
# $Date: Sat Feb 04 21:42:23 2012 +0800
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

"""stooj package. Use stooj.get_app() to get the WSGI application."""

from pyramid.request import Request as OrigRequest
from stooj.config import config as config

class Request(OrigRequest):
    # pylint: disable=C0301
    """request factory class for stooj. This class also includes two methods
    *_* and *_pl*, see :ref:`devnotes-nls` for details."""

    charset = 'utf-8'
    """see http://docs.pylonsproject.org/projects/pyramid/en/1.3-branch/narr/webob.html#unicode ."""

    def set_cookie(self, key, value, max_age = None, **kargs):
        """A convenient function for setting cookies, with *path*, *domain* and
        other options set properly (see the source for details).
        
        :param kargs: other arguments passed to
                      :meth:`pyramid.response.Response.set_cookie` to overwrite
                      the stooj defaults."""
        self.response.set_cookie(key, value, max_age,
            kargs.get('path', config.PREFIX),
            kargs.get('domain', config.DOMAIN),
            kargs.get('secure', config.USE_HTTPS),
            kargs.get('httponly', False),
            kargs.get('comment', None),
            kargs.get('expires', None),
            kargs.get('overwrite', True))

    def del_cookie(self, key):
        """Delete a cookie from the client."""
        from stooj.lib import time
        self.set_cookie(key, '', 0, expires = time() - 3600)

def get_app():
    """get the WSGI application for stooj"""
    from pyramid.config import Configurator
    from stooj.view import setup_pyramid_route
    from stooj import nls

    nls.init(Request)
    conf = Configurator(request_factory = Request)
    conf.scan('stooj.view')
    setup_pyramid_route(conf)
    
    return conf.make_wsgi_app()

