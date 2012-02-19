# $File: form2.py
# $Date: Sun Feb 19 20:49:45 2012 +0800
#
# Copyright (C) 2012 the pynojo development team <see AUTHORS file>
# 
# Contributors to this file:
#    Kai Jia	<jia.kai66@gmail.com>
#
# This file is part of pynojo
# 
# pynojo is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# pynojo is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with pynojo.  If not, see <http://www.gnu.org/licenses/>.
#
"""2-column forms. See also *static/gss/form2.gss*."""

from pynojo.lib import gen_random_str
from pynojo.view.lib import MakoBase

class MakoForm2Helper(MakoBase):
    """2-column form helper class. Note that all the methods in this class
    write to the context directly, so python blocks, rather than expression
    substitution, should be used. (e.g. write ``<% foo.mkinput() %>``, not 
    ``${foo.mkinput()}``, in the template).
    
    All the methods in this class treat those special arguments:

        * hint: if supplied, a question mark icon will be appended to the
                label text, and the icon will be wrapped by an anchor with
                *title* set to the hint 
        * id: if not supplied, a random id will be used"""

    def mkinput(self, label, **attr):
        """Generate a row for a input element. The default value for *type* is
        'text'."""
        self._mkinput(label, None, **attr)

    def mkcheckbox(self, label, **attr):
        """Generate a row for checkbox input. If 'checked' is in the keys of
        *attr* (no matter what its value is), the checkbox will be
        preselected. And the default value for the *value* attribute is 1."""
        if 'checked' in attr:
            attr['checked'] = 'checked'
        attr['type'] = 'checkbox'
        attr.setdefault('value', 1)
        self._mkinput(label, 'nf', **attr)

    def _mkinput(self, label, div_class, **attr):
        attr.setdefault('type', 'text')
        label = self._update(label, attr)
        with self.tag('div', {'class': div_class}):
            with self.tag('span'):
                self.stag('input', attr)
            with self.tag('label', {'for': attr['id']}):
                self._w(label)

    def _update(self, label, attr):
        """update id, and return the modified label"""
        if 'id' not in attr:
            attr['id'] = 'rid' + gen_random_str(5, ord('a'), ord('z'))
        hint = attr.pop("hint", None)
        if hint is not None:
            label = '{0}<a style="margin-left:0.5em;" title="{1}"><img ' \
                    'alt="hint" src="{2}" /></a>'.format(label, hint,
                        self.local_vars['request'].static_path('img/help.png'))
        return label

