# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['mancala', 'mancala.agents', 'mancala.state']

package_data = \
{'': ['*']}

install_requires = \
['gym>=0.18.0,<0.19.0',
 'numpy>=1.20.1,<2.0.0',
 'pandas>=1.2.4,<2.0.0',
 'tqdm>=4.60.0,<5.0.0']

entry_points = \
{'console_scripts': ['mancala = mancala.cli:cli']}

setup_kwargs = {
    'name': 'mancala',
    'version': '0.2.1',
    'description': 'Mancala written in Python, playable in CLI (GUI coming soon)!',
    'long_description': "# Mancala\n\nMancala board game written in python.\n\n![img](https://github.com/qqhann/Mancala/blob/main/assets/preview_cli.png)\n\n## Features & Road maps\n\n- [x] Mancala playable on CLI\n- [x] Cmpatible with the gym API\n- [ ] Can train RL agents\n- [ ] Mancala playable on GUI\n\n## Installation\n\n```shell\n$ pip install mancala\n```\n\n## Usage\n\n### Play a game with agents\n\n```shell\n$ mancala play --player0 human --player1 random\n```\n\n### Compare each agents and plot their win rates\n\nThe values are player0's (first move) win rates in percentage\n\n```shell\n$ mancala arena\n            p0_random  p0_exact  p0_max  p0_minimax\np1_random        40.0      12.0     2.0         0.0\np1_exact         76.0      38.0    29.0         2.0\np1_max           91.0      55.0    27.0         1.0\np1_minimax       99.0      87.0    81.0        28.0\n```\n\n## Algorithms\n\nMancala is a game with perfect information.\nマンカラは完全情報ゲームです。\n\n### Value Iteration\n\nUsing Dynamic Programming (DP), calculate value for states and memorize them.\nUse the value to plan future actions.\n\nOther implementations\n\n- OpenSpiel value_iteration\n  algorithm <https://github.com/deepmind/open_spiel/blob/master/open_spiel/python/algorithms/value_iteration.py>\n  example <https://github.com/deepmind/open_spiel/blob/master/open_spiel/python/examples/value_iteration.py>\n\n### Policy Iteration\n\nUsing Dynamic Programming (DP), calculate value for states and memorize them.\nUse the value and policy for planning.\n\n## References\n\n- <https://github.com/mdavolio/mancala>\n\n### Multi agent RL\n\n- <https://github.com/deepmind/open_spiel>\n- <https://github.com/PettingZoo-Team/PettingZoo>\n",
    'author': 'Qiushi Pan',
    'author_email': 'qiu.gits@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/qqhann/Mancala',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
