# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['numpickle']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.19.2,<2.0.0', 'pandas>=1.2.4,<2.0.0']

setup_kwargs = {
    'name': 'numpickle',
    'version': '0.1.2.post4',
    'description': 'Save and load numeric pandas data frames as numpy array and pickle their row and column names and types info for performance reasons.',
    'long_description': None,
    'author': 'Gwang-Jin Kim',
    'author_email': 'gwang.jin.kim.phd@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7.1,<4.0.0',
}


setup(**setup_kwargs)
