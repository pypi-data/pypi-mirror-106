# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['stdinutils']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'stdinutils',
    'version': '0.1.0',
    'description': '',
    'long_description': '# stdinutils\n\n## Motivation\n\nBash scripts are nice and all but they are annoying to deal with for more complicated matters.\nEspecially there is no nice way to split strings (!) and perform operations on the parts...\n\n## Installation\n\n```\npip install stdinutils\n```\n\n## Usage\n\nTBD\n\n## License\n\nThis project is licensed under the GPL-3 license.\n',
    'author': '4thel00z',
    'author_email': '4thel00z@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
