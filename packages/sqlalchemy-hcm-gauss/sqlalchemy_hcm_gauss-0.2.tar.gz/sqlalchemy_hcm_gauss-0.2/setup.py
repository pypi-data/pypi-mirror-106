#!/usr/bin/env python
"""
Setup for SQLAlchemy backend for DM
"""
from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup_params = dict(
    name="sqlalchemy_hcm_gauss",
    version='0.2',
    description="SQLAlchemy dialect for hcm special for open gauss",
    author="tangrj",
    author_email="tangrj@inspur.com",
    keywords='gauss hcm SQLAlchemy',
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        "sqlalchemy.dialects":
            ["HCMgauss = sqlalchemy_gs.psycopg2:PGDialect_psycopg2", "HCMgauss.psycopg2 = sqlalchemy_gs.psycopg2:PGDialect_psycopg2"]
    },
    install_requires=['sqlalchemy==1.3.13'],
)

if __name__ == '__main__':
    setup(**setup_params)
