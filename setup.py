# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

import template_goodies


setup(
    name='django_template_goodies',
    version=template_goodies.VERSION,
    description='A set of django template tools.',
    author='Jakub Janoszek',
    author_email='kuba.janoszek@gmail.com',
    include_package_data=True,
    url='https://github.com/jqb/django-template-goodies/',
    packages=find_packages(),
    install_requires=[
        'django-classy-tags==0.6.1',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    zip_safe=False,
)

# Usage of setup.py:
# $> python setup.py register             # registering package on PYPI
# $> python setup.py build sdist upload   # build, make source dist and upload to PYPI
