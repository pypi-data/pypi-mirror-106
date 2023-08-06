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
    'version': '0.1.2',
    'description': 'Wizardry is an open-source CLI for building powerful algorithmic trading strategies faster and easier',
    'long_description': '# Wizardry, the Algorithmic Wizard 💫\n\nWizardry is an open-source **CLI** for **building powerful algorithmic trading strategies faster** and **easier** (for Lean/QuantConnect)\n\n<div align="center">\n<img src="https://raw.githubusercontent.com/ssantoshp/Wizardry/main/documentation/wiz.png"/>\n\n![](https://static.pepy.tech/personalized-badge/wizardry?period=total&units=international_system&left_color=black&right_color=brightgreen&left_text=Users)\n![](https://img.shields.io/badge/license-MIT-blue)\n![](https://img.shields.io/badge/swag%20level-A++-brightgreen)\n![](https://img.shields.io/badge/language-python🐍-blue)\n![](https://camo.githubusercontent.com/97d4586afa582b2dcec2fa8ed7c84d02977a21c2dd1578ade6d48ed82296eb10/68747470733a2f2f6261646765732e66726170736f66742e636f6d2f6f732f76312f6f70656e2d736f757263652e7376673f763d313033)\n\n</div>\n\nHomepage: https://github.com/ssantoshp/Wizardry',
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
