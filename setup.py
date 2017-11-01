#!/usr/bin/env python

from setuptools import setup


setup(
    name='css_classes',
    version='1.1',
    description='Simple python analog of npm package "classnames"',
    author='Ivan Larin',
    author_email='pentusha@gmail.com',
    license='MIT',
    url='https://github.com/Pentusha/css_classes',
    packages=['css_classes'],
    classifiers=(
        # As from https://pypi.python.org/pypi?:action=list_classifiers
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
    ),
    keywords='css class',
    python_requires='>=3.6',
)
