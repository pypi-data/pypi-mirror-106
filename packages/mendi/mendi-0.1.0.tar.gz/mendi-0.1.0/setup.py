# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['mendi']

package_data = \
{'': ['*']}

install_requires = \
['tabulate>=0.8.9,<0.9.0']

setup_kwargs = {
    'name': 'mendi',
    'version': '0.1.0',
    'description': 'A python library for building menu-driven CLI applications.',
    'long_description': '# mendi\n\n[![Code Quality](https://github.com/aahnik/mendi/actions/workflows/quality.yml/badge.svg)](https://github.com/aahnik/mendi/actions/workflows/quality.yml)\n[![Tests](https://github.com/aahnik/mendi/actions/workflows/test.yml/badge.svg)](https://github.com/aahnik/mendi/actions/workflows/test.yml)\n[![codecov](https://codecov.io/gh/aahnik/mendi/branch/main/graph/badge.svg?token=BdwfbFxpIP)](https://codecov.io/gh/aahnik/mendi)\n\nA python library for building menu-driven CLI applications.\n\n> A menu-driven program is one, in which the user is provided a list of choices.\n> A particular action is done when the user chooses a valid option.\n> There is also an exit option, to break out of the loop.\n> Error message is shown on selecting a wrong choice.\n\n## Installation\n\n```shell\npip install mendi\n```\n\n## Usage\n\nThis is a simple snippet showing you the use of `mendi`\n\n- Write functions with docstrings.\nThe first line of the docstring is the description of the choice.\n\n- Call `drive_menu` with the list of functions.\n\n    ```python\n    from mendi import drive_menu\n    drive_menu([func1,func2])\n    ```\n\nSee [`example.py`](example.py) for a full example.\n',
    'author': 'aahnik',
    'author_email': 'daw@aahnik.dev',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/aahnik/mendi',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
