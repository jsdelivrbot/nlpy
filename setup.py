#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

from setuptools import find_packages, setup
from konlpy import __version__

with open('requirements.txt', 'r') as f:
    requirements = f.read().splitlines()

setup(name='konlpy',
    version=__version__,
    description='Korean morpheme analyzer on Python',
    url='http://github.com/e9t/konlpy',
    author='Lucy Park',
    author_email='me@lucypark.kr',
    license='Apache v2.0',
    packages=find_packages(),
    package_data={'konlpy': [
        'data/*/*.txt',
        'java/conf/plugin/*/*/*.json',
        'java/data/*/*',
        'java/jhannanum-0.8.4.jar', 'java/bin/kr/lucypark/jhannanum/*/*.class',
        'java/kkma-2.0.jar', 'java/bin/kr/lucypark/kkma/*.class',
        ]},
    install_requires=requirements,
    zip_safe=False)
