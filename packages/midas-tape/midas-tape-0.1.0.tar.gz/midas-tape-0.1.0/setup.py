# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['midas_tape']

package_data = \
{'': ['*']}

install_requires = \
['awkward>=1.2.0,<2.0.0', 'numpy>=1.13.1,<2.0.0']

setup_kwargs = {
    'name': 'midas-tape',
    'version': '0.1.0',
    'description': 'Read MIDAS tape server files',
    'long_description': None,
    'author': 'Angus Hollands',
    'author_email': 'goosey15@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
