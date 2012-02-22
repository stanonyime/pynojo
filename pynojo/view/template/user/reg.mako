## $File: reg.mako
## $Date: Mon Feb 20 19:47:04 2012 +0800
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
<form method="post" class="form2 wide" id="reg-form"
	action="${request.route_path('user.reg.submit')}">

	<div class='msg' id="reg-msg">${_('Please fill in your information.')}</div>
	<% fh.mkinput(_('Username:'), name = 'username', id = 'reg-username',
		hint = _('Username is a unique identifier of a user, used for login. ' \
		'It can not be changed. Note that username is case sensitive.')) %>
	<% fh.mkinput(_('Display Name:'), name = 'dispname',
		hint = _('The name to be displayed on the page. You can also consider it as a nickname.')) %>
	<% fh.mkinput(_('Password:'), name = 'passwd', type = 'password', id = 'reg-passwd') %>
	<% fh.mkinput(_('Confirm Password:'), type = 'password', id = 'reg-passwd2') %>
	<div><button type="sumit" id="reg-button" class="jqui-button">${_('Submit')}</button></div>
</form>
<script type="text/javascript">
	user_register_form_init('${request.route_path("user.reg.validate-username")}', {
		'ask_passwd': '${_("Please enter a password.")}',
		'passwd_unmatch': '${_("The passwords do not match.")}'
	});
</script>
