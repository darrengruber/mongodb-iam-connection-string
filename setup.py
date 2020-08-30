#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [ 
    'boto3==1.14.43',
    'botocore==1.17.43',
    'docopt==0.6.2',
    'docutils==0.15.2',
    'jmespath==0.10.0',
    'python-dateutil==2.8.1',
    's3transfer==0.3.3',
    'six==1.15.0',
    'urllib3==1.25.10',
    'yurl==1.0.0'
]

setup_requirements = [ ]

test_requirements = [ ]

setup(
    author="Darren Gruber",
    author_email='dgruber@gmail.com',
    python_requires='>=3.5',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="A small utility to generate a mongodb connection string from an IAM role",
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='mongodb_iam_connection_string',
    name='mongodb_iam_connection_string',
    packages=find_packages(include=['mongodb_iam_connection_string', 'mongodb_iam_connection_string.*']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/darrengruber/mongodb-iam-connection-string',
    version='1.0.0',
    entry_points={"console_scripts": ["mics = mongodb_iam_connection_string.cli:cli"]},
    zip_safe=False,
)
