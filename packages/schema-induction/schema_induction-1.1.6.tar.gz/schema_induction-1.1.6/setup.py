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
    'version': '1.1.6',
    'description': 'Auto generate schema from list of json objects',
    'long_description': '# Installation\n\n```bash\npip install schema_induction\n```\n\n# Usages\n\n```python\nfrom schema_induction import generate_schema\n\n# list of objects that you wish to find their schema\nrecords = []\nprint(generate_schema(records))\n```',
    'author': 'Binh Vu',
    'author_email': 'binh@toan2.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/binh-vu/schema-induction',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
