# $File: _base.py
# $Date: Sun Mar 04 19:31:27 2012 +0800
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
"""ACL base"""

class Base(object):
    """The base class for ACL. All ACL implementations should be derived from
    this class. The name of derived class should be unique among all the
    subclasses, and should not exceed :attr:`TYPE_MAX_LEN
    <pynojo.model.acl.ACLMdl.TYPE_MAX_LEN>` characters."""

    @classmethod
    def from_model(cls, model):
        """A factory method for making an instance of this ACL based on the
        data provided by *model*, which is an :class:`ACLMdl
        <pynojo.model.acl.ACLMdl>` instance."""
        raise NotImplementedError()

