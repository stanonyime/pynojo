# $File: user.py
# $Date: Mon Jan 30 23:58:36 2012 +0800
#
# This file is part of stooj
# 
# stooj is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# stooj is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with stooj.  If not, see <http://www.gnu.org/licenses/>.
#

"""models for users and user groups"""

from _base import *
from ..config import config
from hashlib import sha256 

_SALT_LEN = 5
_PASSWD_LEN = sha256().digest_size


# password encryption functions should take two arguments:
# user: an instance of User class
# passwd: the password to be ecrypted
def _pwd_enc_v0(user, passwd):
    m = sha256()
    m.update(user.username)
    m.update(chr(0))
    m.update(user._salt)
    m.update(chr(0))
    m.update(passwd)
    return m.digest()

_pwd_enc_funcs = [_pwd_enc_v0]



class UserGroup(Base):
    __tablename__ = 'usergrp'

    id = Column(Integer, primary_key = True)
    name = Column(String(config.user.GRPNAME_LEN_MAX))

    # users: backref defined in User.group




class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key = True)
    username = Column(String(config.user.USERNAME_LEN_MAX),
            index = True, unique = True)	# used for login, immutable
    dispname = Column(String(config.user.DISPNAME_LEN_MAX))	# display name

    group_id = Column(Integer, ForeignKey(UserGroup.id))	# the group that the user belongs to
    group = relationship(UserGroup, uselist = False,
            backref = backref('users', lazy = 'dynamic'))
    


    # following are used for authentication
    _salt = Column('salt', BINARY(_SALT_LEN))
    _pwd = Column('pwd', BINARY(_PASSWD_LEN))
    _pwd_enc_v = Column('pwdencv', SmallInteger,
            server_default = text(str(len(_pwd_enc_funcs) - 1)))	# version of password encryption algorithm


    def chk_passwd(self, passwd):
        """Return whether *passwd* matches the password set by this user."""
        from ..lib import stooj_assert
        stooj_assert(self.id is not None)
        stooj_assert(self._pwd_enc_v >= 0 and self._pwd_enc_v < len(_pwd_enc_funcs))
        enc_func = _pwd_enc_funcs[self._pwd_enc_v]
        if enc_func(self, passwd) != self._pwd:
            return False

        if self._pwd_enc_v != len(_pwd_enc_funcs) - 1:  # update the password if possible
            self.set_passwd(passwd)
        return True

    def set_passwd(self, passwd):
        """Set the password of the user to *passwd*."""
        from ..lib import gen_random_binary as grb
        self._salt = grb(_SALT_LEN)
        self._pwd = _pwd_enc_funcs[-1](self, passwd)
        self._pwd_enc_v = len(_pwd_enc_funcs) - 1

