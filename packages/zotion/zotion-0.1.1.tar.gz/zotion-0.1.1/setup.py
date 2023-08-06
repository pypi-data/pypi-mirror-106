# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['zotion']

package_data = \
{'': ['*']}

install_requires = \
['addict>=2.4.0,<3.0.0', 'httpx>=0.18.1,<0.19.0', 'python-decouple>=3.4,<4.0']

setup_kwargs = {
    'name': 'zotion',
    'version': '0.1.1',
    'description': 'A python client for the official notion API',
    'long_description': 'WIP Python client for official Notion API (now in public beta)\n\nFor now just internal integrations.\n\nFeel free to contribute.\n\nMIT license.\n',
    'author': 'avlm',
    'author_email': 'victor.luckwu@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/avlm/zotion',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
