from setuptools import setup, find_packages

setup(
    name='robotframework-primerobot',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'boto3',
        'PyYAML',
        'typing_extensions',
        'pandas==1.2.3'
    ],
)
