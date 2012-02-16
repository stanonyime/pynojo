## $File: form2.mako
## $Date: Thu Feb 16 23:34:34 2012 +0800
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

## this file provides helper functions for making 2-column forms
<%!
	from pynojo.lib import gen_random_str
	randid = lambda: 'ri-' + gen_random_str(5, ord('a'), ord('z'))
%>
<%def name="mkinput(label, **attr)">
	## generate a row for input
	## type defaults to 'text', and id defaults to a random one
	## support 'hint' attribute, which will be added to the 'title' of an anchor wrapping the title
	<%
		attr.setdefault('type', 'text')
		id = attr.get('id')
		if id is None:
			id = randid()
			attr['id'] = id
		hint = attr.pop('hint', None)
		if hint is not None:
			label = '<a title="{0}">{1}</a>'.format(hint, label)
	%>
	<div>
		<label for="${id}">${label}</label>
		<span>
			<input ${' '.join('{0}="{1}"'.format(k, v) for k, v in attr.iteritems())} />
		</span>
	</div>
</%def>
