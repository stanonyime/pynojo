## $File: nav.mako
## $Date: Thu Feb 16 14:34:45 2012 +0800
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
<%! from pynojo.view.navbar import PAGES %>
<%
	pg_route_name = request.matched_route
	if pg_route_name is not None:
		pg_route_name = pg_route_name.name
%>
<div id="page-nav">
	<div id="page-nav-wrapper">
		<div id="bg1"></div>
		<div id="bg2"></div>
		<ul>
			% for i in PAGES:
				<li ${'class="active"' if pg_route_name == i.route_name else ''}>
				<a href="${request.route_path(i.route_name)}">${i.title}</a>
				</li>
			% endfor
		</ul>
		<br style="clear: both" />
	</div>
</div>
