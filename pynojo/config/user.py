# $File: user.py
# $Date: Fri Feb 17 13:04:13 2012 +0800
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

class UserConfig(ConfigBase):
    """configuration for user maintenance"""

    USERNAME_LEN_MIN = 3
    """minimum length of username"""

    USERNAME_LEN_MAX = 20
    """maximum length of username"""

    DISPNAME_LEN_MAX = 20
    """maximum length of display name"""

    GRPNAME_LEN_MAX = 20
    """maximum length of user group name"""

    ALLOW_REGISTER = True
    """whether to allow new users to register"""

    RESERVED_USERNAME = frozenset(['admin', 'administrator', 'root', 'r00t'])
    """the set of reserved usernames that could not be registered"""

