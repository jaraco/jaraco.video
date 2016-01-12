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

You can install it with ``easy_install jaraco.video``, or from the
`mercurial repository
<http://bitbucket.org/jaraco/jaraco.video/get/tip.zip#egg=jaraco.video-dev>`_
with
``easy_install jaraco.video==dev``.

`jaraco.video` is designed to run on Python 2.6+, including Python 3,
and including 32-bit and 64-bit versions of Python.

Installation
------------

``jaraco.video`` depends on several libraries including Pillow and comtypes.
If the package is installed using `setuptools
<https://pythonhosted.org/setuptools>`_ or `pip
<https://pythonhosted.org/pip>`_, those dependencies should be installed
automatically.

There are `some <https://sourceforge.net/p/comtypes/bugs/27/>`_
`issues <https://sourceforge.net/p/comtypes/bugs/30/>`_ that prevent the
released version of comtypes from installing properly. Until those issues are
fixed, work around them by first installing comtypes manually from jaraco's
mirror::

    easy_install https://bitbucket.org/jaraco/comtypes/get/b85ebb181c17.zip

Usage
-----

``jaraco.video`` includes a console script "save-frame", which
locates the first video capture device and saves a single frame
to disk as "test.jpg". The command may also be invoked thus::

    python -m jaraco.video.capture

This example usage can be seen in the function
``jaraco.video.capture:save_frame``.
