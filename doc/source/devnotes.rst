Notes for Developers
====================


Preparations
------------

Install `virtualenv <http://pypi.python.org/pypi/virtualenv>`_,
and setup a virtualenv directory.  Then write your own init.sh
to initialize virtualenv environment. Note that init.sh has
already been added to *.gitignore*.
One possible version of init.sh:

.. code-block:: sh

    export PYTHONDONTWRITEBYTECODE=1
    export PATH=~/programming/python2-virtualenv/bin:$PATH

And install the following packages required by stooj
(recommend using pip or easy_install):

    * pyramid
    * SQLAlchemy
    * WebTest
    * sphinx




Miscellaneous Specifications and Instructions
---------------------------------------------

Code Style
^^^^^^^^^^

Follow the
`Style Guide for Python Code <http://www.python.org/dev/peps/pep-0008>`_.
Use `pylint <http://pypi.python.org/pypi/pylint>`_ to check the style
and find potential bugs.


