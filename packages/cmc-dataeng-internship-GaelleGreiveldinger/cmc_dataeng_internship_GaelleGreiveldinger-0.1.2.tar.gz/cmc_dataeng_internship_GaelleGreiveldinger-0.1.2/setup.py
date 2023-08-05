# -*- coding: utf-8 -*-
"""
Created on Mon May 17 22:35:44 2021

@author: Gaëlle Greiveldinger
"""

from setuptools import setup, find_packages

with open('README.md') as readme_file:
    README = readme_file.read()

setup_args = dict(
    name='cmc_dataeng_internship_GaelleGreiveldinger',
    version='0.1.2',
    description='Package for cmc_dataeng_internship_exercise',
    long_description_content_type="text/markdown",
    long_description=README,
    license='MIT',
    packages=find_packages(),
    author='Gaëlle Greiveldinger',
)

install_requires = [
]

if __name__ == '__main__':
    setup(**setup_args, install_requires=install_requires)