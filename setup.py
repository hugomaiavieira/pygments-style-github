#!/usr/bin/python

from setuptools import setup

setup(
    name = 'pygments-style-github',
    version = '0.1',
    description = 'Pygments version of the github theme.',
    license = 'BSD',

    author = 'Hugo Maia Vieira',
    author_email = 'hugomaiavieira@gmail.com',

    url = 'https://github.com/hugomaiavieira/pygments-style-github',

    packages = ['pygments_style_github'],
    install_requires = ['pygments >= 1.4'],

    entry_points = '''[pygments.styles]
                      github = pygments_style_github:GithubStyle''',

    classifiers = [
        'Development Status :: 1 - Beta',
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