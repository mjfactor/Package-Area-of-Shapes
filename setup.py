import os
from setuptools import setup, find_namespace_packages
from version import __version__ as version
import pathlib
# hi
HERE = os.path.abspath(os.path.dirname(__file__))

long_description = (pathlib.Path(HERE) / "readme.md").read_text()

setup(
    name='AreaOfShapesLib',
    version=version,
    packages=find_namespace_packages(),
    url='https://github.com/mjfctor/ArithmeticOperations',
    license='MIT',
    author='mjfctor',
    author_email='emjayfactor@gmail.com',
    description='A Python library for performing arithmetic operations related to the area of different shapes',
    long_description=long_description,
    long_description_content_type='text/markdown',
    install_requires=[
        # Add dependencies here if any
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    python_requires='>=3.6',
    package_data={'': ['readme.md']},  # Include README.md in the package
    include_package_data=True  # Include package data files specified in MANIFEST.in
)
