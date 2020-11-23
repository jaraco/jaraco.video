.. image:: https://img.shields.io/pypi/v/skeleton.svg
   :target: `PyPI link`_

.. image:: https://img.shields.io/pypi/pyversions/skeleton.svg
   :target: `PyPI link`_

.. _PyPI link: https://pypi.org/project/skeleton

.. image:: https://github.com/jaraco/skeleton/workflows/Automated%20Tests/badge.svg
   :target: https://github.com/jaraco/skeleton/actions?query=workflow%3A%22Automated+Tests%22
   :alt: Automated Tests

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/psf/black
   :alt: Code style: Black
.. image:: https://img.shields.io/pypi/v/jaraco.video.svg
   :target: https://pypi.org/project/jaraco.video

.. image:: https://img.shields.io/pypi/pyversions/jaraco.video.svg

.. .. image:: https://img.shields.io/travis/jaraco/jaraco.video/master.svg
..    :target: https://travis-ci.org/jaraco/jaraco.video

.. image:: https://img.shields.io/appveyor/ci/jaraco/jaraco-video/master.svg
   :target: https://ci.appveyor.com/project/jaraco/jaraco-video/branch/master

.. .. image:: https://readthedocs.org/projects/jaracovideo/badge/?version=latest
..    :target: https://jaracovideo.readthedocs.io/en/latest/?badge=latest

``jaraco.video`` implements a framegrabber inteface for Windows Video Capture
devices.

``jaraco.video`` is a port of the `VideoCapture module
<http://videocapture.sourceforge.net/>`_ in pure Python using ctypes
and comtypes.

`jaraco.video` is designed to run on Python 2.7+, including Python 3,
and including 32-bit and 64-bit versions of Python.

Usage
-----

``jaraco.video`` includes a console script "save-frame", which
locates the first video capture device and saves a single frame
to disk as "test.jpg". The command may also be invoked thus::

    python -m jaraco.video.capture

This example usage can be seen in the function
``jaraco.video.capture:save_frame``.
