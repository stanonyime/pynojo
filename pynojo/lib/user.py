# $File: user.py
# $Date: Mon Feb 27 20:54:33 2012 +0800
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
"""helper functions for maintaining users"""

import re

from sqlalchemy.orm.exc import NoResultFound

from pynojo.exc import PynojoRuntimeError
from pynojo.model import Session
from pynojo.model.user import UserMdl
from pynojo.config import config


_username_re = re.compile(r'^[-_a-zA-Z0-9]{{{min},{max}}}$'.format(
    min = config.user.USERNAME_LEN_MIN, max = config.user.USERNAME_LEN_MAX))
# it's said that compiled re is thread-safe, so no lock needed
# http://www.gossamer-threads.com/lists/python/python/391977
def validate_username(username):
    """Check whether *username* is a legal one. Raise
    :exc:`pynojo.exc.PynojoRuntimeError` on error."""
    if _username_re.match(username) is None:
        raise PynojoRuntimeError(_('Invalid username. Valid ones should ' \
            'contain only numbers, letters, dash (-) and underscore (_), ' \
            'and at least {min} characters and at most {max}.',
            min = config.user.USERNAME_LEN_MIN,
            max = config.user.USERNAME_LEN_MAX))

    if username in config.user.RESERVED_USERNAME:
        raise PynojoRuntimeError(_('Username "{name}" is reserved.',
            name = username))


def get_model(request):
    """Return an instance of :class:`pynojo.model.UserMdl`, or *None* if no user
    has logged in."""
    val = request.pynojo_cache.get(get_model, -1)
    if val == -1:
        val = request.pynojo_cache[get_model] = _get_model(request)
    return val


def check_login_pw(request, username, passwd, cookie_max_age = None):
    """Check user login via password authentication. Raise
    :exc:`pynojo.exc.PynojoRuntimeError` on error. If login is successful,
    corresponding cookies are set."""
    ses = Session()
    ok = True
    try:
        user = ses.query(UserMdl).filter(UserMdl.username == username).one()
    except NoResultFound:
        ok = False
    else:
        if user.auth_pw is None:
            ok = False
        else:
            ok = user.auth_pw.check(passwd)

    if not ok:
        raise PynojoRuntimeError(_('incorrect username/password'))

    request.pynojo_cache[get_model] = user
    request.set_cookie('uid', user.id, cookie_max_age)
    request.set_cookie('token', user.update_auth_code(), cookie_max_age)


def _get_model(req):
    uid = req.cookies.get('uid', -1)
    if uid == -1:
        return None

    ses = Session()
    try:
        user = ses.query(UserMdl).filter(UserMdl.id == uid).one()
    except NoResultFound:
        return None

    if user.get_auth_code() == req.cookies.get('token'):
        return user
    return None

