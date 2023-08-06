#!/usr/bin/env python3
import os
import re
import shutil
import sys
from io import open

from setuptools import find_packages, setup

CURRENT_PYTHON = sys.version_info[:2]
REQUIRED_PYTHON = (3, 5)

# This check and everything above must remain compatible with Python 2.7.
if CURRENT_PYTHON < REQUIRED_PYTHON:
	sys.stderr.write("""
==========================
Unsupported Python version
==========================
This version of JSL Django Sitemap requires Python {}.{}, but you're trying
to install it on Python {}.{}.
This may be because you are using a version of pip that doesn't
understand the python_requires classifier. Make sure you
have pip >= 9.0 and setuptools >= 24.2, then try again:
    $ python -m pip install --upgrade pip setuptools
    $ python -m pip install jsl_django_sitemap
"
""".format(*(REQUIRED_PYTHON + CURRENT_PYTHON)))
	sys.exit(1)


def read(f):
	return open(f, 'r', encoding='utf-8').read()


def get_version(package):
	"""
	Return package version as listed in `__version__` in `init.py`.
	"""
	return "1.0.0"


version = get_version('jsl_django_sitemap')

if sys.argv[-1] == 'publish':
	if os.system("pip freeze | grep twine"):
		print("twine not installed.\nUse `pip install twine`.\nExiting.")
		sys.exit()
	os.system("python setup.py sdist bdist_wheel")
	if os.system("twine check dist/*"):
		print("twine check failed. Packages might be outdated.")
		print("Try using `pip install -U twine wheel`.\nExiting.")
		sys.exit()
	os.system("twine upload dist/*")
	print("You probably want to also tag the version now:")
	print("  git tag -a %s -m 'version %s'" % (version, version))
	print("  git push --tags")
	shutil.rmtree('dist')
	shutil.rmtree('build')
	shutil.rmtree('jsl_django_sitemap.egg-info')
	sys.exit()

setup(
	name='jsl_django_sitemap',
	version=version,
	url='https://github.com/JSoftwareLabs/jsl_django_sitemap',
	license='MTI',
	description="JSL Django Sitemap is a Django app to which iterates over all the url patterns in your main Django project and creates a ready to use sitemap. The sitemap.xml is useful in crawlers such as Google, Bing, Yahoo.We hope you like our app! Leave a star on our github repository. Thanks!",
	long_description=read('README.rst'),
	long_description_content_type='text/markdown',
	author='Dhananjay Joshi',
	author_email='info@jsoftwarelabs.com',  # SEE NOTE BELOW (*)
	keywords=['JSoftwareLabs', 'JSL Django sitemap', 'sitemap', 'Django sitemap'],
	packages=find_packages(exclude=['tests*']),
	include_package_data=True,
	install_requires=["django>=2.2"],
	python_requires=">=3.5",
	zip_safe=False,
	classifiers=[
		'Development Status :: 5 - Production/Stable',
		'Environment :: Web Environment',
		'Framework :: Django',
		'Framework :: Django :: 2.2',
		'Framework :: Django :: 3.0',
		'Framework :: Django :: 3.1',
		'Intended Audience :: Developers',
		'License :: OSI Approved :: BSD License',
		'Operating System :: OS Independent',
		'Programming Language :: Python',
		'Programming Language :: Python :: 3',
		'Programming Language :: Python :: 3.5',
		'Programming Language :: Python :: 3.6',
		'Programming Language :: Python :: 3.7',
		'Programming Language :: Python :: 3.8',
		'Programming Language :: Python :: 3.9',
		'Programming Language :: Python :: 3 :: Only',
		'Topic :: Internet :: WWW/HTTP',
	],
	project_urls={
		'Funding': 'https://fund.django-rest-framework.org/topics/funding/',
		'Source': 'https://github.com/encode/django-rest-framework',
	},
)
