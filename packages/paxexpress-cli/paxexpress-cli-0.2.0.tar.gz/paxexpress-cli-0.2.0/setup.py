# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['paxexpress_cli',
 'paxexpress_cli.authentication',
 'paxexpress_cli.files',
 'paxexpress_cli.packages',
 'paxexpress_cli.repositories',
 'paxexpress_cli.versions']

package_data = \
{'': ['*']}

install_requires = \
['PyYAML>=5.4.1,<6.0.0',
 'httpx>=0.16.1,<0.17.0',
 'inquirer>=2.7.0,<3.0.0',
 'keyring>=22.3.0,<23.0.0',
 'pydantic[email]>=1.8.1,<2.0.0',
 'rich>=9.13.0,<10.0.0',
 'typer>=0.3.2,<0.4.0']

extras_require = \
{':sys_platform == "win32"': ['pypiwin32>=223,<224']}

entry_points = \
{'console_scripts': ['paxexpress = paxexpress_cli.cli:cli']}

setup_kwargs = {
    'name': 'paxexpress-cli',
    'version': '0.2.0',
    'description': '',
    'long_description': None,
    'author': 'Florian Ludwig',
    'author_email': 'f.ludwig@greyrook.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
