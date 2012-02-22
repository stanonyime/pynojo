# $File: user.py
# $Date: Mon Feb 20 19:46:59 2012 +0800
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
"""handling requests about users, such as login/logout/register"""

import cgi

from pyramid.view import view_config

from pynojo.view import mkroute
from pynojo.lib import user
from pynojo.exc import PynojoRuntimeError
from pynojo.model import Session
from pynojo.model.user import User
from pynojo.model.user.auth_pw import UserAuthPW

@view_config(route_name = mkroute(pattern = 'user/login', name = 'user.login'),
        renderer = 'cjson')
def login(request):
    """POST: username, passwd, [set_cookie]
    
    Return: fail, msg

        note that *msg* is returned only if *fail* != 0"""
    p = request.POST
    age = None
    if 'set_cookie' in p:
        age = 3600 * 24 * 7 * 2 # 2 weeks
    try:
        user.check_login_pw(request, p['username'], p['passwd'], age)
        return {'fail': 0}
    except PynojoRuntimeError as e:
        return {'fail': 1, 'msg': _('Failed to log in: {msg}', msg = str(e))}



@view_config(route_name = mkroute(pattern = 'user/reg',
    name = 'user.reg'), renderer = 'user/reg.mako')
def register(request):
    # pylint: disable=W0613
    return {}


@view_config(route_name = mkroute(pattern = 'user/reg/submit',
    name = 'user.reg.submit'), renderer = 'cjson')
def register_submit(request):
    """POST: username, passwd, dispname

    Return: fail, msg
    """
    p = request.POST
    p['dispname'] = cgi.escape(p['dispname'])
    uname = p['username']
    try:
        validate_username(uname)
        ses = Session()
        u = User(username = uname, extra = dict())
        for i in ('dispname', ):
            u.extra[i] = p[i]
        u.auth_pw = UserAuthPW(p['passwd'])
        ses.add(u)
        ses.commit()
    except PynojoRuntimeError as e:
        return {'fail': 1, 'msg': _('Failed to register: {msg}', msg = str(e))}
    return {
            'fail': 0,
            'msg': _('Congratulations! You have successfully registered.' \
                    '{line_break}Log in after 2 seconds...',
                    line_break = '<br />')
            }



@view_config(route_name = mkroute(pattern = 'user/reg/vdname',
    name = 'user.reg.validate-username'), renderer = 'cjson')
def validate_username_on_request(request):
    v = request.GET['v']
    try:
        validate_username(v)
    except PynojoRuntimeError as e:
        return {'fail': 1, 'msg': str(e)}
    return {'fail': 0, 'msg': _('Good! Username "{0}" still available.', v)}



@view_config(route_name = mkroute(pattern = 'user/chgpasswd',
    name = 'user.chgpw'), renderer = 'user/chgpw.mako')
def chg_passwd(request):
    # pylint: disable=W0613
    return {}

def validate_username(username):
    """Validate the username, raise :exc:`pynojo.exc.PynojoRuntimeError` on
    error. This function checks the name's legality and non-existence."""
    user.validate_username(username)
    ses = Session()
    if ses.query(User).filter(User.username == username).count():
        raise PynojoRuntimeError(_('Sorry, username "{0}" already exists.',
            username))


