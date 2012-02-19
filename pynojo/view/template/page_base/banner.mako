## $File: banner.mako
## $Date: Sun Feb 19 16:34:47 2012 +0800
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
<%namespace file="../user.mako" name="user_tp" />
<div id="page-banner">
	<img src="${request.static_path('img/pynojo-banner.jpg')}" alt="banner" />
	<div>
		<%
			model = user.get_model(request)
			if model is None:
				user_tp.show_login_form()
			else:
				user_tp.show_user_info(model)
		%>
	</div>
</div>
