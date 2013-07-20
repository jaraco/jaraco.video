from __future__ import print_function

def find_name(name):
	"For testing only; search for a name in the libraries"
	from comtypes.gen import DirectShowLib, DexterLib
	from ctypes import wintypes
	import comtypes
	for lib in DirectShowLib, DexterLib, wintypes, comtypes:
		res = [x for x in dir(lib) if name.lower() in x.lower()]
		if res:
			print('found {name} in {lib} as {items}'.format(
				items = ', '.join(res), **vars()))
