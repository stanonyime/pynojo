# $File: _base.py
# $Date: Mon Mar 05 22:24:47 2012 +0800
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

__all__ = ['Base']
import unittest

_engine = None
_session_maker = None

def init():
    global _engine, _session_maker

    from sqlalchemy import create_engine, event
    from sqlalchemy.orm import sessionmaker, scoped_session

    from pynojo.model import install_db

    _engine = create_engine('sqlite:///:memory:')
    event.listen(_engine, 'connect', lambda con, record:
            con.execute('PRAGMA foreign_keys=ON'))
    install_db(_engine)

    _session_maker = scoped_session(sessionmaker(bind = _engine))

    ses = _session_maker()
    from pynojo.model import set_session_maker
    set_session_maker(_session_maker)


    from tests.model.datafiller import datafillers
    for i in datafillers:
        i(ses)

    ses.commit()



class Base(unittest.TestCase):
    """base class for model unit tests"""

    engine = None
    session_maker = None

    @classmethod
    def setUpClass(cls):
        if _engine is None:
            init()

        cls.engine = _engine
        cls.session_maker = _session_maker

        cls.set_up_class()

    @classmethod
    def tearDownClass(cls):
        cls.tear_down_class()
        cls.session_maker.commit()

    @classmethod
    def set_up_class(cls):
        """A class method called before tests in an individual class run."""
        pass


    @classmethod
    def tear_down_class(cls):
        """A class method called after tests in an individual class have
        run."""
        pass


