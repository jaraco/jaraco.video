import contextlib
import functools
import importlib.resources
import os

import comtypes.client


def raises_error(callable, exception=Exception):
    try:
        callable()
    except exception:
        return True
    return False


def typelibs_generated():
    import_SG = functools.partial(
        __import__, 'comtypes.gen.DexterLib', fromlist=['SampleGrabber']
    )
    return not raises_error(import_SG)


@contextlib.contextmanager
def directory_context(dir):
    orig = os.getcwd()
    os.chdir(dir)
    yield
    os.chdir(orig)


def generate_typelibs():
    with directory_context(importlib.resources.files(__name__) / 'DirectShow'):
        list(
            map(
                comtypes.client.GetModule,
                [
                    'DirectShow.tlb',
                    'DexterLib.tlb',
                ],
            )
        )


if not typelibs_generated():
    generate_typelibs()
