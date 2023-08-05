#!/usr/bin/env python3

from setuptools import setup, find_packages

# read the contents of your README file
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

classifiers = [
    "Development Status :: 5 - Production/Stable",
    "Operating System :: Microsoft :: Windows :: Windows 10",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3",
]

setup(
    name="mrpeace",
    version="1.1.5",
    description="Basic Cli",
    url="https://github.com/claudiolau/MrPeace",
    packages=find_packages(),
    include_package_date=True,
    author="Claudio Lau",
    author_email="claudio.lau12@gmail.com",
    license="Apache 2.0",
    classifiers=classifiers,
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=["click"],
    entry_points="""
        [console_scripts]
        mrpeace=mrpeace.cli:cli
    """,
)
