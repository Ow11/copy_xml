#!/usr/bin/env python3

from setuptools import setup


setup(
    name='pycopy_xml',
    version='1.0',
    description='A tool for copying files passed via xmls',
    long_description='A tool for copying files passed via xmls',
    classifiers=[
      'Programming Language :: Python :: 3.9',
    ],
    keywords='copy xml',
    url='https://github.com/Ow11/copy_xml',
    install_requires=[
        'tap.py',
        'setuptools'
    ],
    include_package_data=True,
    zip_safe=False,
    packages=[
        'package_pycopy',
    ],
    entry_points={
        'console_scripts': [
            'pycopy_xml=package_pycopy.pycopy_xml:main',
        ],
    },
)
