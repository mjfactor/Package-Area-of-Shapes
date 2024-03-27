import os
import re
import subprocess

from setuptools import setup, find_packages

from codecs import open
from os import path

HERE = path.abspath(path.dirname(__file__))

latest_tag = (
    subprocess.run(['git', 'describe', '--tags'], stdout=subprocess.PIPE)
    .stdout.strip()
    .decode('utf-8')
)
if "-" in latest_tag:
    v, i, s = latest_tag.split("-")
    latest_tag = v + "+" + i + ".git" + s

assert "-" not in latest_tag
assert "." in latest_tag

with open(path.join(HERE, 'readme.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='AreaOfShapesLib',
    version=latest_tag,
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
