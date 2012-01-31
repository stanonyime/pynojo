# $File: __init__.py
# $Date: Wed Feb 01 00:19:19 2012 +0800
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
"""stooj static configurations. See the sources for details."""

# pylint: disable=C0103,W0212

from stooj.lib import Const

config = Const()
from stooj.config import sys
sys._set_config(config)

config.user = Const()
from stooj.config import user
user._set_config(config.user)
