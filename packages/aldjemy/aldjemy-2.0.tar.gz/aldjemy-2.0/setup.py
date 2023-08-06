# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['aldjemy']

package_data = \
{'': ['*']}

install_requires = \
['Django>=2.2', 'SQLAlchemy>=1.4']

setup_kwargs = {
    'name': 'aldjemy',
    'version': '2.0',
    'description': 'SQLAlchemy for your Django models',
    'long_description': None,
    'author': 'Mikhail Krivushin',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6',
}


setup(**setup_kwargs)
