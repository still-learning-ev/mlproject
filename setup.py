import os
import re
from setuptools import find_packages, setup
from typing import List


HYPHEN_E_DOT = "-e ."  # Ignore the -e . from the file
COMMENTED_REQS = r"^#.*"  # Ignore the commented requirements
requirement_file_path = os.path.join(os.getcwd(), "requirements.txt")


def get_requirements(file_path: str) -> List[str]:
    """
    This file is going to read the requirements.txt file
    and then return them as a List.
    Add -e . to the requirements.txt to automatically
    trigger the setup.py file.
    """
    requirements = []

    with open(file_path, "r") as requirements_file:
        requirements = requirements_file.readlines()

        # Remove the '\n' added after reading the requirements.txt
        # Add an empty string inplace of '\n'
        requirements = [requirement.replace("\n", "") for requirement in requirements]

        # Remove the '-e .' from requirements.txt from return list
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

        for req in requirements:
            if re.match(COMMENTED_REQS, req):
                requirements.remove(req)

        return requirements


setup(
    # Used to create the description of the project
    name="mlproject",
    version="0.1",
    author="Zeeshan Lone",
    author_email="lonexishan@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements(requirement_file_path),
)
