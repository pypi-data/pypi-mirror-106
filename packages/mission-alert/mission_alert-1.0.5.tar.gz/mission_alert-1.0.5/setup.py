#!/usr/bin/env python
# coding: utf-8

from setuptools import setup

setup(
    name='mission_alert',
    version='1.0.5',
    author='xanxus',
    author_email='123@123.com',
    url='https://github.com/Xanxus1111',
    description='alert mission complete in server through email',
    packages=['mission_alert'],
    install_requires=['PyEmail'],
    license='MIT',
    entry_points={
        'console_scripts': [
            'sendEmail=jujube_pill:sendEmail'
        ]
    }
)