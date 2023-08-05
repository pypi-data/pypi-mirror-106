"""Setup script for realpython-reader"""

import os.path
from setuptools import setup

# The directory containing this file
HERE = os.path.abspath(os.path.dirname(__file__))

# The text of the README file
with open(os.path.join(HERE, "README.md")) as fid:
    README = fid.read()




setup(name='mawaqit_times_calculator',
      version='0.0.3',
      description='Mawaqit Times Calculator',
      url='https://github.com/yac69/mawaqit_times_calculator',
      download_url = 'https://github.com/yac69/mawaqit_times_calculator/archive/refs/tags/0.0.3.tar.gz',
      author='Yacine Zitouni',
      author_email='iyac15@gmail.com',
      license='MIT',
      packages=['mawaqit_times_calculator'],
      zip_safe = False)
