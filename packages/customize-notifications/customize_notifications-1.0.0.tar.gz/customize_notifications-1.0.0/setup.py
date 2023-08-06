#!/usr/bin/env python
# coding: utf-8

import setuptools

with open("README.md","r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='customize_notifications',
    version='1.0.0',
    author='renjun',
    author_email='jamesbond.ren@gmail.com',
    url='https://github.com/renjunok/customize-notifications-python-sdk',
    description='customize notifications python sdk',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
