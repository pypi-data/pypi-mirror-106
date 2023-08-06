import sys
from setuptools import setup, find_packages

from constants import __version__

setup(
  name = 'app_icon_creator',
  packages = find_packages(),
  version = 3,
  license='MIT',
  description = 'A simple app icon creator',
  author = 'Behron Georgantas',
  author_email = 'behronsresume@gmail.com',
  url = 'https://github.com/bresume/app_icon_creator',
  install_requires = [
    'pillow'
  ],
  classifiers=[
      'Development Status :: 4 - Beta',
      'Intended Audience :: Developers',
      'Topic :: Scientific/Engineering :: Artificial Intelligence',
      'License :: OSI Approved :: MIT License',
      'Programming Language :: Python :: 3.6',
  ],
)