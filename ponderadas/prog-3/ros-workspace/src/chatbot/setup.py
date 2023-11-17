from setuptools import find_packages, setup
from glob import glob
import os

package_name = 'chatbot'

setup(
    name=package_name,
    version='0.0.1',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='jupiter',
    maintainer_email='lucas.jupiter23@gmail.com',
    description='My first chatbot',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'output = chatbot.output:main',
            'input = chatbot.input:main'
        ],
    },
)
