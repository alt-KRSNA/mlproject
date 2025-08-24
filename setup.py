from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path: str) -> List[str]:
    with open(file_path) as file_obj:
        requirements = file_obj.read().splitlines()
        requirements = [req.strip() for req in requirements if req.strip() and req.strip() != "-e ."]
    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author="KRzNA",
    author_email="krishnadhikale605@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
