|version| |build| |coverage|

Simple python analog of npm package `classnames`_

Installation
============

Installation via Python pip::

    pip install css_classes


Usage
=====

.. code:: python

    >>> css_classes('btn btn-success')
    'btn btn-success'
    >>> css_classes('btn', {'btn-success': True, 'btn-cancel': False})
    'btn btn-success'
    >>> css_classes('btn', 'btn-success')
    'btn btn-success'
    >>> css_classes('btn', btn_success=True)
    'btn btn-success'
    >>> css_classes('btn', btn_success=True, underscore_as_dash=False)
    'btn btn_success'

.. _classnames: https://www.npmjs.com/package/classnames

.. |version| image:: http://badge.fury.io/py/css-classes.svg
   :alt: PyPI version
   :target: http://badge.fury.io/py/css-classes
.. |build| image:: http://secure.travis-ci.org/Pentusha/css_classes.png?branch=master
   :alt: Build status
   :target: https://travis-ci.org/Pentusha/css_classes
.. |coverage| image:: http://coveralls.io/repos/Pentusha/cinemate/badge.svg?branch=master
   :alt: Tests Coverage
   :target: https://coveralls.io/r/Pentusha/css_classes
.. |wheel| image:: https://img.shields.io/pypi/wheel/css_classes.svg?style=flat
   :alt: Wheel Status
   :target: https://pypi.python.org/pypi/css_classes/
