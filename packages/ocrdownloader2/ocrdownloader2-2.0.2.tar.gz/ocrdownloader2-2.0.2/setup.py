# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ocrdownloader2', 'ocrdownloader2.data', 'ocrdownloader2.downloaders']

package_data = \
{'': ['*']}

install_requires = \
['beautifulsoup4>=4.9.3,<5.0.0',
 'click>=8.0.0,<9.0.0',
 'html5lib>=1.1,<2.0',
 'requests>=2.25.1,<3.0.0']

extras_require = \
{':python_version < "3.8"': ['importlib-metadata>=1.0,<2.0']}

entry_points = \
{'console_scripts': ['ocrdownloader = ocrdownloader2.cli:cli']}

setup_kwargs = {
    'name': 'ocrdownloader2',
    'version': '2.0.2',
    'description': 'Download songs from OC ReMix before packs are available',
    'long_description': None,
    'author': 'Anthony Porthouse',
    'author_email': 'anthony@porthou.se',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
