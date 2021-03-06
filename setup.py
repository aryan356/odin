import re
from os.path import join, dirname

from setuptools import setup, find_packages


with open(join(dirname(__file__), 'odin', '__init__.py')) as v_file:
    package_version = re.compile('.*__version__ = \'(.*?)\'', re.S)\
        .match(v_file.read()).group(1)


dependencies = [
    'restfulpy >= 1.5.0'
]


setup(
    name='odin',
    author='shayan',
    author_email='shayan.rokrok@gmail.com',
    version=package_version,
    install_requires=dependencies,
    packages=find_packages(),
    test_suite='odin.tests',
    entry_points={
        'console_scripts': [
            'odin = odin:odin.cli_main'
        ]
    }
)

