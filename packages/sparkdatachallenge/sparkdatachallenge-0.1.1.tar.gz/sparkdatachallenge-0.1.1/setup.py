# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['sparkdatachallenge']
install_requires = \
['ipykernel>=5.5.5,<6.0.0',
 'isort>=5.8.0,<6.0.0',
 'matplotlib>=3.4.2,<4.0.0',
 'nbsphinx>=0.8.5,<0.9.0',
 'numpy>=1.20.3,<2.0.0',
 'pandas>=1.2.4,<2.0.0',
 'pylint>=2.8.2,<3.0.0',
 'sympy>=1.8,<2.0']

setup_kwargs = {
    'name': 'sparkdatachallenge',
    'version': '0.1.1',
    'description': '<Enter a one-sentence description of this project here.>',
    'long_description': '==================\nsparkdatachallenge\n==================\n\n\n\nSparkdata challenge for finding multiplicative pairs in a sorted array of decimal numbers that\nare constructed from two arrays (A,B), one containing the integer part and one containing the decimal part\nbut as an integer.\n\nThe decimal numbers are then constructed as following:\nC[i] = A[i] + B[i] / scale \n\nwhere the scale is a fixed number (here 1_000_000).\n\n* Free software: MIT license\n* Documentation: https://sparkdatachallenge.readthedocs.io.\n\n\nFeatures\n--------\n\n* Brute force method that fails due to memory allocation for large arrays but only uses numpy vectorized functions\n* Brute force method based on a double for-loop\n* Math based method - optimized using mathematical properties of the inequalities and leveraging that the decimal number array C is sorted.\n  \n',
    'author': 'Tom Mertens',
    'author_email': 'your.email@whatev.er',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/tomerten/sparkdatachallenge',
    'py_modules': modules,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
