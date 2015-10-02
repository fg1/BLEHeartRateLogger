#!/usr/bin/python

from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding = 'utf-8') as f:
    long_description = f.read()

setup(
    name = 'BLEHeartRateLogger',
    version = '0.1.0',
    description = 'A tool to log your heart rate using a Bluetooth low-energy (BLE) heart rate monitor (HRM).',
    long_description = long_description,
    url = 'https://github.com/fg1/BLEHeartRateLogger',
    author = 'fg1',
    license = 'BSD',

    classifiers = [
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
    ],

    keywords = 'bluetooth heart-rate logging',
    packages = find_packages(),
    install_requires = ['pexpect'],

    entry_points = {
        'console_scripts': [
            'BLEHeartRateLogger=BLEHeartRateLogger:cli',
        ],
    },
)
