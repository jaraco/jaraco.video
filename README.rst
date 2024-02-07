.. image:: https://img.shields.io/pypi/v/jaraco.video.svg
   :target: https://pypi.org/project/jaraco.video

.. image:: https://img.shields.io/pypi/pyversions/jaraco.video.svg

.. image:: https://github.com/jaraco/jaraco.video/actions/workflows/main.yml/badge.svg
   :target: https://github.com/jaraco/jaraco.video/actions?query=workflow%3A%22tests%22
   :alt: tests

.. image:: https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/charliermarsh/ruff/main/assets/badge/v2.json
    :target: https://github.com/astral-sh/ruff
    :alt: Ruff

.. .. image:: https://readthedocs.org/projects/PROJECT_RTD/badge/?version=latest
..    :target: https://PROJECT_RTD.readthedocs.io/en/latest/?badge=latest

.. image:: https://img.shields.io/badge/skeleton-2024-informational
   :target: https://blog.jaraco.com/skeleton

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
