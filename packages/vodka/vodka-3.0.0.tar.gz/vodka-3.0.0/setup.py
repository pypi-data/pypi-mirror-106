# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['vodka',
 'vodka.config',
 'vodka.data',
 'vodka.plugins',
 'vodka.resources.blank_app',
 'vodka.resources.blank_app.plugins',
 'vodka.runners']

package_data = \
{'': ['*']}

install_requires = \
['click', 'munge>=1,<2', 'pluginmgr>=1,<2', 'tmpl>=0,<1']

entry_points = \
{'console_scripts': ['bartender = vodka.bartender:bartender']}

setup_kwargs = {
    'name': 'vodka',
    'version': '3.0.0',
    'description': 'plugin based real-time web service daemon',
    'long_description': None,
    'author': '20C',
    'author_email': 'code@20c.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
