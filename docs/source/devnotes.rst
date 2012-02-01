..  stooj docs
    $File: devnotes.rst
    $Date: Thu Feb 02 00:24:12 2012 +0800

Notes for Developers
====================

.. contents::


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

These documents are generated from
`reStructuredText <http://docutils.sf.net/rst.html>`_
sources and docstrings by `Sphinx <http://sphinx.pocoo.org/>`_.
Issue the following command to generate all the documents:

.. code-block:: sh

    cd docs
    ./gendoc



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


.. _devnotes-nls:

Native Language Support (NLS)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

All the human-readable messages in stooj source code should be written in
English. 

stooj dose not use the NLS mechanism provided by Pyramid and Chameleon.
Instead, stooj has its own :mod:`stooj.nls` package, which is based on
`GNU gettext <http://www.gnu.org/software/gettext/>`_.  To generate the pot
file, cd to *utils* and execute *./genpot*.  The pot file will be written
to stooj/nls/stooj.pot. The locale directory is stooj/nls/locale. To update the
po files, cd to *utils* and execute *./update-po*.

To localize:

    * In a pyramid view callable, the *request* parameter passed to it will
      include the translation functions as methods named *_* and *_pl*. They are
      appropriate for the locale of the client, which is already determined
      according to the information provided by *request*.
    * In a page template, the appropriate translation functions are the global
      functions named *_* and *_pl*.
    * See :func:`stooj.nls.init` and :mod:`stooj.view` for some further
      explanations.
    
Here are two examples about how to use the translator:

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


To add a new translation, **append** it to *_trans_list* defined in
stooj/nls/__init__.py. DO NOT touch any other translations already defined
there.

Tests
^^^^^

It is recommended to write test suite for some basic functions.
Place the test scripts in stooj/tests, and execute *run-tests* to
run the test suit.
