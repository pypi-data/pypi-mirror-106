# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['to7z']

package_data = \
{'': ['*']}

install_requires = \
['py7zr>=0.16.1,<0.17.0', 'typer>=0.3.2,<0.4.0']

entry_points = \
{'console_scripts': ['to7z = to7z.cli:main']}

setup_kwargs = {
    'name': 'to7z',
    'version': '1.0.2',
    'description': 'Converts ZIP folders to 7z.',
    'long_description': None,
    'author': 'Marcus Bruno Fernandes Silva',
    'author_email': 'marcusbfs@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
