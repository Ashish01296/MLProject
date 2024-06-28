#for Downloading Packages
from setuptools import find_packages
from setuptools import setup

from typing import List

HYPEN_E_DOT = '-e .'
def get_requirements(file_path:str)->List[str]:

    '''
    this function will return the list of Requirements
    '''
    requirements = []
    with open(file_path) as file_object:
        requirements = file_object.readlines()
        requirements=[req.replace("\n","")for req in requirements] 


        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements

setup(

name='MLProject',
version='0.0.1',
author='Ashish',
author_email='ashishvinod160@gmail.com',
packages= find_packages(),
install_requires = get_requirements('requirements.txt') 
)