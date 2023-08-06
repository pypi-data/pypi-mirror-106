#!/usr/bin/env python

"""The setup script."""

from setuptools import find_packages, setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('CHANGELOG.rst') as history_file:
    history = history_file.read()

setup(
    name='cloup',
    setup_requires=['setuptools_scm'],
    use_scm_version={
        'write_to': 'cloup/_version.py'
    },
    author='Gianluca Gippetto',
    author_email='gianluca.gippetto@gmail.com',
    description="Option groups and subcommand help sections for pallets/click",
    long_description=readme + '\n\n' + history,
    long_description_content_type='text/x-rst',
    url='https://github.com/janLuke/cloup',
    license="BSD 3-Clause",
    keywords='cloup click option',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    packages=find_packages(include=['cloup', 'cloup.*']),
    zip_safe=False,
    include_package_data=True,
    python_requires='>=3.6',
    install_requires=[
        'click >=7.1, <9.0',
        'dataclasses; python_version<="3.6"',
    ],
)
