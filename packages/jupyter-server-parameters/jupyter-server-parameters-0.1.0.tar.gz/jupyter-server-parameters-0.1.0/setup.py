# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['jupyter_server_parameters']

package_data = \
{'': ['*']}

install_requires = \
['jupyter-server>=1.8.0,<2.0.0']

setup_kwargs = {
    'name': 'jupyter-server-parameters',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Angus Hollands',
    'author_email': 'goosey15@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
