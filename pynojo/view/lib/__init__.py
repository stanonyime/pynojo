# $File: __init__.py
# $Date: Sun Feb 19 19:09:53 2012 +0800
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
"""some helper functions for templates"""

from cgi import escape
from contextlib import contextmanager

class MakoBase(object):
    """base class for mako templates"""
    local_vars = None

    _w = None
    # write something to mako template

    def __init__(self, local_vars):
        self.local_vars = local_vars
        self._w = local_vars['context'].write

    @contextmanager
    def tag(self, name, attr = None):
        """A with-statement context for writing a tag to the mako context.
        Note that if *attr[k]* is *None*, then *k* will not be added to the
        attribute list of the tag."""
        self._tag_attr(name, attr)
        yield
        self._w('</' + name + '>')

    def stag(self, name, attr = None):
        """Write a self-closed tag (e.g <input />) to the mako context."""
        self._tag_attr(name, attr, close_ch = '/>')

    def _tag_attr(self, name, attr, open_ch = '<', close_ch = '>'):
        w = self._w
        w(open_ch + name)
        if attr is not None:
            for k, v in attr.iteritems():
                if v is not None:
                    w(' {0}="{1}"'.format(k, escape(str(v), True)))
        w(close_ch)

