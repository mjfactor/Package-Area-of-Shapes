import os
import re
import subprocess

from setuptools import setup, find_packages

from codecs import open
from os import path

HERE = path.abspath(path.dirname(__file__))

# Get Latest Tag
git_describe_output = subprocess.check_output(["git", "describe", "--tags"]).strip().decode('utf-8')
# Extract the tag and the number of additional commits
match = re.match(r'(\d+\.\d+\.\d+)-(\d+)-g[a-f0-9]+', git_describe_output)
if match:
    # Use the tag as the version, and append the number of additional commits as a post-release segment
    version = f'{match.group(1)}.post{match.group(2)}'
else:
    # If the output does not match the expected format, use the whole output as the version
    version = git_describe_output

with open(path.join(HERE, 'readme.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='AreaOfShapesLib',
    version=version,
    packages=find_packages(),
    url='https://github.com/mjfctor/ArithmeticOperations',
    license='MIT',
    author='mjfctor',
    author_email='emjayfactor@gmail.com',
    description='A Python library for performing arithmetic operations related to the area of different shapes',
    long_description=open('readme.md').read(),
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