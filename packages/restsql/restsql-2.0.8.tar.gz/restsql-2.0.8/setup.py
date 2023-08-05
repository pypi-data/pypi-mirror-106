#! /usr/bin/env python
# -*- coding: utf-8 -*-
import setuptools

setuptools.setup(
    name='restsql',
    version='2.0.8',
    description=(
        'RestSQL库。用json与数据库交互。'
    ),
    url='https://git.code.oa.com/tencent_cloud_mobile_tools/RestSQL',
    long_description='restsql',
    author="oliverdding",
    author_email='oliverdding@tencent.com',
    maintainer='oliverdding',
    maintainer_email='oliverdding@tencent.com',
    license='MIT License',
    packages=['restsql', 'restsql.config'],
    install_requires=[
        'numpy==1.20.3',
        'pandas==1.2.4',
        'pyyaml==5.4.1',
        'psycopg2-binary==2.8.6',
    ],
    classifiers=[
        "Programming Language :: Python",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
