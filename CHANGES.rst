v4.0.2
======

* Switch to PEP 420 namespace package.

v4.0.1
======

* Cleanup README.

v4.0.0
======

* #9: In DexterLib, once again the media type is ``tag_AMMediaType``.
* Require Python 3.6 or later.

3.0
===

Switch to `pkgutil namespace technique
<https://packaging.python.org/guides/packaging-namespace-packages/#pkgutil-style-namespace-packages>`_
for the ``jaraco`` namespace.

2.2.1
=====

* #9: The name was meant to be ``_AMMediaType``.

2.2
===

* #9: Expect ``AMMediaType`` in DexterLib and not ``tag_AMMediaType``.
  Cause for the change is unknown.

2.1.1
=====

* #8: For compatibility with later Pillow versions, use ``frombytes``.

2.1
===

* Refreshed package.

2.0
===

* Dropped support for Python 2.6.
* Moved hosting to Github.

1.3
===

* Use ``jaraco.structures`` instead of ``jaraco.util``.

1.2.1
=====

* Fixed several errors in the code due to untested refactorings for Python 3
  support. The code now runs properly under Python 3.
* #3: Added notes about deploying the latest version of comtypes with bug
  fixes from jaraco's mirror.

1.2
===

* #1: Require jaraco.util for bitutil, which has progressed with better Python
  3 support.
* #2: Added a hard dependency on Pillow for imaging. The library is pretty
  useless without it. If there is a use-case out there for using the library
  without Pillow, please file a request ticket.

1.1
===

* Moved typelibs so they will be included with the build.
* Fixed ImportError on Python 3.
* Added readme.

1.0
===

* First non-dev release. Typelibs are included and comtypes libs are
  generated automatically.
