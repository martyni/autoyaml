import pathlib
from setuptools import setup, find_packages

PWD = pathlib.Path(__file__).parent
README = ( PWD / "README.md").read_text()
VERSION = "2020.2.5.1033"





setup(
    name='autoyaml',
    test_suite="tests",
    version=VERSION,
    description="Load and save config files for python projects",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/martyni/autoyaml",
    author="martyni",
    author_email="martynjamespratt@gmail.com",
    license='MIT',
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.5",
    ],
    packages=find_packages(exclude=["tests"],),
    package_data = {'':['*.txt', '*.md']},
    include_package_data=True,
    install_requires=["pyaml","cryptography"],
)
