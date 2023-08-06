import setuptools 

with open("README.md", "r") as fh: 
    long_description = fh.read() 

setuptools.setup( 
name="selee_pk", 
version="0.1", 
author="Seung Eun (Sophia) Lee", 
author_email="leeseungeun0628@gmail.com", 
description="package development exercise", 
long_description=long_description, 
long_description_content_type="text/markdown",
url="https://github.com/sophialee0628/selee_pk", 
packages=setuptools.find_packages(), 
classifiers=[ 
    "Programming Language :: Python :: 3", 
    "Operating System :: OS Independent", ], 
python_requires='>=3.6', 
)

