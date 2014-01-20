# -*- coding: UTF-8 -*-

"""
Setup script for building jaraco.video distribution

Copyright © 2010-2014 Jason R. Coombs
"""

from setuptools import find_packages

__author__ = 'Jason R. Coombs <jaraco@jaraco.com>'

name = 'jaraco.video'

with open('README.txt') as readme_stream:
	readme = readme_stream.read()
with open('CHANGES.txt') as changes_stream:
	changes = changes_stream.read()

setup_params = dict(
	name = name,
	use_hg_version=dict(increment='0.1'),
	description = 'A pure-python framegrabber for Windows',
	long_description = '\n'.join((readme, changes)),
	author = 'Jason R. Coombs',
	author_email = 'jaraco@jaraco.com',
	url = 'https://bitbucket.org/jaraco/'+name,
	packages = find_packages(exclude=['tests']),
	include_package_data=True,
	zip_safe=True,
	namespace_packages = ['jaraco',],
	license = 'MIT',
	classifiers = [
		"Development Status :: 5 - Production/Stable",
		"Intended Audience :: Developers",
		"Operating System :: Microsoft :: Windows",
		"Programming Language :: Python :: 2.6",
		"Programming Language :: Python :: 2.7",
		"Programming Language :: Python :: 3",
		"Topic :: Multimedia :: Video :: Capture",
	],
	entry_points = dict(
		console_scripts = [
			'save-frame = jaraco.video.capture:save_frame',
		],
	),
	install_requires=[
		'comtypes',
		'jaraco.util',
		'Pillow',
	],
	extras_require = {
	},
	dependency_links = [
	],
	setup_requires=[
		'hgtools',
	],
)

if __name__ == '__main__':
	from setuptools import setup
	setup(**setup_params)
