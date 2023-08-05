========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis| |appveyor| |requires|
        | |coveralls| |codecov|
        | |codeclimate|
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|
.. |docs| image:: https://readthedocs.org/projects/ukw_fax/badge/?style=flat
    :target: https://ukw_fax.readthedocs.io/
    :alt: Documentation Status

.. |travis| image:: https://api.travis-ci.com/Maddonix/ukw_fax.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.com/github/Maddonix/ukw_fax

.. |appveyor| image:: https://ci.appveyor.com/api/projects/status/github/Maddonix/ukw_fax?branch=master&svg=true
    :alt: AppVeyor Build Status
    :target: https://ci.appveyor.com/project/Maddonix/ukw_fax

.. |requires| image:: https://requires.io/github/Maddonix/ukw_fax/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/Maddonix/ukw_fax/requirements/?branch=master

.. |coveralls| image:: https://coveralls.io/repos/Maddonix/ukw_fax/badge.svg?branch=master&service=github
    :alt: Coverage Status
    :target: https://coveralls.io/r/Maddonix/ukw_fax

.. |codecov| image:: https://codecov.io/gh/Maddonix/ukw_fax/branch/master/graphs/badge.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/Maddonix/ukw_fax

.. |codeclimate| image:: https://codeclimate.com/github/Maddonix/ukw_fax/badges/gpa.svg
   :target: https://codeclimate.com/github/Maddonix/ukw_fax
   :alt: CodeClimate Quality Status

.. |version| image:: https://img.shields.io/pypi/v/ukw-fax.svg
    :alt: PyPI Package latest release
    :target: https://pypi.org/project/ukw-fax

.. |wheel| image:: https://img.shields.io/pypi/wheel/ukw-fax.svg
    :alt: PyPI Wheel
    :target: https://pypi.org/project/ukw-fax

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/ukw-fax.svg
    :alt: Supported versions
    :target: https://pypi.org/project/ukw-fax

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/ukw-fax.svg
    :alt: Supported implementations
    :target: https://pypi.org/project/ukw-fax

.. |commits-since| image:: https://img.shields.io/github/commits-since/Maddonix/ukw_fax/v0.0.2.svg
    :alt: Commits since latest release
    :target: https://github.com/Maddonix/ukw_fax/compare/v0.0.2...master



.. end-badges

Package to read outlook mails and extract attached .tifs to fspecific folder structure. [D[D[D[D[D[D[D[

* Free software: MIT license

Installation
============

::

    pip install ukw-fax

You can also install the in-development version with::

    pip install https://github.com/Maddonix/ukw_fax/archive/master.zip


Documentation
=============


https://ukw_fax.readthedocs.io/


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
