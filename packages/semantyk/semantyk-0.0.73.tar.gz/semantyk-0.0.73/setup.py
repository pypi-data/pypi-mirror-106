from setuptools import find_packages, setup
from pip._internal.req import parse_requirements

with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(
    author='Semantyk',
    author_email='contact@semantyk.com',
    classifiers=[
        'Development Status :: 1 - Planning',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8'
    ],
    description='Ideas Wonder.',
    keywords='semantyk',
    license='LICENSE',
    long_description=long_description,
    long_description_content_type='text/markdown',
    maintainer='Semantyk',
    name='semantyk',
    packages=find_packages(
        exclude={
            'doc',
            'tests*'
        }
    ),
    url='https://github.com/semantyk/Semantyk',
    version='0.0.73'
)
