# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['open_mafia_engine', 'open_mafia_engine.built_in', 'open_mafia_engine.util']

package_data = \
{'': ['*'], 'open_mafia_engine': ['prefabs/*']}

install_requires = \
['pydantic-yaml>=0.2.3,<0.3.0',
 'pydantic>=1.7.3,<2.0.0',
 'ruamel.yaml>=0.17.4,<0.18.0',
 'sortedcontainers>=2.3.0,<3.0.0']

extras_require = \
{'bay12': ['beautifulsoup4>=4.9.3,<5.0.0', 'requests>=2.25.1,<3.0.0']}

setup_kwargs = {
    'name': 'open-mafia-engine',
    'version': '0.4.0b1',
    'description': 'Open Mafia Engine - a framework for mafia/werewolf games.',
    'long_description': None,
    'author': 'Open Mafia Team',
    'author_email': 'openmafiateam@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
