# $File: __init__.py
# $Date: Sun Mar 04 12:15:10 2012 +0800
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

"""models for users and user groups"""

__all__ = ['UserMdl', 'UserGrpMdl']

from pynojo.config import config
from pynojo.model._base import *


_PERMS_CACHE_LEN = 127

class _Tablename:
    UserMdl = 'user'
    UserGrpMdl = 'ugrp'
    MapUserGrpAndGrpPerm = 'mugrpperm'
    MapUserAndUserGrp = 'muugrp'


class MapUserGrpAndGrpPerm(Base):
    """Many-to-many map between user groups and user group permissions. Usually
    this model is not directly used; use :attr:`UserGrpMdl.perms` instead."""
    __tablename__ = _Tablename.MapUserGrpAndGrpPerm

    def __init__(self, perm):
        self.perm = perm

    gid = Column(Integer,
            ForeignKey(_Tablename.UserGrpMdl + '.id', ondelete = 'CASCADE'), 
            nullable = False, index = True, primary_key = True)

    perm = Column(SmallInteger, index = True, primary_key = True)



class MapUserAndUserGrp(Base):
    """Many-to-many map between user and user groups. Usually this model is not
    directly used; use :attr:`UserMdl.groups` and :attr:`UserGrpMdl.users`
    instead."""
    __tablename__ = _Tablename.MapUserAndUserGrp

    uid = Column(Integer, ForeignKey(_Tablename.UserMdl + '.id'),
            nullable = False, index = True, primary_key = True)

    gid = Column(Integer,
            ForeignKey(_Tablename.UserGrpMdl + '.id', ondelete = 'CASCADE'),
            nullable = False, index = True, primary_key = True)



class UserMdl(Base):
    """The user model. Note that deleting an user from the database is not
    allowed."""
    __tablename__ = _Tablename.UserMdl

    id = Column(Integer, primary_key = True)

    username = Column(String(config.user.USERNAME_LEN_MAX),
            index = True, unique = True, nullable = False)
    """username for login, immutable"""

    groups = relationship('UserGrpMdl',
            secondary = _Tablename.MapUserAndUserGrp)
    """groups that this user belongs to; a relationship to
    :class:`UserGrpMdl`."""


    # pylint: disable=C0322
    # I do not know why pylint thinks it is an operator...
    auth_pw = None
    """UserMdl authentication via password. This attribute is a relationship
    to :class:`UserAuthPWMdl <pynojo.model.user.auth_pw.UserAuthPWMdl>`;
    defined by backref in :attr:`UserAuthPWMdl.user
    <pynojo.model.user.auth_pw.UserAuthPWMdl.user>`."""


    extra = Column(JSONEncodeDict(config.user.EXTRA_FIELD_LEN),
            default = dict(), nullable = False)
    """a :class:`JSONEncodeDict <pynojo.model._ext_type.JSONEncodeDict>`, for
    storing fields that are not usually changed and have no indexes."""


    @validates('username')
    def _validate_username(self, key, val):
        # pylint: disable=W0613,R0201
        from pynojo.lib import user
        user.validate_username(val)
        return val


    # maintaining user permission

    _perms_cache_rst = None
    _perms_cache = Column('permscache', String(_PERMS_CACHE_LEN))

    @property
    def perms(self):
        """a frozenset of integer, the permissions that this user has."""
        if self._perms_cache_rst is None:
            self._perms_cache_rst = self._get_perms()
        return self._perms_cache_rst


    def _get_perms(self):
        if self._perms_cache is None:
            rst = set()
            for i in self.groups:
                rst.update(i.perms)
            rst = frozenset(rst)
            self._perms_cache = '|' . join([str(i) for i in rst])
            return rst
        return frozenset([int(i) for i in self._perms_cache.split('|')])


    @staticmethod
    def invalidate_perm_cache(session, gid):
        """Invalidate the permission cache of users belong to the group with id
        *gid*. It is unnecessary to call this method if you just change user
        group permissions via :attr:`UserGrpMdl.perms`. But it should be called
        explicitly when a user group is delete, or any other operation that
        might affect user permissions is made.."""

        # pylint: disable=W0612
        for (cls, pk), obj in session.identity_map.iteritems():
            if cls is UserMdl:
                session.expire(obj, ['_perms_cache'])
                obj._perms_cache_rst = None

        sub = session.query(MapUserAndUserGrp.uid) \
                .filter(MapUserAndUserGrp.gid == gid)
        session.query(UserMdl).filter(UserMdl.id.in_(sub)) \
                .update({UserMdl._perms_cache: None},
                        synchronize_session = False)


    def invalidate_self_perm_cache(self):
        """Invalidate the permission cache. Direct invoking of this method is
        unnecessary if you change the relationship between users and user
        groups via :attr:`UserMdl.groups` or :attr:`UserGrpMdl.users`."""
        self._perms_cache = None
        self._perms_cache_rst = None



    # user authentication

    _auth_code = Column('authcode', BINARY(config.user.AUTH_CODE_LEN))

    def get_auth_code(self):
        """Return an ascii authentication code string, which can be set to
        cookie and later used for authentication.  See also
        :meth:`update_auth_code`."""
        if self._auth_code is None:
            return self.update_auth_code()
        from base64 import b64encode
        return b64encode(self._auth_code, '-_')

    def update_auth_code(self):
        """Update the authentication code, invalidating the previously
        generated one. Return the new authentication code."""
        from pynojo.lib import gen_random_str
        self._auth_code = gen_random_str(config.user.AUTH_CODE_LEN)
        return self.get_auth_code()



class UserGrpMdl(Base):
    __tablename__ = _Tablename.UserGrpMdl

    id = Column(Integer, primary_key = True)

    name = Column(String(config.user.GRPNAME_LEN_MAX), index = True,
            nullable = False)
    """name of the group"""

    users = relationship('UserMdl', lazy = 'dynamic',
            secondary = _Tablename.MapUserAndUserGrp)
    """users belonging to this group; a relationship to :class:`UserMdl`.  Note
    that dynamic loading is used."""

    _perms = relationship('MapUserGrpAndGrpPerm', collection_class = set,
            cascade = 'all, delete-orphan', passive_deletes = True)

    # pylint: disable=C0322
    perms = association_proxy('_perms', 'perm')
    """permissions of this group. It just behaves like a Python *set*.
    Available permissions are defined in
    :class:`permdef.UserGrpMdl <pynojo.model.permdef.UserGrpMdl>`."""




def _invcache_on_grp_perm_chg(target, *args):
    # pylint: disable=W0613
    ses = object_session(target)
    if ses is not None:
        UserMdl.invalidate_perm_cache(ses, target.id)

# pylint: disable=W0212
for _event in 'append', 'remove', 'set':
    event.listen(UserGrpMdl._perms, _event, _invcache_on_grp_perm_chg)
    event.listen(UserGrpMdl.users, _event, lambda target, value, *args:
            value.invalidate_self_perm_cache())
    event.listen(UserMdl.groups, _event, lambda target, *args:
            target.invalidate_self_perm_cache())

