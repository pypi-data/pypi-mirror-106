# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['camphr_pattern_search']

package_data = \
{'': ['*']}

install_requires = \
['camphr_core>=0.1.0,<0.2.0',
 'pyahocorasick>=1.4.0,<2.0.0',
 'pytextspan>=0.5.4,<0.6.0',
 'typing-extensions>=3.7.4']

setup_kwargs = {
    'name': 'camphr-pattern-search',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'tamuhey',
    'author_email': 'tamuhey@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/PKSHATechnology-Research/camphr',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
