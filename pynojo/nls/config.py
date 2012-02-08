# -*- coding: utf-8 -*-
# $File: config.py
# $Date: Fri Feb 03 14:28:35 2012 +0800
# Copyright (C) 2012 the pynojo development team <see AUTHORS file>
# 
# Contributors to this file:
#    Kai Jia <jia.kai66@gmail.com>
# $Date: Fri Feb 03 14:28:35 2012 +0800
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
"""configuration for available translations"""

class TransInfo:
    """class that provides information about a translation"""

    name = None
    """Name of the translation, displayed on the web page."""

    locale_dir = None
    """Locale directory. The .mo file should be stored in
    *locale_dir*/LC_MESSAGES/pynojo.mo. If set to None, no translation would be
    performed."""

    lang_tag = None
    """List of the language tags that this translation applies to."""

    def __init__(self, name, locale_dir, lang_tag):
        self.name = name
        self.locale_dir = locale_dir
        if isinstance(lang_tag, str):
            lang_tag = [lang_tag]
        self.lang_tag = lang_tag


# list available translations here
TRANS_LIST = [
        TransInfo(u'English', None, 'en'),
        TransInfo(u'简体中文', 'zh_CN', 'zh-CN')]

