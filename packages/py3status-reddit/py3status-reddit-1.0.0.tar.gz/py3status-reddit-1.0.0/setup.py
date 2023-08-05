# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['py3status_reddit']

package_data = \
{'': ['*']}

install_requires = \
['praw>=7.2.0,<8.0.0', 'xdg>=5.0.2,<6.0.0']

entry_points = \
{'py3status': ['module = py3status_reddit.reddit']}

setup_kwargs = {
    'name': 'py3status-reddit',
    'version': '1.0.0',
    'description': 'py3status module showing reddit unread messages',
    'long_description': '# py3status-reddit\n\nA py3status module showing reddit unread messages.\n\n## install\n\n```\npip install py3status-reddit\n```\n\n## configuration\n\n* `format`: output format (default `reddit: {count}`)\n* `cache_timeout`: how often to refresh the information\n\nA fancier format could be achieved using Font Awesome:\n\n```\nformat = \'\\?if=!count=0 <span color="#FF5700" font_family="FontAwesome">\\uf281 <span font_weight="heavy">{count}</span></span>|\'\n```\n\n![](fancy_count.png)\n\n## first time launch\n\nThe first time you launch this module, you will have to\nauthorize it via an OAuth flow you can start by clicking on it.\n',
    'author': 'Alessandro -oggei- Ogier',
    'author_email': 'alessandro.ogier@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6.2,<4.0.0',
}


setup(**setup_kwargs)
