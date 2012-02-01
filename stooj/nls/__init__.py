# $File: __init__.py
# $Date: Thu Feb 02 00:35:39 2012 +0800
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
"""Nativ Language Support for stooj. See also :ref:`devnotes-nls`."""

from stooj.exception import StoojInnerError

class TransInfo:
    """class that provides information about a translation"""

    name = None
    """Name of the translation, displayed on the web page."""

    locale_dir = None
    """Locale directory. The .mo file should be stored in
    locale_dir/LC_MESSAGES/stooj.mo"""

    def __init__(self, name, locale_dir):
        self.name = name
        self.locale_dir = locale_dir


# add translations here
_trans_list = []





def get_translation_list():
    """Return a list of :class:`TransInfo` instances, indicating the installed
    translations. The indices can be used as translation identifiers. The
    returned list should not be modified."""
    return _trans_list


_tr_cache = dict()

class Translator:
    """the class which actually implements the translation of message
    identifiers to translatied message strings"""

    _tr = None	# gettext.GNUTranslations class

    def __init__(self, lang):
        """
        :param lang: name of the language. If it is None,
                     :class:`gettext.NullTranslations` is used. Otherwise, if
                     no corresponding .mo file found,
                     :exc:`stooj.exception.StoojInnerError` would be raised.
        :type lang: str or None
        """
        global _tr_cache
        try:
            self._tr = _tr_cache[lang]
            return
        except KeyError:
            pass
        import gettext
        if lang is None:
            self._tr = gettext.NullTranslations()
            return

        from os.path import dirname, join
        locale_dir = join(dirname(__file__), 'locale')
        try:
            self._tr = gettext.translation('stooj', locale_dir, [lang])
        except IOError:
            raise StoojInnerError(
                    'attempt to load unimplmented translation: {0}' .
                    format(lang))

        _tr_cache[lang] = self._tr

    def get_translation(self, msgid, *args, **kargs):
        """Return a Unicode string translation of message identifier *msgid*,
        with *args* and *kargs* passed to :meth:`str.format` on the
        result. See also :meth:`get_plural_translation`."""
        return self._tr.ugettext(msgid).format(*args, **kargs)

    def get_plural_translation(self, singular, plural, n, *args, **kargs):
        """Return a Unicode string translation based on two message identifiers
        and the number *n*. When *n* is 1, *singular* is used for lookup in the
        catalog; otherwise *plural* is used. See also
        :meth:`get_translation`."""
        return self._tr.ungettext(singular, plural, n).format(*args, **kargs)


def get_translator(request):
    """Return an instance of :class:`Translator` according to the language
    implied by pyramid request *request*."""
    # pylint: disable=W0212
    if request._stooj_translator_cache is None:
        request._stooj_translator_cache = _get_translator(request)
    return request._stooj_translator_cache

def _get_translator(req):
    return Translator(None) # XXX


def init(request_factory):
    """Initialize NLS. *request_factory* is a pyramid request factory class to
    be configured.  Two methods named *_* and *_pl* will be added to it, which
    can be used for translation and plural translation, respectively. See
    :meth:`Translator.get_translation` and
    :meth:`Translator.get_plural_translation`.
    """

    request_factory._stooj_translator_cache = None

    request_factory._ = lambda self, *args, **kargs: \
            get_translator(self).get_translation(*args, **kargs)

    request_factory._pl = lambda self, *args, **kargs: \
            get_translator(self).get_plural_translation(*args, **kargs)

