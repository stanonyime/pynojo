/*
 * $File: user.js
 * $Date: Sun Feb 19 20:43:06 2012 +0800
 *
 * Copyright (C) 2012 the pynojo development team <see AUTHORS file>
 * 
 * Contributors to this file:
 *    Kai Jia	<jia.kai66@gmail.com>
 *
 * This file is part of pynojo
 * 
 * pynojo is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 * 
 * pynojo is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License
 * along with pynojo.  If not, see <http://www.gnu.org/licenses/>.
 *
 */

function user_register_form_init(validate_addr, msg)
{
	/*
	* msg: ask_passwd, passwd_unmatch
	*/
	var msgobj = $('#reg-msg');
	$('#reg-username').ajax_validate(validate_addr, msgobj, $.colorbox.resize);
	$('#reg-passwd').blur(function(){
		if ($(this).val() == '') 
			msgobj.validate_msg_fail(msg.ask_passwd);
		else
			msgobj.validate_msg_success(' ');
        $.colorbox.resize();
	});
	$('#reg-passwd2').blur(function(){
		if ($(this).val() != $('#reg-passwd').val())
			msgobj.validate_msg_fail(msg.passwd_unmatch);
		else
			msgobj.validate_msg_success(' ');
        $.colorbox.resize();
	});
	$('#reg-button').button();
    $('#reg-form').ajaxForm({
        'dataType': 'json',
        'success': function(data) {
            if (data.fail)
            {
                msgobj.validate_msg_fail(data.msg);
                $.colorbox.resize();
            }
            else
			{
				$('#login-form input[name="username"]').val($('#reg-username').val());
				$('#login-form input[name="passwd"]').val($('#reg-passwd').val());
				setTimeout(function(){$('#login-form').submit();}, 2000);
				$.colorbox({'html': data.msg});
			}
        }
    });
}

function user_login_form_init()
{
	$("#login-form").ajaxForm({
		'dataType': 'json',
		'success': function(data) {
			if (data.fail)
                $.colorbox({'html': data.msg});
			else
				window.location.reload(true);
		}
	})
}

