# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['mei2volpiano']

package_data = \
{'': ['*']}

install_requires = \
['pytz>=2021.1,<2022.0']

entry_points = \
{'console_scripts': ['mei2vol = mei2volpiano:driver.main',
                     'mei2volpiano = mei2volpiano:driver.main']}

setup_kwargs = {
    'name': 'mei2volpiano',
    'version': '0.6.0',
    'description': '',
    'long_description': None,
    'author': 'DDMAL',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
