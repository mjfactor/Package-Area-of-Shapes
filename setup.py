import os
import re
import subprocess

from setuptools import setup, find_packages

from codecs import open
from os import path

HERE = path.abspath(path.dirname(__file__))


# Get the version from the version.py file
def get_version():
    version_locals = {}
    with open("areaOfShapesLib/version.py", 'r') as f:
        exec(f.read(), None, version_locals)
    return version_locals['__version__']


# Use the absolute path to the readme.md file
readme_path = os.path.join(HERE, 'readme.md')

# Check if the readme.md file exists
if os.path.exists(readme_path):
    with open(readme_path, encoding='utf-8') as f:
        long_description = f.read()
else:
    long_description = ''  # Default description if readme.md does not exist

# ...

setup(
    name='AreaOfShapesLib',
    version="v3.4",
    packages=find_packages(),
    url='https://github.com/mjfctor/ArithmeticOperations',
    license='MIT',
    author='mjfctor',
    author_email='emjayfactor@gmail.com',
    description='A Python library for performing arithmetic operations related to the area of different shapes',
    long_description=long_description,  # Use the long_description variable
    long_description_content_type='text/markdown',
    install_requires=[

    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],

)
