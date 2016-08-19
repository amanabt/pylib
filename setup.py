#!/usr/bin/env python

import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="py_lib",
    version="2.0",
    author="Aman Abhishek Tiwari",
    author_email="amanabt@iitk.ac.in",
    description="My python library where you could find my "
    "miscellaneous python codes",
    license="GPLv3+",
    keywords="utilities",
    url="https://github.com/amanabt/pylib",
    packages=['py_lib'],
    long_description=read('README.rst'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Education",
        "Topic :: Scientific/Engineering",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Programming Language :: Python :: 3.5",
        "Operating System :: OS Independent",
        "Natural Language :: English",
        "Environment :: Console"
    ],
    install_requires=[
        'numpy',
        'matplotlib',
        'scipy'
    ],
    extras_require={
        'docs': ['sphinx', 'sphinx-argparse']
    },
    platforms='any',
    entry_points={
        'console_scripts': ['py_lib=py_lib.fourier:main'],
    }
)
