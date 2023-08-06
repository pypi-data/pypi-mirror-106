# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['kedro_dolt']

package_data = \
{'': ['*']}

install_requires = \
['kedro>=0.17.3,<0.18.0', 'pymysql>=1.0.2,<2.0.0']

setup_kwargs = {
    'name': 'kedro-dolt',
    'version': '0.1.0',
    'description': 'Kedro-Dolt Plugin',
    'long_description': None,
    'author': 'Max Hoffman',
    'author_email': 'max@dolthub.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6.2,<3.9',
}


setup(**setup_kwargs)
