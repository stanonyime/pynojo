# $File: __init__.py
# $Date: Sun Jan 15 01:44:12 2012 +0800
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

from pyramid.config import Configurator
from func import setup_pyramid
from view import index

def get_app():
    """get the WSGI application for stooj"""
    config = Configurator()
    setup_pyramid(config)
    
    return config.make_wsgi_app()

