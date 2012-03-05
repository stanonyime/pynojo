# $File: acl.py
# $Date: Sun Mar 04 19:50:43 2012 +0800
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

"""models for access limiters. Usually these models are not directly used; use
APIs in :mod:`pynojo.lib.acl` instead."""

__all__ = ['ACLMdl']

from pynojo.exc import PynojoRuntimeError
from pynojo.model._base import *

class _Tablename:
    ACLMdl = 'acl'


_acl_dep = Table('acldep', Base.metadata,
        Column('id0', Integer,
            ForeignKey(_Tablename.ACLMdl + '.id', ondelete = 'CASCADE'),
            index = True, nullable = False),
        Column('id1', Integer,
            ForeignKey(_Tablename.ACLMdl + '.id', ondelete = 'CASCADE'),
            index = True, nullable = False))

class ACLMdl(Base):
    __tablename__ = _Tablename.ACLMdl

    TYPE_MAX_LEN = 20

    id = Column(Integer, primary_key = True)
    type = Column(String(TYPE_MAX_LEN), nullable = False)
    data = Column(PickleType, nullable = False)

    dep = relationship('ACLMdl',
            lazy = 'dynamic',
            cascade = 'all',
            secondary = _acl_dep,
            primaryjoin = (id == _acl_dep.c.id0),
            secondaryjoin = (id == _acl_dep.c.id1),
            passive_deletes = True)
    """the ACLs that this ACL depends on; i.e. ACLs used by this ACL.
    Dynamic lazy loading is used."""

    used_by = relationship('ACLMdl',
            lazy = 'dynamic',
            cascade = 'all',
            secondary = _acl_dep,
            primaryjoin = (id == _acl_dep.c.id1),
            secondaryjoin = (id == _acl_dep.c.id0),
            passive_deletes = True)
    """the ACLs using this ACL; i.e. those depending on this ACL.
    Dynamic lazy loading is used."""
    

def _check_circular(root, v0, attr):
    ok = True
    if root is v0:
        ok = False
    else:
        qh = 0
        queue = [v0]
        visited = set(queue)

        while qh < len(queue):
            for i in queue[qh].__getattribute__(attr):
                if i not in visited:
                    if i is root:
                        ok = False
                        break
                    visited.add(i)
                    queue.append(i)
            qh += 1

    if ok:
        return True
    raise PynojoRuntimeError(_('found ACL circular dependency ' \
            '(related ACL ids: {0}, {1})', root.id, v0.id))


event.listen(ACLMdl.dep, 'append', lambda target, value, initiator:
        _check_circular(target, value, 'dep'))

event.listen(ACLMdl.used_by, 'append', lambda target, value, initiator:
        _check_circular(target, value, 'used_by'))

