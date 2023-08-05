#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

# with open('requirements.in') as requirements_file:
#     requirements = requirements_file.read().split()

requirements = [
    'SQLAlchemy==1.4.7',
    'psycopg2-binary==2.8.6',
    'click==8.0.0',
    'colr==0.9.1',
    'matplotlib==3.4.2',
    'pylab-sdk==1.3.2',
    'PyInquirer==1.0.3',
    'requests==2.25.1',
    'pytest==6.2.4',
    'colorlog==5.0.1',
    'pandas==1.2.4',
]


setup(
    author='Andoni Sooklaris',
    author_email='andoni.sooklaris@gmail.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    description='A Python module for custom-built tools and maintained by Andoni Sooklaris.',
    entry_points={
        'console_scripts': [
            'pydonitest=pydonitest.cli:main',
        ],
    },
    install_requires=requirements,
    license='MIT license',
    # long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='pydonitest',
    name='pydonitest',
    packages=find_packages(include=['pydonitest', 'pydonitest.*']),
    setup_requires=[],
    test_suite='tests',
    tests_require=[],
    url='https://github.com/tsouchlarakis/pydonitest',
    version='0.1.12',
    zip_safe=False,
)
