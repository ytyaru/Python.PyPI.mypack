#!/usr/bin/env python
# -*- coding: utf-8 -*-
import setuptools
from os import path
import re

package_name = 'mypack'
description = 'Publish the package with PyPI.'
root_dir = path.abspath(path.dirname(__file__))

with open("README.md", "r") as f:
    long_description = f.read()

with open(path.join(root_dir, package_name, '__init__.py')) as f:
    init_text = f.read()
    version = re.search(r'__version__\s*=\s*[\'\"](.+?)[\'\"]', init_text).group(1)
    license = re.search(r'__license__\s*=\s*[\'\"](.+?)[\'\"]', init_text).group(1)
    author = re.search(r'__author__\s*=\s*[\'\"](.+?)[\'\"]', init_text).group(1)
    author_email = re.search(r'__author_email__\s*=\s*[\'\"](.+?)[\'\"]', init_text).group(1)
    url = re.search(r'__url__\s*=\s*[\'\"](.+?)[\'\"]', init_text).group(1)

assert version
assert license
assert author
assert author_email
assert url

setuptools.setup(
    name=package_name,
    version=version,
    author=author,
    author_email=author_email,
    description=description,
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords="pypi,pip,practice,test,package,module",
    url="https://github.com/ytyaru/Python.PyPI.mypack",
#    download_url="",
    packages=setuptools.find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: Utilities",
    ],
    python_requires='>=2.7',
)
