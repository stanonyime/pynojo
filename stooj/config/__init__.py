# $File: __init__.py
# $Date: Fri Feb 03 11:10:00 2012 +0800
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
"""This package provides stooj static configurations. To access the config,
import *config* from *stooj.config*. See also :ref:`devnotes-sysconf`."""

from stooj.config._base import set_init_finished
from stooj.config.all import AllConfig

config = AllConfig()

set_init_finished()


