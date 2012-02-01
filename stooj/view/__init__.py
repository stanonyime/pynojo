# $File: __init__.py
# $Date: Thu Feb 02 00:43:29 2012 +0800
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
"""
This module define the views for stooj. When initializing the application,
:meth:`pyramid.config.Configurator.scan` should be called on this module.

The following globals will be added to Chameleon templates:
    * *layout*: global layout macro
    * *_*: normal translation function (see
      :meth:`stooj.nls.Translator.get_translation`)
    * *_pl*: plural translation function (see
      :meth:`stooj.nls.Translator.get_plural_translation`)
"""

from pyramid.events import subscriber, BeforeRender

_layout_macro = None
@subscriber(BeforeRender)
def _add_global(event):
    # pylint: disable=W0212
    global _layout_macro
    if _layout_macro is None:
        from pyramid.renderers import get_renderer
        _layout_macro = get_renderer('stooj.view:template/layout.pt') . \
                implementation()
    event['layout'] = _layout_macro
    event['_'] = event['request']._
    event['_pl'] = event['request']._pl

