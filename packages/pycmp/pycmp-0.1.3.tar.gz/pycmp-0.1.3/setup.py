# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pycmp',
 'pycmp.ast',
 'pycmp.cli',
 'pycmp.grammar',
 'pycmp.grammar.cmp_tables',
 'pycmp.helpers',
 'pycmp.traverse']

package_data = \
{'': ['*']}

install_requires = \
['ply==3.11']

setup_kwargs = {
    'name': 'pycmp',
    'version': '0.1.3',
    'description': 'Compiler MATLAB to Python',
    'long_description': None,
    'author': 'Artem Eroshev',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
