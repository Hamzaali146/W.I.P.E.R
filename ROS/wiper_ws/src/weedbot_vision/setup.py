from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'weedbot_vision'

setup(
    name=package_name,
    version='0.0.1',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.py')),
        (os.path.join('share', package_name, 'config'), glob('config/*.yaml')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Hamza Ali',
    maintainer_email='hamzaaly105@gmail.com',
    description='Weed detection vision system for weedbot with YOLO and homography calibration',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'bridge = weedbot_vision.bridge:main',
            # 'vision_node = weedbot_vision.vision_node:main',
            # 'camera_publisher = weedbot_vision.camera_publisher:main',
            # 'detection_monitor = weedbot_vision.detection_monitor:main',
            # 'camera_calibration = weedbot_vision.camera_calibration:main',
        ],
    },
)