..  $File: devnotes.rst
    $Date: Sun Feb 12 14:37:35 2012 +0800
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


Notes for Developers
====================

.. contents::

Contact Kai Jia <jia.kai66@gmail.com> if you have any question about this page.


Getting Started
---------------


Environment Setup
^^^^^^^^^^^^^^^^^

#.  Install SQLite3 and its development packages if you don't already
    have them installed.  Usually this is via your system's package
    manager.  For example, on a Debian Linux system, do ``sudo apt-get
    install libsqlite3-dev``.

#.  Install virtualenv:

    .. code-block:: sh

        $ sudo pip install virtualenv

#.  Setup a workplace using virtualenv. Note that you may need to specify **-p
    python2** option to tell virtualenv to use Python 2. Replace
    <path-to-your-workplace> with something you like:

    .. code-block:: sh
        
        $ virtualenv <path-to-your-workplace>

#.  Write your own init.sh (note that it has already been added to
    *.gitignore*):

    .. code-block:: sh

        $ cd <path-to-pynojo-source-root>
        $ echo "export PATH=<path-to-your-workplace>/bin:$PATH" > init.sh
        $ . ./init.sh

#.  Use pip to get the dependencies installed:

    .. code-block:: sh

        $ pip install pyramid sqlalchemy sphinx pyenchant sphinxcontrib-spelling

#.  Generate the .mo files and documents (they are not tracked by the version
    control system):

    .. code-block:: sh

        $ cd <path-to-pynojo-source-root>/utils
        $ ./genmo
        $ cd ../docs
        $ ./gendoc

.. _devnotes-sysconf:

Configuration
^^^^^^^^^^^^^

The static system configuration package is :mod:`pynojo.config`. To allow the
developers applying their local settings without having to change the system
defaults, *pynojo/config/overwrite.py* has been added to *.gitignore*. Define a
function named *overwrite* in that file and change the configuration there.

An example file::

    def overwrite(conf):
        conf.PREFIX = '/pynojo-dev/'
        conf.ROUTE_PREFIX = conf.PREFIX



Miscellaneous Specifications and Instructions
---------------------------------------------

Framework
^^^^^^^^^

`Pyramid <http://pylonsproject.org/>`_ is used as the web
framework, and `SQLAlchemy <http://www.sqlalchemy.org/>`_
as the ORM. Note that pynojo uses a subclass of :class:`pyramid.request.Request`
as the request factory; see :class:`pynojo.__init__.Request`.


Code Style
^^^^^^^^^^

Follow the
`Style Guide for Python Code <http://www.python.org/dev/peps/pep-0008>`_.
Use `pylint <http://pypi.python.org/pypi/pylint>`_ to check the style
and find potential bugs. Execute the *run-pylint* script to invoke pylint.

The following lines should be included in every Python source file::

    # $File: <file name>
    # $Date: <last modification time>
    #
    # Copyright (C) 2012 the pynojo development team <see AUTHORS file>
    # 
    # Contributors to this file:
    #    <you name and email here>
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

Configure your editor to update the *$File* and *$Date* fields automatically.
Add your name to the contributors field and the AUTHORS file.

By the way, if vim is your favorite, you can add the following lines to
your vimrc:

.. code-block:: vim

    autocmd filetype python set expandtab
    autocmd filetype python set textwidth=79


Documenting
^^^^^^^^^^^

Write docstrings for every package, module, public class, public method, public
function, etc. The documents should be written in English. 

Register all the global names in :ref:`global-name-list`.

These documents are generated from
`reStructuredText <http://docutils.sf.net/rst.html>`_
sources and docstrings by `Sphinx <http://sphinx.pocoo.org/>`_.
Issue the following command to generate all the documents:

.. code-block:: sh

    $ cd <path-to-pynojo-source-root>/docs
    $ ./gendoc


*sphinxcontrib.spelling.* is used for spell-checking of all the documents. The
extra word list file is located at docs/wordlist.txt.


Threading
^^^^^^^^^

Although current CPython implementation does not fully support multithreading,
keep in mind that all the code should be **thread-safe**, so be careful when
modifying global variables. 

To avoid confusion, unexpected behavior or overuse of resource (exceeding the
thread limit in the server configuration), do not use multithreading unless
absolutely necessary.

If it is really necessary to spawn a child thread, remember to call
:func:`pynojo.lib.register_thread_request` in the child thread to ensure that
functions depending on :func:`pynojo.lib.get_thread_request` work correctly.



.. _devnotes-nls:

Native Language Support (NLS)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

All the human-readable messages in pynojo python source code and templates should
be written in English. There should NOT be any non-ASCII characters in the
source, except in nls/config.py, where TRANS_LIST describes the available
translations.

pynojo dose not use the NLS mechanism provided by Pyramid and Chameleon.
Instead, pynojo has its own :mod:`pynojo.nls` package, which is based on
`GNU gettext <http://www.gnu.org/software/gettext/>`_.  To generate the pot
file, cd to *utils* and execute *./genpot*.  The pot file will be written
to pynojo/nls/pynojo.pot. The locale directory is pynojo/nls/locale. To update the
po files or regenerate the mo files, cd to *utils* and execute *./update-po* or
*./genmo* respectively.

To localize:

    * In a pyramid view callable, the *request* parameter passed to it will
      include the translation functions as methods named *_* and *_pl*. They are
      appropriate for the locale of the client, which is already determined
      according to the information provided by *request*.
    * *_* and *_pl* are also added to the *__builtin__* namespace, so they can
      be invoked directly. This method is slightly slower than the one above,
      for it has to access thread local variable. It is assumed that the caller
      resides in the same thread as that of the pyramid view callable, otherwise
      :func:`pynojo.lib.register_thread_request` has to be called explicitly
      before calling *_* or *_pl*.
    * In a page template, the appropriate translation functions are the global
      functions named *_* and *_pl*.
    * See :func:`pynojo.nls.init` and :mod:`pynojo.view` for some further
      explanations.
    
To add a new translation, use *msginit* to generate the po file from the pot
file. Move the output po file to pynojo/nls/locale/*<lang>*/LC_MESSAGES/pynojo.po
and **append** corresponding :class:`pynojo.nls.config.TransInfo` instance to
*TRANS_LIST* defined in pynojo/nls/config.py. DO NOT change the order of the
translations already listed there.

Here are two examples:

In a pyramid view callable::

    @view_config(route_name = mkroute(pattern = ''), renderer = 'template/index.pt')
    def _index(request):
        return {'msg': request._('msgfrompython') + _('builtin-trans')}

In a page template:

.. code-block:: html

    <div metal:use-macro="layout">
        <div metal:fill-slot="content">
            ${_('{0}from{t}', 'msg', t = 'template')} <br />
            ${msg} <br />
            ${_pl('singular', 'plural', 1)} <br />
            ${_pl('singular', 'plural', 2)} <br />
        </div>
    </div>


Locale detection details:

    * If the user does not login, detect the locale via Accept-Language field in
      the HTTP request header.
    * Cookie: TODO

