========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis| |requires|
        | |codecov|
        | |scrutinizer| |codacy| |codeclimate|
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|
.. |docs| image:: https://readthedocs.org/projects/ukw-intelli-store/badge/?style=flat
    :target: https://ukw-intelli-store.readthedocs.io/
    :alt: Documentation Status

.. |travis| image:: https://api.travis-ci.com/maddonix/ukw-intelli-store.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.com/github/maddonix/ukw-intelli-store

.. |requires| image:: https://requires.io/github/maddonix/ukw-intelli-store/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/maddonix/ukw-intelli-store/requirements/?branch=master

.. |codecov| image:: https://codecov.io/gh/maddonix/ukw-intelli-store/branch/master/graphs/badge.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/maddonix/ukw-intelli-store

.. |codacy| image:: https://img.shields.io/codacy/grade/8711a53d3cb049f88c2b87b70c1a6dbb.svg
    :target: https://www.codacy.com/app/maddonix/ukw-intelli-store
    :alt: Codacy Code Quality Status

.. |codeclimate| image:: https://codeclimate.com/github/maddonix/ukw-intelli-store/badges/gpa.svg
   :target: https://codeclimate.com/github/maddonix/ukw-intelli-store
   :alt: CodeClimate Quality Status

.. |version| image:: https://img.shields.io/pypi/v/ukw-intelli-store.svg
    :alt: PyPI Package latest release
    :target: https://pypi.org/project/ukw-intelli-store

.. |wheel| image:: https://img.shields.io/pypi/wheel/ukw-intelli-store.svg
    :alt: PyPI Wheel
    :target: https://pypi.org/project/ukw-intelli-store

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/ukw-intelli-store.svg
    :alt: Supported versions
    :target: https://pypi.org/project/ukw-intelli-store

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/ukw-intelli-store.svg
    :alt: Supported implementations
    :target: https://pypi.org/project/ukw-intelli-store

.. |commits-since| image:: https://img.shields.io/github/commits-since/maddonix/ukw-intelli-store/v0.0.0.svg
    :alt: Commits since latest release
    :target: https://github.com/maddonix/ukw-intelli-store/compare/v0.0.0...master


.. |scrutinizer| image:: https://img.shields.io/scrutinizer/quality/g/maddonix/ukw-intelli-store/master.svg
    :alt: Scrutinizer Status
    :target: https://scrutinizer-ci.com/g/maddonix/ukw-intelli-store/


.. end-badges

Package to read and explore material consumption

* Free software: MIT license

Installation
============

::

    pip install ukw-intelli-store

You can also install the in-development version with::

    pip install https://github.com/maddonix/ukw-intelli-store/archive/master.zip


Documentation
=============


https://ukw-intelli-store.readthedocs.io/


Development
===========

To run all the tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
