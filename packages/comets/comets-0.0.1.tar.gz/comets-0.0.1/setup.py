"""
Copyright (c) Cosmo Tech.
Licensed under the MIT license.
"""


from setuptools import setup, find_packages

NAME = "comets"
VERSION = "0.0.1"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name=NAME,
    version=VERSION,
    author="Cosmo Tech",
    author_email="team.next@cosmotech.com",
    url="https://github.com/Cosmo-Tech/comets",
    keywords=[
        "CosmoTech",
        "comets",
        "Model Experimentation",
        "Uncertainty Analysis",
        "Sensibility Analysis",
        "Optimization",
    ],
    python_requires=">=3.6",
    install_requires=open("requirements.txt", "r").readlines(),
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    license="MIT License",
    description="Comets, the Cosmo Model Experimentation Toolbox, is a Python library for experimenting with numerical models and simulators",
    long_description=long_description,
    long_description_content_type="text/markdown",
)
