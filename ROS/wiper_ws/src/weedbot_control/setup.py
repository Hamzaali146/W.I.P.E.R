from glob import glob
import os

from setuptools import find_packages, setup

package_name = 'weedbot_control'

setup(
    name=package_name,
    version='1.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.py')),
        (os.path.join('share', package_name, 'config'),
            glob('config/*.yaml') + glob('config/*.csv')),
        (os.path.join('share', package_name), ['README.md']),
    ],
    install_requires=['setuptools', 'pyserial'],
    zip_safe=True,
    maintainer='hamza',
    maintainer_email='hamzaaly105@gmail.com',
    description='Laser control node for weedbot field hardware (vision to STM32).',
    license='MIT',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'control_node = weedbot_control.control_node:main',
            'laser_test_node = weedbot_control.laser_test_node:main',
        ],
    },
)
