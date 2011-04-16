# -*- coding: UTF-8 -*-

"""
Setup script for building jaraco.video distribution

Copyright © 2010-2011 Jason R. Coombs
"""

from setuptools import find_packages

__author__ = 'Jason R. Coombs <jaraco@jaraco.com>'

name = 'jaraco.video'

setup_params = dict(
	name = name,
	use_hg_version=dict(increment='1.0'),
	description = 'A pure-python framegrabber for Windows',
	#long_description = open('docs/index.txt').read().strip(),
	author = 'Jason R. Coombs',
	author_email = 'jaraco@jaraco.com',
	url = 'http://pypi.python.org/pypi/'+name,
	packages = find_packages(exclude=['tests']),
	zip_safe=True,
	namespace_packages = ['jaraco',],
	license = 'MIT',
	classifiers = [
		"Development Status :: 4 - Beta",
		"Intended Audience :: Developers",
		"Programming Language :: Python :: 2",
		"Programming Language :: Python :: 3",
	],
	entry_points = dict(
		console_scripts = [
			'save-frame = jaraco.video.capture:save_frame',
		],
	),
	install_requires=[
		'comtypes',
	],
	extras_require = {
		'imaging': 'PIL',
	},
	dependency_links = [
	],
	setup_requires=[
		'hgtools',
	],
	use_2to3=True,
)

if __name__ == '__main__':
	from setuptools import setup
	setup(**setup_params)
