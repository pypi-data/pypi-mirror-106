"""Builds the library.

To upload to cheese:

sudo python3  setup.py sdist bdist_wheel
sudo pip3 install twine
twine upload dist/*
"""
from setuptools import find_packages, setup

setup(
    name="dolon",
    description="A performance tracer application.",
    version='0.0.15',
    packages=find_packages(),
    install_requires=[
        "asyncpg"
    ],
)
