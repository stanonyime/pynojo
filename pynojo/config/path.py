# $File: path.py
# $Date: Tue Feb 14 20:09:27 2012 +0800
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

# pylint: disable=C0111
from pynojo.config._base import ConfigBase

class PathConfig(ConfigBase):
    """Configuration for various paths. All the paths should begin and end with
    a slash, unless """

    COOKIE_PATH = '/'
    """*path* value of the cookies"""

    ROUTE_PREFIX = '/'
    """prefix to be added to all the routes, see also
    :func:`pynojo.view.mkroute`"""

    STATIC_PREFIX = ROUTE_PREFIX + 'static/'
    """prefix of static assets, see also
    :meth:`pynojo.__init__.Request.static_path`"""

    STATIC_NAME = STATIC_PREFIX
    """*name* argument passed to
    :meth:`pyramid.config.Configurator.add_static_view`; static view will not
    be added if this attribute is *None*."""
