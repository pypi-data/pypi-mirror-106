# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dpytools']

package_data = \
{'': ['*']}

install_requires = \
['discord.py>=1.7.1,<2.0.0']

setup_kwargs = {
    'name': 'dpytools',
    'version': '0.11.0b0',
    'description': 'Toolset to speed up discord bot development using discord.py',
    'long_description': '[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)\n\n[![PyPI status](https://img.shields.io/pypi/status/dpytools.svg)](https://pypi.python.org/pypi/dpytools/)\n[![PyPI version fury.io](https://badge.fury.io/py/dpytools.svg)](https://pypi.python.org/pypi/dpytools/)\n[![Downloads](https://pepy.tech/badge/dpytools)](https://pepy.tech/project/dpytools)\n[![PyPI license](https://img.shields.io/pypi/l/dpytools.svg)](https://pypi.python.org/pypi/dpytools/)\n\n\n# dpytools\nCollection of tools to speed up developing discord bots using discord.py\n\n# Features\n- The batteries of discord.py\n- Easy to read type-hinted code\n- Active development\n- Minimal dependencies\n\n# Instalation\nInstall the latest version of the library with pip.\n```\npip install -U dpytools\n```\n\n# Useful links:\n- [List](https://github.com/chrisdewa/dpytools/blob/master/docs/All.md) of all the tools.\n- [Project Home](https://github.com/chrisdewa/dpytools) on github\n- [Changelog](https://github.com/chrisdewa/dpytools/blob/master/CHANGELOG.md)\n- [F. A. Q.](https://github.com/chrisdewa/dpytools/blob/master/docs/FAQ.md) and examples\n\n# Status of the project\nBeta.\nAll functions have been tested but new tools are frequently added.\nBreaking changes may come depending on changes on API or discord.\nUse in production only after extensive testing.\n\n# Contributing\nFeel free to make a pull request or rise any issues.\n\n# Contact\nMessage me on discord at **ChrisDewa#4552** if you have any questions, ideas or suggestions.\n',
    'author': 'chrisdewa',
    'author_email': 'alexdewa@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/chrisdewa/dpytools',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
