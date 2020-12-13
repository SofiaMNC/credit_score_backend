# coding: utf-8

import sys
from setuptools import setup, find_packages

NAME = "swagger_server"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["connexion"]

setup(
    name=NAME,
    version=VERSION,
    description="Credit Score Predictor",
    author_email="contact@madimedia.pro",
    url="",
    keywords=["Swagger", "Credit Score Predictor"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['swagger/swagger.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['swagger_server=swagger_server.__main__:main']},
    long_description="""\
    This is an API to fetch a credit score for a loan seeker. The credit scores go from 0 to 10, 10 indicating a prospect most likely to reimburse its loan.
    """
)
