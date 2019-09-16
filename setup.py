from setuptools import setup, find_packages


with open('version') as v:
    version = v.read().strip()

with open('requirements.txt') as deps:
    dependancies = [line for line in deps.readlines()]


setup(
    name='autoconfig',
    version=version,
    install_requires=dependancies,
    packages=find_packages(),
    test_suite="tests",
    license='Creative Commons Attribution-Noncommercial-Share Alike license',
    long_description=open('README.md').read(),
)
