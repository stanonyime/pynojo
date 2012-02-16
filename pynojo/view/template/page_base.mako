## $File: page_base.mako
## $Date: Thu Feb 16 19:23:57 2012 +0800
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
## blocks:
##		page_name, page_content
<!DOCTYPE HTML>
<html>
	<head>
		<meta http-equiv="Content-type" content="text/html;charset=UTF-8" />
		<link rel="shortcut icon" href="${request.static_path('favicon.ico')}" />

		<link rel="stylesheet" type="text/css" href="${request.static_path('jslib/jquery-ui.css')}" />
		<link rel="stylesheet" type="text/css" href="${request.static_path('jslib/colorbox.css')}" />
		<script type="text/javascript" src="${request.static_path('jslib/jquery.js')}"></script>
		<script type="text/javascript" src="${request.static_path('jslib/jquery.colorbox.js')}"></script>
		<script type="text/javascript" src="${request.static_path('jslib/jquery.form.js')}"></script>

		<link rel="stylesheet" type="text/css" href="${request.static_path('pynojo_all.css')}" />
		<script type="text/javascript" src="${request.static_path('pynojo_all.js')}"></script>

		<title><%block name="page_name"/> - ${config.WEBSITE_NAME}</title>
	</head>
	<body>
		<div id="page-wrap">
			<%include file="page_base/banner.mako" />
			<%include file="page_base/nav.mako" />
			<div id="page-content">
				<%block name="page_content" />
			</div>
		</div>
		<script type="text/javascript">
			$(document).ready(function(){
				pynojo_init("${config.path.STATIC_PREFIX}")
			})
		</script>
	</body>
</html>
