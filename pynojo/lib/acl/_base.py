# $File: _base.py
# $Date: Mon Mar 05 22:29:28 2012 +0800
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
"""ACL base"""

__all__ = ['Base']

from pynojo.model import make_session
from pynojo.model.acl import ACLMdl

class _BaseMetaClass(type):

    def __new__(mcs, name, base, attr):
        # pylint: disable=W0212
        from pynojo.exc import PynojoInternalError

        obj = super(_BaseMetaClass, mcs).__new__(mcs, name, base, attr)

        if name != 'Base' and Base in base:
            if len(name) > ACLMdl.TYPE_MAX_LEN:
                raise PynojoInternalError('ACL name {0} is too long'
                        .format(name))

            if name in Base.acl_impls:
                raise PynojoInternalError('duplicated ACL name: {0}'
                        .format(name))

            Base.acl_impls[name] = obj

        return obj


class Base(object):
    """The base class for ACL. All ACL implementations should be directly
    derived from this class. The name of derived class should be unique among
    all the subclasses, and should not exceed :attr:`TYPE_MAX_LEN
    <pynojo.model.acl.ACLMdl.TYPE_MAX_LEN>` characters."""

    __metaclass__ = _BaseMetaClass
    __slots__ = tuple()

    acl_impls = dict()
    """all the ACL implementations. Key is the class name (also used for
    :attr:`type <pynojo.model.acl.ACLMdl.type>`), and value is the
    class object."""

    @classmethod
    def from_model(cls, model):
        """A factory method for generating an instance of this ACL based on the
        data provided by *model*, which is an :class:`ACLMdl
        <pynojo.model.acl.ACLMdl>` instance. This is an abstract method and
        should be overwritten by ACL implementations."""
        raise NotImplementedError()

    def save_to_model(self, model):
        """Save this ACL instance to the SQLAlchemy model *model*. This is an
        abstract method and should be overwritten by ACL implementations."""
        raise NotImplementedError()

    def check(self, request):
        """Check whether this ACL allows the access request. *request* is a
        :class:`pynojo.__init__.Request` instance. This is an abstract method
        and should be overwritten by ACL implementations."""
        raise NotImplementedError()


    @classmethod
    def from_id(cls, acl_id):
        """Return an ACL instance whose id is *acl_id*."""
        ses = make_session()
        mdl = ses.query(ACLMdl).filter(ACLMdl.id == acl_id).one()
        return cls.acl_impls[mdl.type].from_model(mdl)

