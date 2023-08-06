# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['to7z']

package_data = \
{'': ['*']}

install_requires = \
['py7zr>=0.16.1,<0.17.0', 'rich>=10.2.1,<11.0.0', 'typer[all]>=0.3.2,<0.4.0']

entry_points = \
{'console_scripts': ['to7z = to7z.cli:main']}

setup_kwargs = {
    'name': 'to7z',
    'version': '1.3.5',
    'description': 'Converts ZIP to 7z.',
    'long_description': '# `to7z`\n\nConverts ZIP to 7z.\n\n**Usage**:\n\n```console\n$ to7z [OPTIONS] [PATH]\n```\n\n**Arguments**:\n\n* `[PATH]`: Path to working directory. Default to current dir\n\n**Options**:\n\n* `-i, --ignore PATH`: Directories to ignore  [default: ]\n* `-r, --recursive`: [default: False]\n* `-f, --fetch`: Return list of zips and rar found in path  [default: False]\n* `-k, --keep-original`: Keep original ZIP files. Default is to delete them  [default: False]\n* `-d, --debug`: [default: False]\n* `-v, --version`\n* `--install-completion`: Install completion for the current shell.\n* `--show-completion`: Show completion for the current shell, to copy it or customize the installation.\n* `--help`: Show this message and exit.\n',
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
