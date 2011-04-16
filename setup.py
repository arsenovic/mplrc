#!/usr/bin/env python

import ez_setup
ez_setup.use_setuptools()
from setuptools import setup, find_packages

setup(name='mplrc',
	version='0.01',
	license='gpl',
	description='Matplotlib configurations',
	author='Alex Arsenovic',
	author_email='arsenovic@virginia.edu',
	#url='http://code.google.com/p/mwavepy/',
	packages=find_packages(),
	install_requires = [
		'matplotlib',
		],
	)
