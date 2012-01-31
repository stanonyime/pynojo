# $File: __init__.py
# $Date: Tue Jan 31 23:43:49 2012 +0800
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

def get_app():
    """get the WSGI application for stooj"""
    from pyramid.request import Request as OrigRequest
    from pyramid.config import Configurator
    from stooj.lib import setup_pyramid_route
    from stooj import nls

    class _Request(OrigRequest):
        pass

    nls.init(_Request)
    config = Configurator(request_factory = _Request)
    config.scan('stooj.view')
    setup_pyramid_route(config)
    
    return config.make_wsgi_app()

