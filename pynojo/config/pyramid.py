# $File: pyramid.py
# $Date: Tue Feb 14 18:43:37 2012 +0800
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

class PyramidConfig(ConfigBase):
    """pyramid configuration settings"""

    INCLUDES = []
    """additional pyramid.includes"""

    SETTINGS = {
        'mako.strict_undefined': True,
        'mako.default_filters': [],
        'mako.imports': 'from pynojo.config import config',
        'mako.directories': ['pynojo.view:template'],
        'pyramid.includes': INCLUDES
    }
    """additional settings passed to :class:`pyramid.config.Configurator`."""

