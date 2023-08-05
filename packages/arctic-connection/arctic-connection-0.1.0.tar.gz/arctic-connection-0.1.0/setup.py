#!/usr/bin/env python

from setuptools import setup

setup(
    name='arctic-connection',
    version='0.1.0',
    author='Louis-Alexis Duvief',
    author_email='louisalexis.dubief@gmail.com',
    packages=['arctic_connection'],
    license='LICENSE',
    description='A wrapper arround man-group arctic python package',
    long_description=open('README.md').read(),
    install_requires=[
        "pandas==1.1",
         "arctic",
    ]
)
