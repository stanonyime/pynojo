# $File: user.py
# $Date: Mon Jan 30 00:07:26 2012 +0800
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

"""model for users and user groups"""

from _base import *
from ..config import config
from hashlib import sha256 

_SALT_LEN = 5
_PASSWD_LEN = sha256().digest_size


# password encryption functions should take two arguments:
# user: an instance of User class
# passwd: the password to be ecrypted
def _pwd_enc_v0(user, passwd):
    pass

_pwd_enc_funcs = [_pwd_enc_v0]

class User(Base):
    """User model. See the source for details."""
    __tablename__ = 'user'

    id = Column(Integer, primary_key = True)
    username = Column(String(config.user.USERNAME_LEN_MAX))	# used for login
    dispname = Column(String(config.user.DISPNAME_LEN_MAX))	# display name

    _salt = Column('salt', String(_SALT_LEN))
    _pwd = Column('pwd', String(_PASSWD_LEN))
    _pwd_enc_v = Column('pwdencv', SmallInteger,	# version of password encryption algorithm
            server_default = text(str(len(_pwd_enc_funcs) - 1)))


    def chk_passwd(self, passwd):
        """Return whether *passwd* matches the password set by this user."""
        from ..exception import StoojInnerError
        if self.id is None:
            raise StoojInnerError('attempt to call chk_passwd on an User instance with id is None')
        if self._pwd_enc_v < 0 or self._pwd_enc_v >= len(_pwd_enc_funcs):
            raise StoojInnerError('invalid _pwd_enc_v for user #{0}' . format(self.id))
        enc_func = _pwd_enc_funcs[self._pwd_enc_v]
        if enc_func(self, passwd) != self._pwd:
            return False

        if self._pwd_enc_v != len(_pwd_enc_funcs) - 1:  # update the password if possible
            self.set_passwd(passwd)
        return True

    def set_passwd(self, passwd):
        """Set the password of the user to *passwd*"""
        from ..func import gen_random_binary as grb
        self._salt = grb(_SALT_LEN)
        self._pwd = _pwd_enc_funcs[-1](self, passwd)
        self._pwd_enc_v = len(_pwd_enc_funcs) - 1

