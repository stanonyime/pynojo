# $File: ugrp.py
# $Date: Mon Mar 05 22:30:34 2012 +0800
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

from pynojo.lib.acl._base import Base

class UgrpACL(Base):
    """An ACL which only allows certain user groups."""

    grp_id = None
    """the set of user group ids that should be allowed"""

    def __init__(self, grp_id):
        self.grp_id = set(grp_id)
        super(UgrpACL, self).__init__()

    @classmethod
    def from_model(cls, model):
        return UgrpACL(model.data)

    def save_to_model(self, model):
        model.type = self.__class__.__name__
        model.data = set(self.grp_id)

    def check(self, request):
        from pynojo.lib.user import get_model
        u = get_model(request)
        return (u is not None) and (u.grp_ids & self.grp_id)

