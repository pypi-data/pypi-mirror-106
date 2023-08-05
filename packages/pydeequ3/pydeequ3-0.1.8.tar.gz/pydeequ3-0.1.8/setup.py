# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pydeequ3']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.14.1', 'pandas>=0.23.0']

extras_require = \
{'pyspark': ['pyspark==3.0.2']}

setup_kwargs = {
    'name': 'pydeequ3',
    'version': '0.1.8',
    'description': 'Pydeequ3: PySpark 3 support for deequ - AWSClone',
    'long_description': None,
    'author': 'ChethanUK',
    'author_email': 'chethanuk@outlook.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.7.1',
}


setup(**setup_kwargs)
