import io
from setuptools import setup, find_packages
import sys

setup(name='mctk',
      version='0.0.1',
      description='HEROES minecraft toolkit',
      packages=find_packages(exclude=['*.tests', '*.tests.*', 'tests.*', 'tests']),
      zip_safe=True,
      include_package_data=True,
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Education',
          'Intended Audience :: Developers',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.2',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
      ],
)
