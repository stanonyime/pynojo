## $File: base.mako
## $Date: Tue Feb 14 20:07:23 2012 +0800
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
##		page_name, page_content, additional_header
<!DOCTYPE HTML>
<html>
	<head>
		<meta http-equiv="Content-type" content="text/html;charset=UTF-8" />
		<link rel="shortcut icon" href="${request.static_path('favicon.ico')}" />
		<title><%block name="page_name"/> - ${config.WEBSITE_NAME}</title>
		<%block name='additional_header' />
	</head>
	<body>
		msgfromlayout0 <br />
		${_('msgfromlayout1')} <br />
		<%block name="page_content">
			this should not be seen
		</%block>
	</body>
</html>
