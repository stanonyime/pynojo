..  stooj docs
    $File: devnotes.rst
    $Date: Fri Feb 03 14:41:22 2012 +0800

Notes for Developers
====================

.. sectionauthor:: Kai Jia <jia.kai66@gmail.com>

.. contents::


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

#.  Setup a workplace using virtualenv. Note that you may need to sepcify **-p
    python2** option to tell virtualenv to use Python 2. Replace
    <path-to-your-workplace> with something you like:

    .. code-block:: sh
        
        $ virtualenv <path-to-your-workplace>

#.  Write your own init.sh (note that it has already been added to
    *.gitignore*):

    .. code-block:: sh

        $ cd <path-to-stooj-source-root>
        $ echo "export PATH=<path-to-your-workplace>/bin:$PATH" > init.sh
        $ . ./init.sh

#.  Use pip to get the dependencies installed:

    .. code-block:: sh

        $ pip install pyramid sqlalchemy webtest sphinx


.. _devnotes-sysconf:

Configuration
^^^^^^^^^^^^^

TODO


Document Generation
^^^^^^^^^^^^^^^^^^^

These documents are generated from
`reStructuredText <http://docutils.sf.net/rst.html>`_
sources and docstrings by `Sphinx <http://sphinx.pocoo.org/>`_.
Issue the following command to generate all the documents:

.. code-block:: sh

    $ cd <path-to-stooj-source-root>/docs
    $ ./gendoc


Miscellaneous Specifications and Instructions
---------------------------------------------

Framework
^^^^^^^^^

`Pyramid <http://pylonsproject.org/>`_ is used as the web
framework, and `SQLAlchemy <http://www.sqlalchemy.org/>`_
as the ORM.


Code Style
^^^^^^^^^^

Follow the
`Style Guide for Python Code <http://www.python.org/dev/peps/pep-0008>`_.
Use `pylint <http://pypi.python.org/pypi/pylint>`_ to check the style
and find potential bugs. Execute *run-pylint* (possibly with *-r n* options) to
execute pylint.

Write docstrings for every package, module, public
class, public method, public function, etc. The documents are written in
English. 

By the way, if vim is your favorite, you can add the following lines to
your vimrc:

.. code-block:: vim

    autocmd filetype python set expandtab
    autocmd filetype python set textwidth=79

And please keep in mind that all the code should be **thread-safe**, so be
careful when modifying global variables.



.. _devnotes-nls:

Native Language Support (NLS)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

All the human-readable messages in stooj python source code and templates should
be written in English. There should NOT be any non-ASCII characters in the
source, except in nls/config.py, where TRANS_LIST describes the available
translations.

stooj dose not use the NLS mechanism provided by Pyramid and Chameleon.
Instead, stooj has its own :mod:`stooj.nls` package, which is based on
`GNU gettext <http://www.gnu.org/software/gettext/>`_.  To generate the pot
file, cd to *utils* and execute *./genpot*.  The pot file will be written
to stooj/nls/stooj.pot. The locale directory is stooj/nls/locale. To update the
po files or regenerate the mo files, cd to *utils* and execute *./update-po* or
*./genmo* respectively.

To localize:

    * In a pyramid view callable, the *request* parameter passed to it will
      include the translation functions as methods named *_* and *_pl*. They are
      appropriate for the locale of the client, which is already determined
      according to the information provided by *request*.
    * In a page template, the appropriate translation functions are the global
      functions named *_* and *_pl*.
    * See :func:`stooj.nls.init` and :mod:`stooj.view` for some further
      explanations.
    
To add a new translation, use *msginit* to generate the po file from the pot
file. Move the output po file to stooj/nls/locale/*<lang>*/LC_MESSAGES/stooj.po
and **append** corresponding :class:`stooj.nls.config.TransInfo` instance to
*TRANS_LIST* defined in stooj/nls/config.py. DO NOT change the order of the
translations already listed there.

Here are two examples:

In a pyramid view callable::

    @view_config(route_name = mkroute(pattern = ''), renderer = 'template/index.pt')
    def _index(request):
        return {'msg': request._('msgfrompython')}

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


Locale Detection Details:

    * If the user does not login, detect the locale via Accept-Language field in
      the HTTP request header.
    * TODO

Tests
^^^^^

It is recommended to write test suite for some basic functions.
Place the test scripts in stooj/tests, and execute *run-tests* to
run the test suit.
