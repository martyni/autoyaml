from distutils.core import setup

with open('version') as v:
    version = v.read().strip()

with open('requirements.txt') as deps:
    dependancies = [line for line in deps.readlines()]


setup(
    name='autoconfig',
    version=version,
    install_requires=dependancies,
    py_modules=['autoconfig',],
    license='Creative Commons Attribution-Noncommercial-Share Alike license',
    long_description=open('README.md').read(),
)
