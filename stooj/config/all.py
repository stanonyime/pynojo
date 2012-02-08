# $File: all.py
# $Date: Sun Feb 05 13:52:42 2012 +0800
#
# Copyright (C) 2012 the stooj development team <see AUTHORS file>
# 
# Contributors to this file:
#    Kai Jia <jia.kai66@gmail.com>
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

# pylint: disable=C0111

from stooj.config._base import ConfigBase
from stooj.config import user, pkg

class AllConfig(ConfigBase):
    """configuration of stooj"""
    PREFIX = '/'
    """prefix of stooj in the domain, which must begin and end with a slash"""

    ROUTE_PREFIX = PREFIX
    """prefix to be added to all the routes (see :func:`stooj.view.mkroute`)"""

    USE_HTTPS = False
    """whether HTTPS is enabled (affect the behaviour of some functions, such
    as :meth:`stooj.__init__.Request.set_cookie`)"""

    user = user.UserConfig()
    """user configuration. See :class:`stooj.config.user.UserConfig`."""

    pkg = pkg.PkgInfo()
    """package information. See :class:`stooj.config.pkg.PkgInfo`."""

