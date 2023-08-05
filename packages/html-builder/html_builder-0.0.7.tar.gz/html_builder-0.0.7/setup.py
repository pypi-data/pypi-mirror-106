#!/usr/bin/env python
# coding: utf-8

from setuptools import setup

long_description = '''
# readme:

this is a package to create html with python language
though it will be used by myself, also you can use it.
'''
# python setup.py sdist upload
# twine upload dist/*


def get_readme():
    with open('README.md', 'r') as f:
        return ''.join(f.readlines())


setup(
    name='html_builder',
    version='0.0.7',
    author='normidar',
    author_email='normidar7@gmail.com',
    url='https://www.normidar.com',
    description=get_readme(),
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=[
        'html_builder',
        'html_builder.Body',
        'html_builder.Head',
        'html_builder.Body.Input'
    ],
    install_requires=[],
    entry_points={
        'console_scripts': []
    }
)
