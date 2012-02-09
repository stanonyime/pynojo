# $File: user.py
# $Date: Wed Feb 08 21:59:13 2012 +0800
#
# Copyright (C) 2012 the pynojo development team <see AUTHORS file>
# 
# Contributors to this file:
#    Kai Jia <jia.kai66@gmail.com>
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


from hashlib import sha256 

from pynojo.model._base import *
from pynojo.config import config

_SALT_LEN = 5
_PASSWD_LEN = sha256().digest_size


# password encryption functions should take two arguments:
# user: an instance of User class
# passwd: the password to be ecrypted
def _pwd_enc_v0(user, passwd):
    # pylint: disable=W0212
    alg = sha256()
    alg.update(user.username)
    alg.update(chr(0))
    alg.update(user._salt)
    alg.update(chr(0))
    alg.update(passwd)
    return alg.digest()

_pwd_enc_funcs = [_pwd_enc_v0]

class _Tablename:
    User = 'user'
    UserGroup = 'ugrp'
    MapUserGrpAndGrpPerm = 'ugrpperm'



class User(Base):
    __tablename__ = _Tablename.User

    id = Column(Integer, primary_key = True)

    username = Column(String(config.user.USERNAME_LEN_MAX),
            index = True, unique = True)
    """username for login, immutable"""

    dispname = Column(String(config.user.DISPNAME_LEN_MAX))
    """display name"""

    grp_id = Column(Integer, ForeignKey(_Tablename.UserGroup + '.id'))
    """id of the group that the user belongs to"""

    group = relationship('UserGroup', uselist = False,
                backref = backref('users', lazy = 'dynamic',
                    cascade = "all, delete-orphan"))
    """the group that the user belongs to; a relationship to
    :class:`UserGroup`"""


    # following are used for authentication

    _salt = Column('salt', BINARY(_SALT_LEN))
    _pwd = Column('pwd', BINARY(_PASSWD_LEN))

    # version of password encryption algorithm
    _pwd_enc_v = Column('pwdencv', SmallInteger,
            server_default = text(str(len(_pwd_enc_funcs) - 1)))

    def chk_passwd(self, passwd):
        """Return whether *passwd* matches the password set by this user."""
        from pynojo.lib import pynojo_assert
        pynojo_assert(self.id is not None)
        pynojo_assert(self._pwd_enc_v >= 0 and 
                self._pwd_enc_v < len(_pwd_enc_funcs))
        enc_func = _pwd_enc_funcs[self._pwd_enc_v]
        if enc_func(self, passwd) != self._pwd:
            return False

        # update the password if possible
        if self._pwd_enc_v != len(_pwd_enc_funcs) - 1:
            self.set_passwd(passwd)
        return True

    def set_passwd(self, passwd):
        """Set the password of the user to *passwd*."""
        from pynojo.lib import gen_random_str as grs
        self._salt = grs(_SALT_LEN)
        self._pwd = _pwd_enc_funcs[-1](self, passwd)
        self._pwd_enc_v = len(_pwd_enc_funcs) - 1


    def gen_auth_code(self):
        """Generate an ascii authentication code string, which can be set to
        cookie and later used for authentication by calling
        :meth:`check_auth_code`."""
        pass # XXX TODO: and to seperate authentication




class UserGroup(Base):
    __tablename__ = _Tablename.UserGroup

    id = Column(Integer, primary_key = True)

    name = Column(String(config.user.GRPNAME_LEN_MAX), index = True)
    """name of the group"""

    users = None
    """users belonging to this group; defined by backref in :attr:`User.group`.
    Note that dynamic loading is used."""

    _perms = relationship('MapUserGrpAndGrpPerm', collection_class = set,
            cascade = "all, delete-orphan")

    perms = association_proxy('_perms', 'perm')
    """permissions of this group. It just behaves like a Python *set*.
    Available permissions are defined in :class:`pynojo.permdef.UserGroup`."""




class MapUserGrpAndGrpPerm(Base):
    """Many-to-many map between user groups and user group permissions. Usually
    this model is not directly used, use :attr:`UserGroup.perms` instead."""
    __tablename__ = _Tablename.MapUserGrpAndGrpPerm

    def __init__(self, perm):
        self.perm = perm

    grp_id = Column(Integer, ForeignKey(_Tablename.UserGroup + '.id'), 
            index = True, primary_key = True)

    perm = Column(SmallInteger, index = True, primary_key = True)


