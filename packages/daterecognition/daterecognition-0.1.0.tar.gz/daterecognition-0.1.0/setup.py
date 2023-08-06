# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['daterecognition']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'daterecognition',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Samit Shah',
    'author_email': 'samit@glib.ai',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
