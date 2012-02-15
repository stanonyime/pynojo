# $File: navbar.py
# $Date: Wed Feb 15 22:58:09 2012 +0800
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

"""The content of the navigation bar. See the source of this file for details."""

class PageDesc:
    """describe a page that should appear in the navigation bar"""

    route_name = None
    _title = None

    def __init__(self, route_name, title):
        """
        :param title: a callable to generate the page title which is
                      displayed in the navigation bar.
        """
        self.route_name = route_name
        self._title = title

    @property
    def title(self):
        """the title of this page"""
        return self._title()



PAGES = [
    PageDesc('home', lambda: _('Home')),
    PageDesc('about', lambda: _('About')),
]

