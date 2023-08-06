# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['camphr_cli']

package_data = \
{'': ['*'], 'camphr_cli': ['conf/train/*', 'conf/train/example/*']}

install_requires = \
['camphr_pipelines>=0.1.0,<0.2.0',
 'fire>=0.4.0,<0.5.0',
 'hydra-core==0.11.3',
 'scikit-learn>=0.22,<0.25']

entry_points = \
{'console_scripts': ['camphr = camphr_cli.__main__:main']}

setup_kwargs = {
    'name': 'camphr-cli',
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
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
