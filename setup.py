#!/usr/bin/python

from setuptools import setup, find_packages

setup(
    name='pygments-style-github',
    version='0.4',
    description='Pygments version of the github theme.',
    long_description=open('README.rst').read(),
    keywords='pygments style github',
    license='BSD',

    author='Hugo Maia Vieira',
    author_email='hugomaiavieira@gmail.com',

    url='https://github.com/hugomaiavieira/pygments-style-github',

    packages=find_packages(),
    install_requires=['pygments >= 1.4'],

    entry_points='''[pygments.styles]
                    github=pygments_style_github:GithubStyle''',

    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Plugins',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)