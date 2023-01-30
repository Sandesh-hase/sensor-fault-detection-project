# Basic setup
from setuptools import find_packages,setup
from typing import List

def get_requirements()-> List[str]:
    """
    This function will return a list of requirements
    """
    requirement_list:List[str]=[]
    # Write a code to read requirements.txt and convert all req into list
    return requirement_list

setup(
    name="sensor",
    version="0.0.1",
    author="Sandesh",
    author_email="sandeshhase15@gmail.com",
    packages=find_packages(),
    install_requires=[pymongo==4.2.0],
)

