# $File: auth_pw.py
# $Date: Mon Feb 20 14:31:01 2012 +0800
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

"""user authentication via password"""

__all__ = ['UserAuthPW']

from hashlib import sha256 

from pynojo.lib import pynojo_assert
from pynojo.model._base import *
from pynojo.model.user import User

_SALT_LEN = 5
_PASSWD_LEN = sha256().digest_size

# password encryption functions should take two arguments:
# user: an instance of UserAuthPW class
# passwd: the password to be ecrypted
def _pw_enc_v0(uauth, passwd):
    # pylint: disable=W0212
    m = sha256()
    m.update(chr(0))
    m.update(uauth._salt)
    m.update(chr(0))
    m.update(passwd)
    return m.digest()

_pw_enc_funcs = [_pw_enc_v0]


class UserAuthPW(Base):
    """Usually this model is not directly used, except when creating a new
    user; use :attr:`User.auth_pw <pynojo.model.user.User.auth_pw>` instead."""
    __tablename__ = 'userauthpw'

    def __init__(self, passwd):
        self.set(passwd)

    uid = Column(Integer, ForeignKey(User.get_table_name() + '.id'),
            primary_key = True)

    user = relationship(User, uselist = False,
            backref = backref('auth_pw', uselist = False))

    _salt = Column('salt', BINARY(_SALT_LEN))
    _pw = Column('pw', BINARY(_PASSWD_LEN))

    # version of password encryption algorithm
    _pw_enc_v = Column('pwencv', SmallInteger,
            server_default = text(str(len(_pw_enc_funcs) - 1)))

    def check(self, passwd):
        """Return whether *passwd* matches the password set by this user."""
        pynojo_assert(self._pw_enc_v >= 0 and 
                self._pw_enc_v < len(_pw_enc_funcs))
        enc_func = _pw_enc_funcs[self._pw_enc_v]
        if enc_func(self, passwd) != self._pw:
            return False

        # update the password if possible
        if self._pw_enc_v != len(_pw_enc_funcs) - 1:
            self.set(passwd)
        return True

    def set(self, passwd):
        """Set the password to *passwd*."""
        from pynojo.lib import gen_random_str as grs
        self._salt = grs(_SALT_LEN)
        self._pw = _pw_enc_funcs[-1](self, passwd)
        self._pw_enc_v = len(_pw_enc_funcs) - 1



