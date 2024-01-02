from setuptools import find_packages,setup
from typing import List

Hypen_E_Dot='-e .'

def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements= []
    with open (file_path) as file_obj:
        requirements=file_obj.readlines()
        [req.replace("\n", " ") for req in requirements]

        if Hypen_E_Dot in requirements:
            requirements.remove(Hypen_E_Dot)
    return requirements



setup(
name='mlproject',
version='0.0.1',
author='Deepasijoy',
author_email='deepasijoy@gmail.com',
packages=find_packages() ,
install_requires=get_requirements('requirements.txt')


)