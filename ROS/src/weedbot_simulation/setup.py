from setuptools import setup
import os
from glob import glob

package_name = 'weedbot_simulation'

setup(
    name=package_name,
    version='1.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.py')),
        (os.path.join('share', package_name, 'worlds'), glob('worlds/*.world')),
        (os.path.join('share', package_name, 'urdf'), glob('urdf/*.xacro')),
        (os.path.join('share', package_name, 'models/weed'), glob('models/weed/*')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Hamza Ali',
    maintainer_email='hamzaaly105@gmail.com',
    description='Gazebo simulation for weedbot laser weeding system',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'laser_controller = weedbot_simulation.laser_controller:main',
            'tractor_controller = weedbot_simulation.tractor_controller:main',
            'weed_spawner = weedbot_simulation.weed_spawner:main',
        ],
    },
)