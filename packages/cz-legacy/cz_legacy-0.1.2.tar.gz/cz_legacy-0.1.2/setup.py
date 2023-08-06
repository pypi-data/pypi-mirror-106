# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['cz_legacy']

package_data = \
{'': ['*']}

install_requires = \
['commitizen>=2,<3']

setup_kwargs = {
    'name': 'cz-legacy',
    'version': '0.1.2',
    'description': 'Extends Conventional Commits Change Types with User-Defined Legacy Types for Commitizen',
    'long_description': '# cz_legacy\n\nExtends Conventional Commits Change Types with User-Defined Legacy Types for Commitizen\n\nFull documentation, here: [./docs](./docs)\n',
    'author': 'Kyle King',
    'author_email': 'dev.act.kyle@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/kyleking/cz_legacy',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6.1,<4.0.0',
}


setup(**setup_kwargs)
