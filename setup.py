# -*- coding: UTF-8 -*-

""" Setup script for building jaraco.windows distribution

Copyright © 2010 Jason R. Coombs
"""

from setuptools import setup, find_packages

__author__ = 'Jason R. Coombs <jaraco@jaraco.com>'
__version__ = '$Rev$'[6:-2]
__svnauthor__ = '$Author$'[9:-2]
__date__ = '$Date$'[7:-2]

name = 'jaraco.video'

setup (name = name,
		version = '1.0',
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
			"Programming Language :: Python",
		],
		entry_points = dict(
			console_scripts = [
				'save-frame = jaraco.video.capture:save_frame',
			],
		),
		install_requires=[
		],
		extras_require = {
		},
		dependency_links = [
		],
		tests_require=[
			'nose>=0.10',
		],
		test_suite = "nose.collector",
	)
