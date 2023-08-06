# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# with open('requirements.txt') as f:
#     required = f.read().splitlines()

setup(
    name="greetings_sdk",
    version="0.0.2",
    author="Omar Ilias",
    author_email="elmimouni.o.i@gmail.com",
    description="Greetings SDK.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/elmiomar/greetings",
    project_urls={
        "Bug Tracker": "https://github.com/elmiomar/greetings/issues",
        "Documentation": "https://github.com/elmiomar/greetings/wiki",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[],
    packages=find_packages(),
    python_requires=">=3.6",
)
