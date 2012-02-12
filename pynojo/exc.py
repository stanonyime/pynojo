# $File: exc.py
# $Date: Sun Feb 12 14:40:55 2012 +0800
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
"""pynojo exception classes"""

class PynojoError(Exception):
    """Base class for pynojo exceptions."""
    pass

class PynojoInternalError(PynojoError):
    """Internal errors, usually caused by careless development.
    If this exception is caught, a page containing error message
    and bug reporting information should be presented to the user."""
    pass

class PynojoRuntimeError(PynojoError):
    """Runtime errors, usually caused by incorrect user operations."""
    pass

