# $File: _base.py
# $Date: Fri Feb 10 14:49:47 2012 +0800
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
"""Provides base class for SQLAlchemy ORM and import some commonly used
SQLAlchemy functions. """

# pylint: disable=C0103

from sqlalchemy import Table, Column, event
from sqlalchemy.types import *
from sqlalchemy.types import BINARY
from sqlalchemy.schema import *
from sqlalchemy.sql.expression import text
from sqlalchemy.orm import relationship, backref
from sqlalchemy.orm.session import object_session
from sqlalchemy.ext.associationproxy import association_proxy

from sqlalchemy.ext.declarative import declarative_base as _base

class DeclarativeBase(object):
    """Base class for pynojo ORM."""
    @classmethod
    def get_table_name(cls):
        """Return the table name."""
        # pylint: disable=E1101
        return cls.__tablename__

Base = _base(cls = DeclarativeBase)

# to avoid global namespace pollution
del DeclarativeBase

