# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['cwafctl']

package_data = \
{'': ['*']}

install_requires = \
['PyYAML>=5.4.1,<6.0.0',
 'certifi>=2020.12.5,<2021.0.0',
 'cffi>=1.14.5,<2.0.0',
 'chardet>=4.0.0,<5.0.0',
 'cryptography>=3.4.7,<4.0.0',
 'fire>=0.4.0,<0.5.0',
 'idna>=2.10,<3.0',
 'lxml==4.6.3',
 'pyOpenSSL>=20.0.1,<21.0.0',
 'pycparser>=2.20,<3.0',
 'requests>=2.25.1,<3.0.0',
 'six>=1.16.0,<2.0.0',
 'termcolor>=1.1.0,<2.0.0',
 'urllib3>=1.26.4,<2.0.0']

entry_points = \
{'console_scripts': ['cwafctl = cwafctl.cwafctl:start']}

setup_kwargs = {
    'name': 'cwafctl',
    'version': '0.2.0',
    'description': 'Radware Cloud WAF command-line tool',
    'long_description': None,
    'author': 'Christian Shink',
    'author_email': 'christian.shink@radware.com',
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
