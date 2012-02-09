# $File: all.py
# $Date: Thu Feb 09 20:09:13 2012 +0800
#
# Copyright (C) 2012 the pynojo development team <see AUTHORS file>
# 
# Contributors to this file:
#    Kai Jia <jia.kai66@gmail.com>
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
from pynojo.config import user, pkg

class AllConfig(ConfigBase):
    """configuration of pynojo"""
    PREFIX = '/'
    """prefix of pynojo in the domain, which must begin and end with a slash"""

    ROUTE_PREFIX = PREFIX
    """prefix to be added to all the routes (see :func:`pynojo.view.mkroute`)"""

    USE_HTTPS = False
    """whether HTTPS is enabled (affect the behavior of some functions, such
    as :meth:`pynojo.__init__.Request.set_cookie`)"""

    user = user.UserConfig()
    """user configuration. See :class:`pynojo.config.user.UserConfig`."""

    pkg = pkg.PkgInfo()
    """package information. See :class:`pynojo.config.pkg.PkgInfo`."""

