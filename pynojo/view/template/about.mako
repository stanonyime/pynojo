## $File: about.mako
## $Date: Wed Feb 15 23:06:04 2012 +0800
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
<%!
from pynojo.config import config
pkg = config.pkg
%>
<%inherit file="page_base.mako" />
<%block name="page_name">${_('About')}</%block>
<%block name="page_content">
	Project name: ${pkg.NAME} <br />
	Project website: <a href="${pkg.WEBSITE}">${pkg.WEBSITE}</a> <br />
	Release: ${pkg.RELEASE} <br />
	Copyright: ${pkg.COPYRIGHT} (see the
		<a href="http://code.google.com/p/pynojo/source/browse/AUTHORS">AUTHORS</a> file)
</%block>
