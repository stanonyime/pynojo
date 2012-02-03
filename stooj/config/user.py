# $File: user.py
# $Date: Fri Feb 03 10:58:00 2012 +0800
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

class UserConfig(ConfigBase):
    """configuration for user maintenance"""

    USERNAME_LEN_MAX = 20
    """maximal length of username"""

    DISPNAME_LEN_MAX = 20
    """maximal length of display name"""

    GRPNAME_LEN_MAX = 20
    """maximal length of user group name"""

