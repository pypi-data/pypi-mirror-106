from setuptools import setup, find_packages

setup(
    name='primerobotcli',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'Click',
        'docker',
        'boto3',
        'PyYAML',
        'typing_extensions'
    ],
    entry_points='''
        [console_scripts]
        primerobotcli = primerobotcli.interface:cli
    ''',
)
