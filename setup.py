##!/usr/bin/env python

#import os
#from setuptools import setup


## Utility function to read the README file.
## Used for the long_description.  It's nice, because now 1) we have a top level
## README file and 2) it's easier to type in the README file than to put a raw
## string in below ...
#def read(fname):
    #return open(os.path.join(os.path.dirname(__file__), fname)).read()


#setup(
    #name="lib_py",
    #version="1.0",
    #author="Aman Abhishek Tiwari",
    #author_email="amanabt@iitk.ac.in",
    #description="My python library where you could find my "
    #"miscellaneous python codes",
    #license="GPLv3+",
    #keywords="utilities",
    #url="https://github.com/amanabt/lib_py",
    #packages=['lib_py'],
    #classifiers=[
        #"Development Status :: 3 - Alpha",
        #"Topic :: Software Development :: python",
        #"License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        #"Programming Language :: Python",
        #"Intended Audience :: Developers, Scientists",
        #"Natural Language :: English",
        #"Operating System :: OS Independent",
        #"Environment :: Console"
    #],
    #install_requires=[
        #'numpy',
        #'matplotlib',
        #'scipy'
    #],
    #extras_require={
        #'docs': ['sphinx', 'sphinx-argparse']
    #},
    #platforms='any',
    #entry_points={
        #'console_scripts': ['lib_py=lib_py.fourier:main'],
    #}
#)

from distutils.core import setup

setup(
    name='lib_py',
    version='0.1dev',
    packages=['lib_py',],
    author="Aman Abhishek Tiwari",
    author_email="amanabt@iitk.ac.in",
    description="My python library where you could find my "
    "miscellaneous python codes",
    license="GPLv3+",
    keywords="utilities",
    url="https://github.com/amanabt/pylib",

    long_description=open('README.md').read(),
)
