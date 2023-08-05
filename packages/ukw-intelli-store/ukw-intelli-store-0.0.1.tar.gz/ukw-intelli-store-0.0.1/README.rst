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

.. |travis| image:: https://api.travis-ci.com/Maddonix/ukw-intelli-store.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.com/github/Maddonix/ukw-intelli-store

.. |requires| image:: https://requires.io/github/Maddonix/ukw-intelli-store/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/Maddonix/ukw-intelli-store/requirements/?branch=master

.. |codecov| image:: https://codecov.io/gh/Maddonix/ukw-intelli-store/branch/master/graphs/badge.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/Maddonix/ukw-intelli-store

.. |codacy| image:: https://img.shields.io/codacy/grade/8711a53d3cb049f88c2b87b70c1a6dbb.svg
    :target: https://www.codacy.com/app/Maddonix/ukw-intelli-store
    :alt: Codacy Code Quality Status

.. |codeclimate| image:: https://codeclimate.com/github/Maddonix/ukw-intelli-store/badges/gpa.svg
   :target: https://codeclimate.com/github/Maddonix/ukw-intelli-store
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

.. |commits-since| image:: https://img.shields.io/github/commits-since/Maddonix/ukw-intelli-store/v0.0.1.svg
    :alt: Commits since latest release
    :target: https://github.com/Maddonix/ukw-intelli-store/compare/v0.0.1...master


.. |scrutinizer| image:: https://img.shields.io/scrutinizer/quality/g/Maddonix/ukw-intelli-store/master.svg
    :alt: Scrutinizer Status
    :target: https://scrutinizer-ci.com/g/Maddonix/ukw-intelli-store/


.. end-badges

Package to read and explore material consumption

* Free software: MIT license

Installation
============

::

    pip install ukw-intelli-store

You can also install the in-development version with::

    pip install https://github.com/Maddonix/ukw-intelli-store/archive/master.zip


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
