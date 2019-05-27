from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = []

setup(
    name="pytorch-cloze-pretrained",
    version="0.0.1",
    author="Dhanachandra N.",
    author_email="dhana1991.n@gmail.com",
    description="Pytorch implementation of cloze driven pretrained",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/newprojectsetup/",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)
