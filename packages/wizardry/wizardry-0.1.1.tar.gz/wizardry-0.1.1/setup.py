# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['wizardry']

package_data = \
{'': ['*']}

install_requires = \
['PyInquirer>=1.0.2,<2.0.0',
 'lean>=0.1.53,<0.2.0',
 'pyfiglet>=0.8.0,<0.9.0',
 'requests==2.25.1',
 'termcolor>=1.1.0,<2.0.0',
 'typer[all]>=0.3.2,<0.4.0']

entry_points = \
{'console_scripts': ['wizardry = wizardry.cli:app']}

setup_kwargs = {
    'name': 'wizardry',
    'version': '0.1.1',
    'description': 'Wizardry is an open-source CLI for building powerful algorithmic trading strategies faster and easier',
    'long_description': None,
    'author': 'ssantoshp',
    'author_email': 'santoshpassoubady@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
