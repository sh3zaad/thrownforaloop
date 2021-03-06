from setuptools import setup, find_packages

setup(
    name='thrownforaloop',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA hackathon package',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/sh3zaad/thrownforaloop',
    author='Shezaad Essop Moosa',
    author_email='shezaadem@gmail.com'
)
