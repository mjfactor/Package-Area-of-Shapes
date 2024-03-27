import subprocess
import re
from setuptools import setup, find_packages

# Get the latest tag in Git
latest_tag = subprocess.getoutput('git describe --tags --abbrev=0')

# Parse the tag to get the version number
match = re.search(r'v(\d+\.\d+\.\d+)', latest_tag)
if match is None:
    raise ValueError("No version number found in Git tag")
version = match.group(1)

# Your existing setup.py code
setup(
    name='AreaOfShapesLib',
    version=version,  # Use the version number from the Git tag
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