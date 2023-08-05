# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['schema_induction']

package_data = \
{'': ['*']}

install_requires = \
['unicodecsv>=0.14.1,<0.15.0']

setup_kwargs = {
    'name': 'schema-induction',
    'version': '1.1.5',
    'description': 'Auto generate schema from list of json objects',
    'long_description': None,
    'author': 'Binh Vu',
    'author_email': 'binh@toan2.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
