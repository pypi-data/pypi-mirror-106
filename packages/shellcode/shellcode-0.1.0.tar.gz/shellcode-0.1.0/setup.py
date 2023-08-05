# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['shellcode']

package_data = \
{'': ['*']}

install_requires = \
['capstone>=4.0.2,<5.0.0', 'typer>=0.3.2,<0.4.0']

setup_kwargs = {
    'name': 'shellcode',
    'version': '0.1.0',
    'description': 'CLI to turn shellcode back to asm.',
    'long_description': None,
    'author': '4thel00z',
    'author_email': '4thel00z@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
