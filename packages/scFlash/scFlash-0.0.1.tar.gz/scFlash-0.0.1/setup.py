from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.1'
DESCRIPTION = 'scFlash is convinient and flexible package for Single Cell Analysis.'

# Setting up
setup(
    name="scFlash",
    version=VERSION,
    author="Sarath Kolli, Anudeep Kota, Aysha Saniya,  Kushan Raj, Meenakshi Pillai, Niranjan Jain, Rujutha Shinde, Shraddha Bharadwaj",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=['scanpy', 'lightning-flash==0.2.3'],
    keywords=['python', 'scrnaseq', 'sca'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
    ]
)