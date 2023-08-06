"""A setuptools based setup module.

See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

# To use a consistent encoding
from codecs import open
from os import path

# Always prefer setuptools over distutils
from setuptools import setup, find_packages

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
      name='conciliator-python',
      
      version='0.0.2',
      
      description="Python library for the Conciliator API",
      long_description=long_description,
            long_description_content_type='text/markdown',

      classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: Apache Software License",
            "Operating System :: OS Independent",
      ],

      keywords=['conciliator', 'client', 'api', 'python'],
      author='Dhatim',
      author_email='contact@dhatim.com',
      url='https://github.com/dhatim/conciliator-python',
      download_url = 'https://github.com/dhatim/conciliator-python/archive/refs/tags/0.0.2.tar.gz',
      license='Apache Software License',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      python_requires='>=3.6',
      install_requires=['requests', 'pyjwt'],
      entry_points={},
      test_suite="tests"
)
