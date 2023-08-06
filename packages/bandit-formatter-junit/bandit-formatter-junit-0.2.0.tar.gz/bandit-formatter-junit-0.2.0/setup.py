# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['bandit_formatter_junit']

package_data = \
{'': ['*']}

install_requires = \
['bandit>=1.7.0,<2.0.0']

entry_points = \
{u'bandit.formatters': ['junit = bandit_formatter_junit.junit:report']}

setup_kwargs = {
    'name': 'bandit-formatter-junit',
    'version': '0.2.0',
    'description': 'A bandit formatter plugin for valid JUnit output',
    'long_description': None,
    'author': 'Martin Styk',
    'author_email': 'mart.styk@gmail.com',
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
