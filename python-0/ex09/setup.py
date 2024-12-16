from setuptools import setup, find_packages

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
    python_requires=">=3.6",
    install_requires=[],
)
