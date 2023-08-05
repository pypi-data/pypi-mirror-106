# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dbload',
 'dbload.resources',
 'dbload.tests',
 'dbload.tests.context',
 'dbload.tests.parser',
 'dbload.tests.query',
 'dbload.tests.return_random',
 'dbload.tests.scenario']

package_data = \
{'': ['*']}

install_requires = \
['Faker>=8.1.2,<9.0.0',
 'JPype1>=1.2.0,<2.0.0',
 'click>=7.1.2,<8.0.0',
 'ilexconf>=0.9.6,<0.10.0',
 'loguru>=0.5.3,<0.6.0',
 'mapz>=1.1.28,<2.0.0',
 'prettytable>=2.1.0,<3.0.0']

entry_points = \
{'console_scripts': ['dbload = dbload.cli:main']}

setup_kwargs = {
    'name': 'db-load-generator',
    'version': '0.1.0',
    'description': 'Database load generator.',
    'long_description': '# db-load-generator\n\n`db-load-generator` is a Python framework and toolbox for generating artificial database loads with as little code as necessary.\nIt uses Java and JDBC drivers to connect to the databases.\n\n<p>\n    <a href="https://pypi.org/project/db-load-generator/"><img alt="PyPI" src="https://img.shields.io/pypi/v/db-load-generator?color=blue&logo=pypi"></a>\n    <a href=\'https://db-load-generator.readthedocs.io/en/latest/?badge=latest\'><img src=\'https://readthedocs.org/projects/db-load-generator/badge/?version=latest\' alt=\'Documentation Status\' /></a>\n    <a href="https://pypi.org/project/db-load-generator/"><img alt="PyPI - Python Version" src="https://img.shields.io/pypi/pyversions/db-load-generator"></a>\n</p>\n\n## Getting Started\n\nNew to `db-load-generator`? Checkout official [getting started](https://db-load-generator.readthedocs.io/) guide.\n\n## Development & Contributions\n\nIf you are interested in contributing to the project please our [Code of Conduct](CODE_OF_CONDUCT.md).\n\n## License\n\n[Apache Version 2.0](LICENSE)\n',
    'author': 'Vagiz Duseev',
    'author_email': 'vagiz.duseev@dynatrace.com',
    'maintainer': 'Vagiz Duseev',
    'maintainer_email': 'vagiz.duseev@dynatrace.com',
    'url': 'https://github.com/dynatrace-oss/db-load-generator',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
