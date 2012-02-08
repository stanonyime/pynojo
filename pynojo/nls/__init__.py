# $File: __init__.py
# $Date: Wed Feb 08 13:51:51 2012 +0800
#
# Copyright (C) 2012 the pynojo development team <see AUTHORS file>
# 
# Contributors to this file:
#    Kai Jia <jia.kai66@gmail.com>
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
"""Nativ Language Support for pynojo. See also :ref:`devnotes-nls`."""

from pynojo.exception import StoojInnerError
from pynojo.nls.config import TRANS_LIST


class Translator:
    """the class which actually implements the translation of message
    identifiers to translatied message strings"""

    _tr = None	# gettext.GNUTranslations class

    def __init__(self, lang):
        """
        :param lang: name of the language. If it is None,
                     :class:`gettext.NullTranslations` is used. Otherwise, if
                     no corresponding .mo file found,
                     :exc:`pynojo.exception.StoojInnerError` would be raised.
        :type lang: str or None
        """
        import gettext
        if lang is None:
            self._tr = gettext.NullTranslations()
        else:
            from os.path import dirname, join
            locale_dir = join(dirname(__file__), 'locale')
            try:
                self._tr = gettext.translation('pynojo', locale_dir, [lang])
            except IOError:
                raise StoojInnerError(
                        'attempt to load unimplmented translation: {0}' .
                        format(lang))

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
    """Return an instance of :class:`Translator` according to the locale
    implied by pyramid request *request*."""
    # pylint: disable=W0212
    k = 'translator'
    if k not in request.stooj_cache:
        tr = _get_translator(request)
        request.stooj_cache[k] = tr
    else:
        tr = request.stooj_cache[k]
    return tr



_trans_list_tag2translator = None
_trans_list_offers = None
_trans_list_default_translator = Translator(None)
def _init_trans_list_vars():
    global _trans_list_tag2translator, _trans_list_offers
    _trans_list_tag2translator = dict()
    _trans_list_offers = list()
    for i in TRANS_LIST:
        tr = Translator(i.locale_dir)
        _trans_list_offers.extend(i.lang_tag)
        for j in i.lang_tag:
            _trans_list_tag2translator[j] = tr

def _get_translator(req):
    # XXX: detect by cookie
    tag = req.accept_language.best_match(_trans_list_offers)
    if tag is None:
        return _trans_list_default_translator
    return _trans_list_tag2translator[tag]


def init(request_factory):
    """Initialize NLS and configure pyramid request factory class
    *request_factory*.  Two methods named *_* and *_pl* will be added to it,
    which can be used for translation and plural translation, respectively.
    Functions with the same names will also be added to the builtin namespace.
    See :meth:`Translator.get_translation` and
    :meth:`Translator.get_plural_translation` for the usage. """

    # pylint: disable=W0108
    # this lambda is really necessary ...
    import __builtin__
    from pynojo.lib import get_thread_request
    __builtin__._ = lambda *args, **kargs: \
            get_translator(get_thread_request()).get_translation(
                    *args, **kargs)
    __builtin__._pl = lambda *args, **kargs: \
            get_translator(get_thread_request()).get_plural_translation(
                    *args, **kargs)

    _init_trans_list_vars()

    request_factory._ = lambda self, *args, **kargs: \
            get_translator(self).get_translation(*args, **kargs)

    request_factory._pl = lambda self, *args, **kargs: \
            get_translator(self).get_plural_translation(*args, **kargs)

