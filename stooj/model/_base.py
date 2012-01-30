# $File: _base.py
# $Date: Mon Jan 30 14:32:22 2012 +0800
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

from sqlalchemy import Column
from sqlalchemy.types import *
from sqlalchemy.types import BINARY
from sqlalchemy.schema import *
from sqlalchemy.sql.expression import text
from sqlalchemy.orm import relationship, backref

from sqlalchemy.ext.declarative import declarative_base as _base
Base = _base()
