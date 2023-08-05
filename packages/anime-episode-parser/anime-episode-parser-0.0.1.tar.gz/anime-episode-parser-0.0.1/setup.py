# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['anime_episode_parser']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'anime-episode-parser',
    'version': '0.0.1',
    'description': 'BGmi is a cli tool for subscribed bangumi.',
    'long_description': "# anime-episode-parser\n\ntry parse episode info from title\n\n```bash\npoetry add anime_episode_parser\n```\n\n```python\nfrom anime_episode_parser import parse_episode\n\nprint(parse_episode('[YMDR][哥布林殺手][Goblin Slayer][2018][01][1080p][AVC][JAP][BIG5][MP4-AAC][繁中]'))\n```\n",
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
