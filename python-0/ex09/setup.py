from setuptools import setup, find_packages

"""
    To create a python package we should write setup.py file.
    Name: package name
    version: verison of package
    summary : summary of package
    author: who wrote this package
    aurhor_email: author mail
    url: where package source code
    description: description of package
    long_description: long description of package like readme
    license: license of package
    packages: finc packaged automatic finding the packages what you used
    package_dir: package direction
    python_requires: python requires
    install_requires: if you have extra packages like numpy you can add here
"""

setup(
    name="ft_package",
    version="0.0.1",
    summary="A sample test package",
    author="museker",
    author_email="museker@student.42istanbul.com.tr",
    url="https://github.com/museker/ft_package",
    description="A sample test package",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    license="MIT",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[],
    python_requires=">=3.10",
    install_requires=[],
)
