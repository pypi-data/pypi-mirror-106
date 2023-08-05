# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['snakypy',
 'snakypy.helpers',
 'snakypy.helpers.ansi',
 'snakypy.helpers.calcs',
 'snakypy.helpers.catches',
 'snakypy.helpers.console',
 'snakypy.helpers.decorators',
 'snakypy.helpers.files',
 'snakypy.helpers.os',
 'snakypy.helpers.path',
 'snakypy.helpers.subprocess']

package_data = \
{'': ['*']}

install_requires = \
['pyfiglet==0.8.post1']

setup_kwargs = {
    'name': 'snakypy-helpers',
    'version': '0.1.0',
    'description': 'Snakypy Helpers is a package that contains code ready to assist in the development of packages/applications so as not to replicate the code.',
    'long_description': None,
    'author': 'William C. Canin',
    'author_email': 'william.costa.canin@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
