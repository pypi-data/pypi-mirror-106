# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['camphr_pipelines']

package_data = \
{'': ['*'], 'camphr_pipelines': ['model_config/*']}

install_requires = \
['camphr_transformers>=0.1.0,<0.2.0', 'toolz>=0.10,<0.12']

setup_kwargs = {
    'name': 'camphr-pipelines',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Yohei Tamura',
    'author_email': 'tamuhey@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
