# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pyproteins',
 'pyproteins.alignment',
 'pyproteins.container',
 'pyproteins.sequence',
 'pyproteins.utils']

package_data = \
{'': ['*']}

install_requires = \
['biopython>=1.78,<2.0',
 'bs4>=0.0.1,<0.0.2',
 'lxml>=4.6.3,<5.0.0',
 'numpy>=1.20.3,<2.0.0']

setup_kwargs = {
    'name': 'pyproteins',
    'version': '1.5.1',
    'description': 'Toolbox to manipulate protein sequence data',
    'long_description': None,
    'author': 'glaunay',
    'author_email': 'pitooon@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
