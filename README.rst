jaraco.video
============

.. contents::

Overview
--------

``jaraco.video`` implements a framegrabber inteface for Windows Video Capture
devices.

Status and License
------------------

``jaraco.video`` is a port of the `VideoCapture module
<http://videocapture.sourceforge.net/>`_ in pure Python using ctypes
and comtypes.

``jaraco.video`` is maintained by Jason R. Coombs.  It is licensed under
an `MIT-style permissive license
<http://www.opensource.org/licenses/mit-license.php>`_.

`jaraco.video` is designed to run on Python 2.7+, including Python 3,
and including 32-bit and 64-bit versions of Python.

Installation
------------

You can install it with ``easy_install jaraco.video`` or
``pip install jaraco.video``.

``jaraco.video`` depends on several libraries including Pillow and comtypes.
If the package is installed using `setuptools
<https://pythonhosted.org/setuptools>`_ or `pip
<https://pythonhosted.org/pip>`_, those dependencies should be installed
automatically.

Usage
-----

``jaraco.video`` includes a console script "save-frame", which
locates the first video capture device and saves a single frame
to disk as "test.jpg". The command may also be invoked thus::

    python -m jaraco.video.capture

This example usage can be seen in the function
``jaraco.video.capture:save_frame``.
