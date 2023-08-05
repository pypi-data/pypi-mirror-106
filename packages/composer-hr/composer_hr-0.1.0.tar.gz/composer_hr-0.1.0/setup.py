# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['composer_hr', 'composer_hr.engine']

package_data = \
{'': ['*']}

install_requires = \
['Markdown>=3.3.4,<4.0.0',
 'requests-html>=0.10.0,<0.11.0',
 'responder>=2.0.7,<3.0.0',
 'typesystem>=0.2.4,<0.3.0']

setup_kwargs = {
    'name': 'composer-hr',
    'version': '0.1.0',
    'description': 'Composer for Eletronic Health Records',
    'long_description': None,
    'author': 'Daniel Arantes',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
