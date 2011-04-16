import os
import pkg_resources
import functools
import comtypes.client
import contextlib

def raises_error(callable, exception = Exception):
	try:
		callable()
	except exception:
		return True
	return False

def typelibs_generated():
	import_SG = functools.partial(
		__import__,
		'comtypes.gen.DexterLib', fromlist=['SampleGrabber']
	)
	return not raises_error(import_SG)

@contextlib.contextmanager
def directory_context(dir):
	orig = os.getcwd()
	os.chdir(dir)
	yield
	os.chdir(orig)

def generate_typelibs():
	req = pkg_resources.Requirement.parse('jaraco.video')
	fn = functools.partial(
		pkg_resources.resource_filename,
		req,
	)
	with directory_context(fn('DirectShow')):
		map(comtypes.client.GetModule, [
			'DirectShow.tlb',
			'DexterLib.tlb',
		])

if not typelibs_generated():
	generate_typelibs()
