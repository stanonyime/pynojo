/*
 * $File: common.js
 * $Date: Fri Feb 17 15:33:13 2012 +0800
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

function pynojo_init(static_prefix)
{
	$(".jqui-button").button();
	$(".jqcolorbox").colorbox();
	document.globals = new Object();
	document.globals.static_prefix = static_prefix;
}

(function($){
	$.fn.ajax_validate = function(url, msg_obj, update_hook) {
		/*
		 * send the data to *url* via GET method using the key 'v'
		 * the server should return a json-encoded object:
		 *		fail: 0 for success, otherwise for failure
		 *		msg: message to be put to msg_obj
		 * *update_hook*, if supplied, will be called after the data
		 *		in *msg_obj* got updated
		 */
		return this.blur(function(){
			msg_obj.html('<img alt="loading" src="' +
				document.globals.static_prefix + '/img/loading.gif" />');
			$.ajax({
				'url': url,
				'cache': false,
				'data': {'v': $(this).val()},
				'dataType': 'json',
				'success': function(data) {
					if (data.fail)
						msg_obj.validate_msg_fail(data.msg);
					else 
						msg_obj.validate_msg_success(data.msg);
					if (update_hook)
						update_hook();
				}
			})
		})
	};

	$.fn.validate_msg_success = function(msg) {
		$this = $(this);
		$this.removeClass('fail');
		$this.addClass('success');
		$this.html(msg);
	}

	$.fn.validate_msg_fail = function(msg) {
		$this = $(this);
		$this.addClass('fail');
		$this.removeClass('success');
		$this.html(msg);
	}
})(jQuery);

