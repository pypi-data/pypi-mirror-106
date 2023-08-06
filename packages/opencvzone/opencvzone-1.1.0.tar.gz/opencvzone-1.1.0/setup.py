from distutils.core import setup
from setuptools import setup

# read the contents of your README file
from os import path
file = 'C:\\Users\\Lepsy\\Desktop\\General\\CompVision\\opencvzone\\README.md'
with open(file, encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='opencvzone',
    packages=['opencvzone'],
    version='1.1.0',
    license='MIT',
    description='Computer Vision Helping Library',
    author='Lepsy Goyal',
    author_email='goyalpti99@gmail.com',
    url='https://github.com/lepsygoyal/opencvzone.git',
    keywords=['ComputerVision', 'HandTracking', 'FaceTracking', 'PoseEstimation','Volume Controller'],
    install_requires=[
        'opencv-python',
        'mediapipe',
        'numpy',
        'pyserial',
        'pycaw',
        'comtypes'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',  # Specify which pyhton versions that you want to support
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)
