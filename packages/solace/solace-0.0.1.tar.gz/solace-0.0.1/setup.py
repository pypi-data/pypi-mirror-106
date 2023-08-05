# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['solace']

package_data = \
{'': ['*']}

install_requires = \
['Werkzeug>=2.0.0,<3.0.0', 'munch>=2.5.0,<3.0.0']

setup_kwargs = {
    'name': 'solace',
    'version': '0.0.1',
    'description': 'A modern microframework for building REST APIs in Python',
    'long_description': None,
    'author': 'Dan Sikes',
    'author_email': 'dansikes7@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
