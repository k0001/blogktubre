#!/usr/bin/env python
# -*- coding: utf8 -*-

import distribute_setup
distribute_setup.use_setuptools()

from setuptools import setup, find_packages


setup(
    name = "blogktubre",
    version = "0.1dev",
    description = u"Minimal blogging platform built with Flask",
    url = u"https://github.com/k0001/blogktubre",
    author = u"Renzo Carbonara",
    author_email = u"blogktubre@k0001.org",
    license = u"BSD",

    zip_safe = False,
    packages = find_packages(),
    include_package_data = True,
    scripts = [
        'scripts/blogktubre',
    ],

    install_requires = [
        'Flask==0.6.1'
    ],

    classifiers = [
        "Development Status :: 2 - Pre-Alpha",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
    ]
)

