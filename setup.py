# Overzicht
# @bd0nd4lds
# See LICENSE for details

import sys
import re
from os import path
from setuptools import find_packages, setup

assert sys.version_info[0] == 3, "Overzicht requires Python 3."

VERSIONFILE = "overzicht/__init__.py"
ver_file = open(VERSIONFILE, "rt").read()
VSRE = r"^__version__ = ['\"]([^'\"]*)['\"]"
mo = re.search(VSRE, ver_file, re.M)

if mo:
    version = mo.group(1)
else:
    raise RuntimeError(
        "Unable to find version string in {}".format(VERSIONFILE))

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

requirements = []
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='overzicht',
    version=version,
    description='',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license="MIT",
    author='@bd0nd4lds',
    author_email='@bd0nd4lds',
    url='https://github.com/bd0n4lds/overzicht',
    keywords='',
    packages=find_packages(exclude=['tests']),
    install_requires=requirements,
    entry_points={'console_scripts': ['overzicht = overzicht.__main__:main']},
    classifiers=[
        'Topic :: Software Development :: Libraries',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
    ]
)
