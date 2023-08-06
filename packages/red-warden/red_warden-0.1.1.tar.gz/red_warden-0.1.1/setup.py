# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['red_warden']

package_data = \
{'': ['*']}

install_requires = \
['Mako>=1.1.4,<2.0.0',
 'SQLAlchemy<1.4',
 'aioauth>=0.1.6,<0.2.0',
 'aioredis>=1.3.1,<2.0.0',
 'alembic>=1.6.2,<2.0.0',
 'cryptography>=3.4.7,<4.0.0',
 'databases[mysql]>=0.4.3,<0.5.0',
 'gunicorn>=20.1.0,<21.0.0',
 'httpx>=0.18.1,<0.19.0',
 'motor>=2.4.0,<3.0.0',
 'pedantic>=1.2.7,<2.0.0',
 'starlette[full]>=0.14.2,<0.15.0',
 'uvicorn[standard]>=0.13.4,<0.14.0']

setup_kwargs = {
    'name': 'red-warden',
    'version': '0.1.1',
    'description': 'Resilient, Extensible and Distributed Web Application Rapid Development ENgine',
    'long_description': None,
    'author': "Daniele 'px' Picca (Sevenia)",
    'author_email': 'd.picca@sevenia.tech',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
