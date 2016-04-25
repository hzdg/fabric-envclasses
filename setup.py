#/usr/bin/env python
import codecs
import os
import sys
from setuptools import setup, find_packages


read = lambda filepath: codecs.open(filepath, 'r', 'utf-8').read()

setup(
    name='fabenv',
    version='0.1.0',
    description='Use classes to declare fabric environment tasks.',
    long_description=read(os.path.join(os.path.dirname(__file__), 'README.rst')),
    author='Matthew Tretter',
    author_email='matthew@exanimo.com',
    url='http://github.com/hzdg/fabric-envclasses/',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=[
        'Fabric>=1.4.1',
    ],
)
