# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['rpgmva2rpgmmz', 'rpgmva2rpgmmz.classes']

package_data = \
{'': ['*']}

install_requires = \
['rubymarshal>=1.2.7,<2.0.0']

entry_points = \
{'console_scripts': ['rpgmva2rpgmmz = rpgmva2rpgmmz.main:main']}

setup_kwargs = {
    'name': 'rpgmva2rpgmmz',
    'version': '0.1.0',
    'description': 'Convert and extract tilesets from RPG Maker VX/Ace to RPG Maker MV/MZ format',
    'long_description': '# animated-journey\nConvert RPG Maker VX Ace Tileset.rvdata2 to RPG Maker MV/MZ JSON\n\n# Needs\n\n* [RubyMarshal](https://github.com/d9pouces/RubyMarshal)\n',
    'author': 'Konosprod',
    'author_email': 'konosprod@free.fr',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/Konosprod/rpgmva2rpgmmz',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.4,<4.0',
}


setup(**setup_kwargs)
