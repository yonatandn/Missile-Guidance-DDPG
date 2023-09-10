#!/usr/bin/env python3
'''
Python distutils setup file for gym-bomber module.

Copyright (C) 2023 Yehonatan Dahan, Yogev Attias, Simon D. Levy

MIT License
'''

#from distutils.core import setup
from setuptools import setup

setup (name = 'gym_bomber',
    version = '0.1',
    install_requires = ['gymnasium', 'numpy'],
    description = 'Gym environment for guided bomb game',
    packages = ['gym_bomber', 'gym_bomber.envs'],
    author='Yehonatan Dahan, Yogev Attias',
    author_email='',
    url='https://github.com/simondlevy/gym-bomber',
    license='',
    platforms='Linux; Windows; OS X'
    )
