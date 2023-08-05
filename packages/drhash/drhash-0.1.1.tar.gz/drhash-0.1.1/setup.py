#!/usr/bin/env python
# coding: utf-8

from setuptools import setup, find_packages, Extension


#cws_cplusplus = Extension('./drhash/cpluspluslib/cws_fingerprints', sources=['./drhash/cpluspluslib/cws_fingerprints.cpp'])
#haeupler_cplusplus = Extension('./drhash/cpluspluslib/haeupler_expandset', sources=['./drhash/cpluspluslib/haeupler_expandset.cpp'])
#gollapudi1_cplusplus = Extension('./drhash/cpluspluslib/gollapudi1_fingerprints', sources=['./drhash/cpluspluslib/gollapudi1_fingerprints.cpp'])
#haveliwala_cplusplus = Extension('./drhash/cpluspluslib/haveliwala_expandset', sources=['./drhash/cpluspluslib/haveliwala_expandset.cpp'])


setup(
    name='drhash',
    version='0.1.1',
    author='Wei Wu',
    author_email='william.third.wu@gmail.com',
    url='https://github.com/drhash-cn',
    description='drhash is a software package for data representation via similarity-preserved hashing algorithms',
    packages=find_packages(),
    install_requires=['numpy>=1.15.0', 'scipy>=1.1.0'],
    # add an extension module named 'wmh' to the package
    # install_requires=['numpy>=1.15.0', 'scipy>=1.1.0'],
    #ext_modules=[cws_cplusplus, haeupler_cplusplus, gollapudi1_cplusplus, haveliwala_cplusplus],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)