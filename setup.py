"""
This script is used to set up the Python package 'python-uds'. It includes information about the author, licensing,
and other metadata. The script reads the long description from the README file and sets up the package with necessary
details such as name, URL, author, dependencies, version, license, description, classifiers, etc. Importantly, it includes
the metadata required for packaging, such as packages to include, dependencies, license information, and other package
settings to properly distribute and share the 'python-uds' library. The script utilizes setuptools for the setup process.
"""
#!/usr/bin/env python

__author__ = "Richard Clubb"
__copyrights__ = "Copyright 2018, the python-uds project"
__credits__ = ["Richard Clubb"]

__license__ = "MIT"
__maintainer__ = "Richard Clubb"
__email__ = "richard.clubb@embeduk.com"
__status__ = "Development"


from setuptools import setup, find_packages


with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    # Needed to silence warnings (and to be a worthwhile package)
    name='python-uds',
    url='https://github.com/richClubb/python-uds',
    author='Richard Clubb',
    author_email='richard.clubb@embeduk.com',
    # Needed to actually package something
    packages=find_packages(exclude=["test", "test.*"]),
    # Needed for dependencies
    install_requires=['python-can>=3.0.0', 'python-lin>=0.1.0'],
    # *strongly* suggested for sharing
    version='1.1.0',
    # The license can be anything you like
    license='MIT',
    description='A library for interfacing with UDS using python',
    # We will also need a readme eventually (there will be a warning)
    # long_description=open('README.txt').read(),
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Operating System :: OS Independent"
    ],
    include_package_data=True
)
