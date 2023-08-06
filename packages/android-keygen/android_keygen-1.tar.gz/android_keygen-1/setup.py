import sys
from setuptools import setup, find_packages

from constants import __version__

setup(
  name = 'android_keygen',
  packages = find_packages(),
  version = 1,
  license='MIT',
  description = 'A simple keygen creator',
  author = 'Behron Georgantas',
  author_email = 'behronsresume@gmail.com',
  url = 'https://github.com/bresume/android_keygen',
  classifiers=[
      'Development Status :: 4 - Beta',
      'Intended Audience :: Developers',
      'Topic :: Scientific/Engineering :: Artificial Intelligence',
      'License :: OSI Approved :: MIT License',
      'Programming Language :: Python :: 3.6',
  ],
)