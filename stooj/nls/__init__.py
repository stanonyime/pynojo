# $File: __init__.py
# $Date: Wed Feb 01 11:15:02 2012 +0800
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
"""Nativ Language Support for stooj"""

class StrTranslator:
    """L10n class"""
    def __init__(self, lang):
        """
        :param lang: name of the language
        :type lang: str
        """
        pass

    def get_translation(self, string, *args, **kargs):
        """Return the translation of *string*, with *args* and *kargs* passed
        to *str.format*."""
        # XXX: not implemented
        return string.format(*args, **kargs)


def get_translator(request): # XXX
    """Return a translation function according to the
    language implied by pyramid request *request*.
    See :meth:`StrTranslator.get_translation` for usage of
    the returned function."""
    return StrTranslator('x').get_translation

def init(request_factory):
    """Initialize NLS. *request_factory* is 
    a pyramid request factory class to be configured.
    An attribute named *_* will be added to it, which
    can be used for translation.
    """

    def _tr(self, *args, **kargs):
        # pylint: disable=W0212
        if self._translator_cache is None:
            self._translator_cache = get_translator(self)
        return self._translator_cache(*args, **kargs)

    request_factory._translator_cache = None
    request_factory._ = _tr

