# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['baretypes']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'baretypes',
    'version': '3.3.2',
    'description': 'Types for bareASGI and bareClient',
    'long_description': '# bareTypes\n\nTypes for [bareASGI](https://github.com/rob-blackbourn/bareASGI)\nand [bareClient](https://github.com/rob-blackbourn/bareClient)\n(read the [docs](https://rob-blackbourn.github.io/bareTypes/)).\n\n## Installation\n\nThe package can be installed with pip.\n\n```bash\npip install baretypes\n```\n\nThis is a Python 3.7 and later package with no dependencies.\n',
    'author': 'Rob Blackbourn',
    'author_email': 'rob.blackbourn@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/rob-blackbourn/bareTypes',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
