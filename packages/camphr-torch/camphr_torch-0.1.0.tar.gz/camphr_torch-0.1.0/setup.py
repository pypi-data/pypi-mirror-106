# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['camphr_torch']

package_data = \
{'': ['*']}

install_requires = \
['camphr_core>=0.1.0,<0.2.0', 'torch>=1.7.1,<2.0.0', 'typing-extensions>=3.7.4']

entry_points = \
{'spacy_languages': ['camphr_torch = camphr_torch.lang:TorchLanguage']}

setup_kwargs = {
    'name': 'camphr-torch',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'tamuhey',
    'author_email': 'tamuhey@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/PKSHATechnology-Research/camphr',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
