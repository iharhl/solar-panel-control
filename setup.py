from importlib.metadata import entry_points
from setuptools import setup, find_packages

setup(name='solar-panel-control',
      version='0.3.0',
      description='Package contains software for solar panel movement control',
      author='Ihar Hlukhau',
      author_email='ihluk@outlook.com',
      packages=find_packages(),
     )