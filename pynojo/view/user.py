# $File: user.py
# $Date: Thu Feb 16 19:38:14 2012 +0800
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

from pyramid.view import view_config
from pynojo.view import mkroute

@view_config(route_name = mkroute(pattern = 'user/login', name = 'user.login'))
def login(request):
    return None

@view_config(route_name = mkroute(pattern = 'user/reg',
    name = 'user.reg'), renderer = 'user.mako')
def register(request):
    return {}


@view_config(route_name = mkroute(pattern = 'user/reg/vdname',
    name = 'user.reg.validate-username'), renderer = 'cjson')
def validate_username(request):
    username = request.GET['v']
    return {'fail': int(username == 'x'), 'msg': username}

