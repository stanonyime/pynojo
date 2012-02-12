# $File: __init__.py
# $Date: Sun Feb 12 23:35:51 2012 +0800
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

"""Database models for pynojo. See the source files for details. """

from pyramid.events import subscriber, BeforeRender

from pynojo.config import config

# pylint: disable=C0103
Session = config.db.make_session()


@subscriber(BeforeRender)
def _commit_session(event):
    # pylint: disable=W0613,E1101
    Session.commit()


def install_db(engine):
    """Create all the tables using sqlalchemy engine *engine*."""
    # pylint: disable=W0612
    from pkgutil import walk_packages
    for loader, module_name, is_pkg in  walk_packages(__path__):
        __import__(module_name, globals(), locals(), [], -1)

    from pynojo.model._base import Base
    Base.metadata.create_all(engine)


