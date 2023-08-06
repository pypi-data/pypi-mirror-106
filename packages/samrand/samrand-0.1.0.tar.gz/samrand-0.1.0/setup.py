from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='samrand',
    version='0.1.0',
    description='A random sampling tool.',
    long_description=long_description,
    long_description_content_type='text/x-rst',
    url='https://gitlab.com/omazhary/SamRand',
    author='omazhary',
    author_email='omazhary@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering :: Information Analysis',
    ],
    keywords='data sample statistics',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    install_requires=[
        'argparse',
        'numpy',
    ],
    extras_require={},
    package_data={},
    data_files={},
    scripts=['bin/samrand'],
    zip_safe=False
)
