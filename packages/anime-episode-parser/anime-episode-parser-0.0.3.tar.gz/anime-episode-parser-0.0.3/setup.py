# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['anime_episode_parser']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'anime-episode-parser',
    'version': '0.0.3',
    'description': 'BGmi is a cli tool for subscribed bangumi.',
    'long_description': "# anime-episode-parser\n\ntry parse episode info from title\n\n```bash\npoetry add anime_episode_parser\n```\n\n```python3\nfrom anime_episode_parser import parse_episode\n\ntitle = '[YMDR][哥布林殺手][Goblin Slayer][2018][05][1080p][AVC][JAP][BIG5][MP4-AAC][繁中]'\nassert (5, 1) == parse_episode(title)\n\n# 5 for episode start\n# 1 for episodes count\n# `None` for un-determined episode\n# episode range is not implemented yet.\n```\n",
    'author': 'Trim21',
    'author_email': 'trim21me@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/BGmi/anime-episode-parser',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.6.1,<4.0.0',
}


setup(**setup_kwargs)
