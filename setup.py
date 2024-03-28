import os
from setuptools import setup, find_namespace_packages

HERE = os.path.abspath(os.path.dirname(__file__))


def get_version():
    version_locals = {}
    version_file_path = os.path.join(HERE, "AreaOfShapesLib", "areaOfShapesLib", "version.py")
    with open(version_file_path, 'r') as f:
        exec(f.read(), None, version_locals)
    return version_locals['__version__']


with open(os.path.join(HERE, 'readme.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='AreaOfShapesLib',
    version=get_version(),
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
)
