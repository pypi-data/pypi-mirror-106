# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

with open('requirements.txt') as f:
    requirements = f.read().splitlines()
setup(
    name='orbitsim',
    version='0.0.1b',
    description='3D orbit simulation visualisation tool',
    long_description=readme,
    author='Alexander Minchin',
    author_email='alexander.w.minchin@gmail.com',
    url='https://github.com/alexander-minchin/orbitsim',
    license=license,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={'':'src'},
    packages=find_packages(where="src",exclude=('tests', 'docs')),
    install_requires=requirements,
    python_requires=">=3.6"
)