# -*- coding: utf-8 -*-
"""
:Author: Meenmo Kang
:Date: 2021. 5. 21.
"""
from setuptools import setup, find_packages

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()

setup(
    name='ksifteq',
    version='0.0.2', 
    description='KSIF API',
    long_description=long_description,
    author='KSIF Tech',
    author_email='meenmo@outlook.com',
    url='https://github.com/ksifteq/ksifteq',
    install_requires=[
        'numpy==1.20.3',
        'pandas==1.2.4',
        'PyQt5==5.15.4',
        'PyQt5-Qt5==5.15.2',
        'PyQt5-sip==12.9.0',
        'python-dateutil==2.8.1',
        'pytz==2021.1',
        'six==1.16.0',
        'dnspython==2.1.0',
        'pymongo==3.11.4',
    ],
    packages=find_packages(),
    keywords=['ksif', 'eFriend', 'KRX', 'derivatives'],
    python_requires='>=3.5',
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
