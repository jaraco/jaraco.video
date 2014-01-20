.. -*- restructuredtext -*-

============
jaraco.video
============

.. contents::

Status and License
------------------

``jaraco.video`` is a port of the `VideoCapture module
<http://videocapture.sourceforge.net/>`_ in pure Python using ctypes
and comtypes.

``jaraco.video`` is maintained by Jason R. Coombs.  It is licensed under
an `MIT-style permissive license
<http://www.opensource.org/licenses/mit-license.php>`_.

You can install it with ``easy_install jaraco.video``, or from the
`mercurial repository
<http://bitbucket.org/jaraco/jaraco.video/get/tip.zip#egg=jaraco.video-dev>`_
with
``easy_install jaraco.video==dev``.

`jaraco.video` is designed to run on Python 2.5+, including Python 3,
and including 32-bit and 64-bit versions of Python.

Issues
------

Although the package currently installs on Python 3, there is currently
no supported version of PIL for Python 3, so only raw bitmap data will
be available (no JPEG support, etc).

Usage
-----

`jaraco.video` includes a console script "save-frame", which
locates the first video capture device and saves a single frame
to disk as "test.jpg". The command may also be invoked thus::

    python -m jaraco.video.capture

This example usage can be seen in the function
`jaraco.video.capture:save_frame`.
