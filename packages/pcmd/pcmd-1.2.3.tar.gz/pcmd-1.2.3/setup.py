# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pcmd']

package_data = \
{'': ['*']}

install_requires = \
['PyYAML>=5.4.1,<6.0.0', 'typer>=0.3.2,<0.4.0']

entry_points = \
{'console_scripts': ['pcmd = pcmd.main:app']}

setup_kwargs = {
    'name': 'pcmd',
    'version': '1.2.3',
    'description': 'A super simple terminal command shortener.',
    'long_description': '### ><=> pcmd \n- [Documentation](https://github.com/j0fiN/pcmd/wiki)\n- [Source Code](https://github.com/j0fiN/pcmd)',
    'author': 'Jofin',
    'author_email': 'jofinfab@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/j0fiN/pcmd',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
