from setuptools import find_packages
from setuptools import setup

setup(
    name='weedbot_interfaces',
    version='0.0.1',
    packages=find_packages(
        include=('weedbot_interfaces', 'weedbot_interfaces.*')),
)
