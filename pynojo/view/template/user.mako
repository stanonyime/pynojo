## $File: user.mako
## $Date: Thu Feb 16 23:30:12 2012 +0800
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
<%namespace file="lib/form2.mako" import="mkinput" />
<form method="POST" class="form2 wide" id="userreg-form"
	action="${request.route_path('user.reg')}">

	<div class='msg' id="userreg-msg">${_('Please fill in your information')}</div>
	${mkinput(_('Username:'), name = 'username', id = 'reg-username',
		hint = _('Username is a unique identifier of a user, used for login.'))}
	${mkinput(_('Password:'), name = 'passwd', type = 'password', id = 'reg-passwd')}
	${mkinput(_('Confirm Password:'), name = 'confirm_passwd', type = 'password', id = 'reg-passwd2')}
	<div><button type="sumit" id="reg-button" class="jqui-button">${_('Submit')}</button></div>

</form>
<script type="text/javascript">
	var msg = $('#userreg-msg');
	$('#reg-username').ajax_validate('${request.route_path("user.reg.validate-username")}', msg)
	$('#reg-passwd').blur(function(){
		if ($(this).val() == '') {
			msg.validate_msg_fail('${_("You should enter a password.")}');
		} else {
			msg.validate_msg_success(' ');
		}
	})
	$('#reg-passwd2').blur(function(){
		if ($(this).val() != $('#reg-passwd').val()) {
			msg.validate_msg_fail('${_("The passwords do not match.")}');
		}else {
			msg.validate_msg_success(' ');
		}

	})
	$('#reg-button').button();
</script>
<%def name="show_user_info(model)">
	user info <br />
	${str(model) | h}
</%def>
<%def name="show_login_form()">
	<form method="POST" class="form2"
		action="${request.route_path('user.login')}">
		${mkinput(_('Username:'), name = 'username')}
		${mkinput(_('Password:'), name = 'passwd', type = 'password')}
		<div>
			<button type="submit" class="jqui-button">${_('Login')}</button>
			<a href="${request.route_path('user.reg')}" class="jqcolorbox jqui-button">${_('Register')}</a>
		</div>
	</form>
	<div id="user-reg-page-div"></div>
</%def>
