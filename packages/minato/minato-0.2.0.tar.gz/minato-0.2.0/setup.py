# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['minato', 'minato.commands', 'minato.filesystems']

package_data = \
{'': ['*']}

install_requires = \
['fs-gcsfs>=1.4.5,<2.0.0',
 'fs-s3fs>=1.1.1,<2.0.0',
 'fs>=2.4.13,<3.0.0',
 'requests>=2.25.1,<3.0.0',
 'tqdm>=4.60.0,<5.0.0']

entry_points = \
{'console_scripts': ['minato = minato.__main__:run']}

setup_kwargs = {
    'name': 'minato',
    'version': '0.2.0',
    'description': 'Cache and file system for online resources',
    'long_description': None,
    'author': 'Yasuhiro Yamaguchi',
    'author_email': 'altescy@fastmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
