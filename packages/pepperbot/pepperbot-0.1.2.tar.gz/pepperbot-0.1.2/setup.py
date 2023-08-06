# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pepperbot',
 'pepperbot.action',
 'pepperbot.command',
 'pepperbot.exceptions',
 'pepperbot.message',
 'pepperbot.models',
 'pepperbot.models.api',
 'pepperbot.models.events',
 'pepperbot.parse',
 'pepperbot.utils']

package_data = \
{'': ['*']}

install_requires = \
['SQLAlchemy>=1.4.15,<2.0.0',
 'arrow>=1.0.3,<2.0.0',
 'devtools>=0.6.1,<0.7.0',
 'httpx==0.15.4',
 'loguru>=0.5.3,<0.6.0',
 'pretty-errors>=1.2.20,<2.0.0',
 'pydantic>=1.8.1,<2.0.0',
 'sanic>=20.12.2,<21.0.0']

setup_kwargs = {
    'name': 'pepperbot',
    'version': '0.1.2',
    'description': '',
    'long_description': None,
    'author': 'SSmJaE',
    'author_email': 'shaoxydd8888@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
