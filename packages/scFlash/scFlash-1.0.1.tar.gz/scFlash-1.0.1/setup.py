from setuptools import setup,find_packages

def readme():
    with open('README.md') as f:
        README = f.read()
    return README


setup(
    name="scFlash",
    version="1.0.1",
    description="One stop solution for Single Cell analysis",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/bayeslabs/scFlash",
    author="Sarath Kolli, Anudeep Kota, Aysha Saniya, Kushan Raj, Meenakshi Pillai, Niranjan Jain, Rujutha Shinde, Shraddha Bharadwaj",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",        
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
    packages=find_packages(),
    keywords=['SCA', 'SC-RNA SEQ'],
    include_package_data=True,
    install_requires=['bs4', 'requests'],
    
)
