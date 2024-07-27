from setuptools import setup, find_packages
from typing import List

# get_requriments = lambda filename: [line.strip() for line in open(filename).readlines()]
HYPEN_E_DOT = "-e ."
def get_requriments(file_path:str)->List:
    reuirements = []
    with open(file_path, 'r') as file:
        requirements=file.readlines()
        requirements=[req.replace("\n","")for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
    name='mlproject',
    version='0.1',
    packages=find_packages(),
    install_requires=get_requriments('requirements.txt'),
)