# $File: __init__.py
# $Date: Wed Feb 01 00:14:23 2012 +0800
#
# Copyright (C) 2012 the stooj development team <see AUTHORS file>
# 
# Contributors to this file:
#    Kai Jia <jia.kai66@gmail.com>
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

"""Database models for stooj. See the source files for details."""

def install_db(engine):
    """Create all the tables in sqlalchemy engine *engine*."""
    # pylint: disable=W0612
    from pkgutil import walk_packages
    for loader, module_name, is_pkg in  walk_packages(__path__):
        __import__(module_name, globals(), locals(), [], -1)

    from stooj.model._base import Base
    Base.metadata.create_all(engine)

