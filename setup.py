try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    description='Module to handle automatic variable naming, multiple files and some file acrobatics in python',
    long_description=long_description,
    author='daegontaven',
    url='https://github.com/daegontaven/filemapper',
    download_url='https://github.com/daegontaven/filemapper.git',
    author_email='admin@greycadet.com',
    version='0.1',
    license='GNU GENERAL PUBLIC LICENSE Version 3',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5'
    ],
    keywords='multiple file mapper variable',
    packages=find_packages(),
    name='filemapper'
)
