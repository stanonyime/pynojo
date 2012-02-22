## $File: login.mako
## $Date: Mon Feb 20 19:56:29 2012 +0800
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
<%! from pynojo.view.lib.form2 import MakoForm2Helper %>
<% fh = MakoForm2Helper(locals()) %>
<form method="post" class="form2" id="login-form"
	action="${request.route_path('user.login')}">
	<% fh.mkinput(_('Username:'), name = 'username') %>
	<% fh.mkinput(_('Password:'), name = 'passwd', type = 'password') %>
	<% fh.mkcheckbox(_('Stay logged in for 2 weeks'), name = 'set_cookie') %>
	<div>
		<button type="submit" class="jqui-button">${_('Log in')}</button>
		<a href="${request.route_path('user.reg')}" class="jqcolorbox jqui-button">${_('Register')}</a>
	</div>
</form>
<script type="text/javascript">
	user_login_form_init();
</script>
