# $File: __init__.py
# $Date: Sun Jan 15 01:48:11 2012 +0800
#
# This file is part of stooj
# 
# stooj is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# stooj is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with stooj.  If not, see <http://www.gnu.org/licenses/>.
#
"""define views for stooj
globals added to template:
    layout: global layout macro
    _: i18n translation function
"""

from pyramid.renderers import get_renderer
from pyramid.events import (subscriber, BeforeRender)
from ..func import subscriber

_layout_macro = None

@subscriber(BeforeRender)
def _add_global(event):
    from ..i18n import translators    # XXX
    global _layout_macro, _translator
    if _layout_macro is None:
        _layout_macro = get_renderer('template/layout.pt').implementation().macros['layout']
    event['layout'] = _layout_macro
    event['_'] = translators


