# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='github_crawler',
    version='0.1.0',
    description='This package allow a user to start the process of crawler the GitHub webpage after search for a list of keywords.',
    long_description=readme,
    author='Manu Molina',
    author_email='manu.molinam@gmail.com',
    url='https://github.com/manumolina/github_crawler',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
