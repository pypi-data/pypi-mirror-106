#!usr/bin/env python3

from setuptools import find_packages
from distutils.core import setup
from os import path



if __name__ == '__main__':
    # read the contents of your README file
    this_directory = path.abspath(path.dirname(__file__))
    with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
        long_description = f.read()

    setup(
        name='autocleus',
        version='0.1.1',
        author='Christopher Demone',
        author_email='c.demone@hotmail.com',
        packages=[
            'autocleus',
            'autocleus.cmd',
            'autocleus.climaker',
            'autocleus.forms',
            'autocleus.hooks',
            'autocleus.library',
            'autocleus.templates', 
        ],
        package_data={
            "": ["*.j2", "*.lic"]
        },
        include_package_data=True,
        scripts=['autocleus/library/autocleus'],
        url='https://github.com/ludah65/autocleus.git',
        license='LICENSE',
        description="A command line interface for creating your own command line interface",
        long_description=long_description,
        long_description_content_type='text/markdown',
        install_requires=[
            'Pydantic==1.7.3',
            'typing==3.7.4.3',
            'PyInquirer==1.0.3',
            'virtualenv==20.4.4',
            'art==5.1',
            'jinja2==2.10.1',
            'setuptools==45.2.0',
            'asciimatics==1.13.0',
            'yaspin==1.5.0',
            'yamldirs==1.1.8'
            ],
    )
