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
    'version': '0.4.0b3',
    'description': 'Open Mafia Engine - a framework for mafia/werewolf games.',
    'long_description': '# Open Mafia Engine\n\nThe Open Mafia Engine is a flexible, open-source game engine\n\n## Features\n\n- Event-based architecture, which allows for very complex interactions.\n- Many built-in abilities, victory conditions, etc.\n- YAML `Prefab`s let you define a game in a (mostly) human-readable fashion.\n- Open source & extensible, with a plugin system in the works.\n\n## Installing\n\nIt should be pretty easy to install:\n\n`pip install open_mafia_engine`\n\n## Getting started\n\nThis example starts a 5-player "vanilla" mafia game (1 mafioso vs 4 townies):\n\n```python\nfrom open_mafia_engine.api import Prefab\n\nprefab = Prefab.load("Vanilla Mafia")\nplayers = [\'Alice\', \'Bob\', \'Charlie\', \'Dave\', \'Eddie\']\ngame = prefab.create_game(players)\n```\n\nActually running commands in the engine is pretty complicated for now.\nWe\'re working to improve that experience.\n',
    'author': 'Open Mafia Team',
    'author_email': 'openmafiateam@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://open-mafia-engine.readthedocs.io/en/latest/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
