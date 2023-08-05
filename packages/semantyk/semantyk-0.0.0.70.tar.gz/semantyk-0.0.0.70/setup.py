from setuptools import find_packages, setup

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
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8'
    ],
    description='Ideas Wonder.',
    install_requires=['rdflib', 'uuid'],
    keywords='semantyk',
    license='LICENSE',
    long_description=long_description,
    long_description_content_type='text/markdown',
    maintainer='Semantyk',
    name='semantyk',
    package_dir={'': 'src'},
    packages=find_packages(
        exclude={
            'doc',
            'tests*'
        }
    ),
    url='https://github.com/semantyk/Semantyk',
    version='0.0.0.70'
)
