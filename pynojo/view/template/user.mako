## $File: user.mako
## $Date: Wed Feb 15 23:36:17 2012 +0800
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
user register page
<%def name="show_user_info(model)">
	user info <br />
	${str(model) | h}
</%def>
<%def name="show_login_form()">
	<form method="POST" class="form2"
		action="${request.route_path('user.login')}">
		<div>
			<label>${_('Username:')}</label>
			<span><input type="text" name="username" /></span>
		</div>
		<div>
			<label>${_('Password:')}</label>
			<span><input type="password" name="passwd" /></span>
		</div>
		<div>
			<div style="text-align: center">
				<button type="submit" class="jqui-button">${_('Login')}</button>
				<a href="${request.route_path('user.register')}" class="jqui-button">
					${_('Register')}
				</a>
			</div>
		</div>
	</form>
</%def>
