# -*- coding: utf-8 -*-
import setuptools
from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="evansung",
    version="1.5",
    author="evansung",
    author_email="evansung@outlook.com",
    description="evansung yyds",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'pillow'
    ],
    python_requires='>=3'
)
