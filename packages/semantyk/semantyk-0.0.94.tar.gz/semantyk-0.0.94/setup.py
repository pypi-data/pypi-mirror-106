from pip._internal.req import parse_requirements
from setuptools import find_packages, setup

from src import semantyk as package

with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(
    author=package.__author__,
    author_email=package.__email__,
    classifiers=[
        'Development Status :: 1 - Planning',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8'
    ],
    description=package.__description__,
    keywords='semantyk',
    license='LICENSE',
    long_description=long_description,
    long_description_content_type='text/markdown',
    maintainer=package.__author__,
    name='semantyk',
    package_dir={'': 'src'},
    packages=find_packages(
        exclude={
            'doc',
            'tests*'
        }
    ),
    url='https://www.semantyk.com',
    version=package.__version__
)
