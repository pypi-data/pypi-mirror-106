# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pyfactcast',
 'pyfactcast.app',
 'pyfactcast.app.business',
 'pyfactcast.app.ui',
 'pyfactcast.client',
 'pyfactcast.client.auth',
 'pyfactcast.grpc',
 'pyfactcast.grpc.generated']

package_data = \
{'': ['*'], 'pyfactcast.grpc': ['proto/*']}

install_requires = \
['grpcio-tools>=1.37.1,<2.0.0',
 'grpcio>=1.37.1,<2.0.0',
 'pydantic>=1.8.2,<2.0.0',
 'rich>=10.2.0,<11.0.0',
 'typer>=0.3.2,<0.4.0']

extras_require = \
{'docs': ['sphinx<4', 'sphinx-click>=2.7.1,<3.0.0']}

entry_points = \
{'console_scripts': ['factcast = pyfactcast.app.ui.cli:app']}

setup_kwargs = {
    'name': 'pyfactcast',
    'version': '0.0.2',
    'description': 'A python client library for FactCast',
    'long_description': None,
    'author': 'Eduard Thamm',
    'author_email': 'eduard.thamm@thammit.at',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
