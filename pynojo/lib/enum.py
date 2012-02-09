# $File: enum.py
# $Date: Tue Feb 07 22:35:24 2012 +0800
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

"""Implements enumerations in Python"""

import threading

from pynojo.exception import PynojoInternalError

# count of all enumeration items
_enum_cnt = 0
_enum_cnt_lock = threading.Lock()


class _EnumItem:
    def __init__(self, order):
        self.order = order
        self.has_data = False
        self.data = None

    def __call__(self, data):
        self.has_data = True
        self.data = data
        return self


class _EnumMetaClass(type):

    def __new__(mcs, name, base, attr):
        # pylint: disable=W0212

        if '_enum_base_class_flag' in attr:
            del attr['_enum_base_class_flag']
            return super(_EnumMetaClass, mcs).__new__(mcs, name, base, attr)

        if len(base) != 1:
            raise PynojoInternalError('enumeration class derived from multiple ' +
                    'bases')
        try:
            cur_enum = base[0]._enum_start
            step = base[0]._enum_step
        except AttributeError:
            raise PynojoInternalError('_enum_start or _enum_step not found in ' +
                    'enumeration base class')

        enum_items = list()	# (key, val)
        enumed_attr = dict()
        for (key, val) in attr.iteritems():
            if isinstance(val, _EnumItem):
                enum_items.append((key, val))
            else:
                enumed_attr[key] = val

        enum_data = dict()
        enum_items.sort(cmp = lambda x, y: cmp(x[1].order, y[1].order))
        for i in enum_items:
            enumed_attr[i[0]] = cur_enum
            if i[1].has_data:
                enum_data[cur_enum] = i[1].data

            cur_enum += step

        # set this so that enumeration items in classes derived from the newly
        # created class can continue the enumeration count
        enumed_attr['_enum_start'] = cur_enum

        enumed_attr['_enum_data'] = enum_data

        return super(_EnumMetaClass, mcs).__new__(mcs, name, base, enumed_attr)

    def __getattribute__(mcs, name):
        if name == 'enum':
            global _enum_cnt, _enum_cnt_lock
            with _enum_cnt_lock:
                ret = _enum_cnt
                _enum_cnt += 1
            return _EnumItem(ret)
        return super(_EnumMetaClass, mcs).__getattribute__(name)

    def __setattr__(mcs, name, value):
        raise PynojoInternalError('trying to modify an enumeration class')




def get_base(start = 0, step = 1):
    """Return the base class for creating an enumeration. Assuming the
    generated base class is Base, to create an enumeration, derive a class from
    Base, and assign *Base.enum* to the attributes that you want to mark as an
    enumeration item, which will be automatically replaced by an integer
    starting from *start* and increasing *step*. You can also assign to an
    attribute *Base.enum(val)*, where *val* is an associated data to this item
    and can later be retrieved by calling the class method :meth:`get_data` on
    the derived class. Enumeration classes can also be derived to construct
    subclasses. The order of enumeration items is preserved and used to
    determin the corresponding enumeration value, so it is safe to append new
    items to the attribute list while staying backward compatible.  But adding
    new items will affect all subclasses derived from it. Trying to modify an
    attribute or deriving from multiple bases will cause an error.  See the
    example below and the source of
    :meth:`pynojo.tests.test_lib.LibUnitTests.test_enum` for details.

    :param start: the value assigned to the first enumeration item
    :type start: int

    :param step: the value increased between two adjacent items
    :type step: int

    Example:

    .. testcode::
        
        from pynojo.lib.enum import get_base
        Base = get_base(start = 42, step = 8)

        class Enum0(Base):
            VAL0 = Base.enum
            VAL1 = Base.enum
            VAL2 = 'str'

        class Enum1(Enum0):
            VAL3 = Base.enum

        class Enum2(Base):
            VAL4 = Base.enum
            VAL5 = Base.enum('hello, world')
            
        print Enum0.VAL0, Enum0.VAL1, Enum0.VAL2
        print Enum1.VAL3
        print Enum2.VAL4
        print Enum2.get_data(Enum2.VAL5)


    Then the output would be:

    .. testoutput::

        42 50 str
        58
        42
        hello, world
    """

    class _Base(object):
        __metaclass__ = _EnumMetaClass
        __slots__ = tuple()

        _enum_start = start
        _enum_step = step
        _enum_base_class_flag = True

        enum = lambda args: None

        @classmethod
        def get_data(cls, key):
            """get the associated data for enumeration value *key*"""
            while True:
                try:
                    data = cls.__dict__['_enum_data']
                except KeyError:
                    raise PynojoInternalError('no associated data for the'
                        ' enumeration item')

                try:
                    return data[key]
                except KeyError:
                    cls = cls.__bases__[0]

        def __setattr__(self, name, value):
            raise PynojoInternalError('trying to modify an enumeration class')


    return _Base

