# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['nonebot_plugin_help']

package_data = \
{'': ['*']}

install_requires = \
['nonebot-adapter-cqhttp>=2.0.0a11.post2,<3.0.0',
 'nonebot2>=2.0.0-alpha.10,<3.0.0']

setup_kwargs = {
    'name': 'nonebot-plugin-help',
    'version': '0.1.0',
    'description': 'A general help lister for nonebot2 plugins',
    'long_description': '# nonebot-plugin-help\nA general help plugin for nonebot2\n',
    'author': 'XZhouQD',
    'author_email': 'X.Zhou.QD@hotmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/XZhouQD/nonebot-plugin-help',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7.3,<4.0.0',
}


setup(**setup_kwargs)
