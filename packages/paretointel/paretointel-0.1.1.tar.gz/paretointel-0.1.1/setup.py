import os

from setuptools import setup

HERE = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(HERE, 'README.md')) as f:
    README = f.read()

setup(
  name='paretointel',
  long_description=README,
  version='0.1.1',
  setup_requires=['pytest-runner'],
  tests_require=['pytest'],
  packages=[
    'paretointel',
    'paretointel.hdi',
    'paretointel.hdi.db', 
    'paretointel.hdi.spark', 
  ],
  url='https://github.com/paretointel/pareto-py',
  license='',
  author='Pareto Intelligence',
  author_email='engineering@paretointel.com',
  description='Pareto Engineering Python libraries'
)