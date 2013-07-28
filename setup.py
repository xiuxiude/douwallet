#!/usr/bin/env python

from setuptools import setup, find_packages


setup(
    name="douwallet",
    version="0.1.0.dev",
    packages=find_packages(excludes=["tests"]),
)
