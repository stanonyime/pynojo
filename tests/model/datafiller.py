# $File: datafiller.py
# $Date: Mon Mar 05 22:24:11 2012 +0800
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
"""functions for filling the database"""

from pynojo.model.user import *
from pynojo.model.user.auth_pw import *
from pynojo.model.acl import *

def datafiller_user(ses):
    """
    * user groups:

        * g0: perms=[1, 2]
        * g1: perms=[2, 3]
    
    * user:
        
        * user0: groups=[g0, g1]
        * user1: groups=[g0], passwd = ''
        * user2: groups=[g1], passwd = ''"""

    g0 = UserGrpMdl(name = 'g0')
    g1 = UserGrpMdl(name = 'g1')
    u0 = UserMdl(username = 'user0')

    u0.groups.append(g0)
    u0.groups.append(g1)
    g0.perms.update([1, 2])
    g1.perms.update([2, 3])
    ses.add(u0)

    u1 = UserMdl(username = 'user1')
    u1.groups.append(g0)
    u1.auth_pw = UserAuthPWMdl('')
    ses.add(u1)

    u2 = UserMdl(username = 'user2')
    u2.groups.append(g1)
    u2.auth_pw = UserAuthPWMdl('')
    ses.add(u2)



def datafiller_acl(ses):
    """a = [ACLMdl(type = str(i), data = i) for i in range(3)]:
    a[i] dep on a[i+1] """

    a = [ACLMdl(type = str(i), data = i) for i in range(3)]
    for i in a:
        ses.add(i)

    for i in range(2):
        a[i].dep.append(a[i + 1])


def datafiller_acl_ugrp(ses):
    """allowed user group: g0"""
    from pynojo.lib.acl.ugrp import UgrpACL

    mdl = ACLMdl()
    g = ses.query(UserGrpMdl).filter(UserGrpMdl.name == 'g0').one()
    acl = UgrpACL([g.id])
    acl.save_to_model(mdl)

    ses.add(mdl)


datafillers = [datafiller_user, datafiller_acl,
        datafiller_acl_ugrp]
