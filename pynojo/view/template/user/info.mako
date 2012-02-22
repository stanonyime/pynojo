## $File: info.mako
## $Date: Mon Feb 20 20:37:18 2012 +0800
##
## Copyright (C) 2012 the pynojo development team <see AUTHORS file>
## 
## Contributors to this file:
##    Kai Jia	<jia.kai66@gmail.com>
##
## This file is part of pynojo
## 
## pynojo is free software: you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation, either version 3 of the License, or
## (at your option) any later version.
## 
## pynojo is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.
## 
## You should have received a copy of the GNU General Public License
## along with pynojo.  If not, see <http://www.gnu.org/licenses/>.
##
<%! from pynojo.lib import user %>
<%
	model = user.get_model(request)
	if model is None:
		return
%>
<%def name="_mkli(name, url)">
	<li><a href="${url}" class="jqcolorbox">${name}</a></li>
</%def>
Hello, ${model.extra['dispname']}! <br />
<ul class="user-action">
	${_mkli(_('Change Password'), request.route_path('user.chgpw'))}
	${_mkli(_('Update Profile'), request.route_path('user.chgpw'))}
	<li><a href="#" onclick="user_logout()">${_('Log Out')}</a></li>
</ul>
