from setuptools import setup, find_packages
from typing import List
HYPEN_E_DOT = '-e .'

def get_requirements(file_pate)->list[str]:
    '''this function will return the list of requirements'''
    requrirements = []
    with open(file_pate) as file_obj:
        requrirements = file_obj.readlines()
        [req.replace("\n","") for req in requrirements]
        if HYPEN_E_DOT in requrirements:
            requrirements.remove(HYPEN_E_DOT)
    return requrirements

setup(
    name='mlproject',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA example python package',
    long_description=open('README.md').read(),
    author='Umesh Kumar',
    author_email='umeshpatelofficialmail@gmail.com',
    install_requires=get_requirements('requirements.txt')
)