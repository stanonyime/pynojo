..  $File: perm-model.rst
    $Date: Mon Feb 27 20:47:41 2012 +0800
    -----------------------------------------------------------------
    Copyright (C) 2012 the pynojo development team <see AUTHORS file>
    Contributors to this file:
       Kai Jia	<jia.kai66@gmail.com>
    -----------------------------------------------------------------
    This file is part of pynojo
    pynojo is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    pynojo is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
    You should have received a copy of the GNU General Public License
    along with pynojo.  If not, see <http://www.gnu.org/licenses/>.

The Permission Model
====================

.. contents::

Contact Kai Jia <jia.kai66@gmail.com> if you have any question about this page.


Users and User Groups
---------------------

Each user can be assigned to multiple user groups, and each user group can be
given multiple permissions, which are used for authorization of system
management tasks.  The permissions are defined in
:class:`pynojo.model.permdef.UserGrp`.

For a user, the permissions that it has is the union of the permissions of
groups that it belongs to.


Problem Access Control
----------------------

Whether a problem can be accessed by a particular user is determined by the
user's accessibility to the problem groups(PG) that it belongs to. Each PG is
associated to an :ref:`ACL <perm-model.acl>`. A user is able to access a PG if
the ACL associated with that PG allows the user's request.

A user gains access to a problem if he has access to **at least one** of the PGs
that it belongs to. Although this might weaken the access controllability, it is
designed so to simplify overall design and speed up listing problems. A user can
only see the PGs that he has access to, so under such design, when listing
problems in a PG, it is not needed to consider for each problem the user's
access to other PGs that the it belongs to.


Event Access Control
--------------------

An event is an activity that lasts for a period of time, associated with some
problems and can be associated with an :ref:`ACL <perm-model.acl>`. For example,
it can be a time-limited assignment, a test or a contest. The event manager will
modify the problem groups(PG) of the problems in upcoming events. For an event,
a virtual PG associated with the ACL of it will be created, and all the problems
in this event will be associated only with that virtual PG. So the event can
have full access control in those problems. After an event ends, the event
manager is responsible to restore the original relationship between problems and
PGs, and delete the virtual PG.


.. _perm-model.acl:

Access Limiter (ACL)
--------------------

ACL is an abstract access control mechanism used by pynojo. It can be viewed as
an abstract base class, and the resource that needs access control can be
associated with an instance of an implemented subclass of ACL. Each ACL instance
is identified by a unique ACL id. This is the basic idea of ACL, and refer to
:mod:`pynojo.lib.acl` and :mod:`pynojo.model.acl` for the detailed API
descriptions.
