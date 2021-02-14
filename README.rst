.. image:: https://img.shields.io/pypi/v/jaraco.video.svg
   :target: `PyPI link`_

.. image:: https://img.shields.io/pypi/pyversions/jaraco.video.svg
   :target: `PyPI link`_

.. _PyPI link: https://pypi.org/project/jaraco.video

.. image:: https://github.com/jaraco/jaraco.video/workflows/tests/badge.svg
   :target: https://github.com/jaraco/jaraco.video/actions?query=workflow%3A%22tests%22
   :alt: tests

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/psf/black
   :alt: Code style: Black

.. .. image:: https://readthedocs.org/projects/skeleton/badge/?version=latest
..    :target: https://skeleton.readthedocs.io/en/latest/?badge=latest

``jaraco.video`` implements a framegrabber inteface for Windows Video Capture
devices.

``jaraco.video`` is a port of the `VideoCapture module
<http://videocapture.sourceforge.net/>`_ in pure Python using ctypes
and comtypes.

Usage
-----

``jaraco.video`` includes a console script "save-frame", which
locates the first video capture device and saves a single frame
to disk as "test.jpg". The command may also be invoked thus::

    python -m jaraco.video.capture

This example usage can be seen in the function
``jaraco.video.capture:save_frame``.
