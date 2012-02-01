..  stooj docs
    $File: devnotes.rst
    $Date: Wed Feb 01 11:33:39 2012 +0800

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
and find potential bugs.


Native Language Support (NLS)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

All the human-readable messages in stooj source code should be written in
English. 

stooj dose not use the NLS mechanism provided by Pyramid and Chameleon.
Instead, stooj has its own :mod:`stooj.nls` package, which is based on
`GNU gettext <http://www.gnu.org/software/gettext/>`_.  To generate the pot
file, cd to *utils* and execute *./genpot*.  The pot file will be written
to stooj/nls/stooj.pot. 

To localize:

    * In a pyramid view callable, the *request* parameter will include the
      translator as an attribute named *_*. The translator is appropriate for
      the language of the client, which is already determined according to the
      information provided by *request*.
    * In a page template, the appropriate translator is the global function
      named *_*.
    * See :meth:`stooj.nls.StrTranslator.get_translation` for usage of the
      translator.
    
Here are some examples about how to use the translator:

In a pyramid view callable::

    @view_config(route_name = mkroute(pattern = ''), renderer = 'template/index.pt')
    def _index(request):
        return {'msg': request._('msgfrompython')}

In a page template:

.. code-block:: html

    <div metal:use-macro="layout">
        <div metal:fill-slot="content">
            ${_('{0}from{t}', 'msg', t = 'template')} <br />
            ${msg}
        </div>
    </div>


Tests
^^^^^

It is recommended to write test suite for some basic functions.
Place the test scripts in stooj/tests, and execute *run-tests* to
run the test suit.
