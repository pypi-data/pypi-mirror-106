# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['poetry_scripts']

package_data = \
{'': ['*']}

install_requires = \
['poetry>=1.2.0a1,<2.0.0']

entry_points = \
{'poetry.application.plugin': ['do = poetry_scripts:MyApplicationPlugin']}

setup_kwargs = {
    'name': 'poetry-scripts',
    'version': '0.0.1',
    'description': '',
    'long_description': 'None',
    'author': 'Trim21',
    'author_email': 'i@trim21.me',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6.2,<4.0.0',
}


setup(**setup_kwargs)
