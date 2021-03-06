#!/usr/bin/env python

"""The setup script."""

import os
import TinyBeansBox as module
from setuptools import setup, find_packages


def walker(base, *paths):
    file_list = set([])
    cur_dir = os.path.abspath(os.curdir)

    os.chdir(base)
    try:
        for path in paths:
            for dname, dirs, files in os.walk(path):
                for f in files:
                    file_list.add(os.path.join(dname, f))
    finally:
        os.chdir(cur_dir)

    return list(file_list)


with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('CHANGELOG.rst') as history_file:
    history = history_file.read()

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup_requirements = ['pytest-runner', ]

test_requirements = ['pytest>=3', ]

setup(
    author="Adam Hitchcock",
    author_email='adam@northisup.com',
    python_requires='>=3.7',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="A tool to sync tinybeans to dropbox for pictureframes.",
    entry_points={
        'console_scripts': [
            'TinyBeansBox=TinyBeansBox.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='TinyBeansBox',
    name='TinyBeansBox',
    packages=find_packages(include=['TinyBeansBox', 'TinyBeansBox.*']),
    package_data={
        module.__name__: walker(
            os.path.dirname(module.__file__),
            'files'
        ),
    },
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/NorthIsUp/TinyBeansBox',
    version='0.1.0',
    zip_safe=False,
)
