# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['replapi_it']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'replapi-it',
    'version': '0.0.1',
    'description': 'ReplAPI-It for Python',
    'long_description': '# Python-ReplAPI-It\nPython package that mirrors the original Nodejs ReplAPI-It.\n\n## Contributing\n\n1. Fork the repo:\n\n```shell\n$ git clone https://github.com/ReplAPI-it/Python-ReplAPI-It.$ poetry install\n```\n\n2. Edit the project\n3. Clean up:\n\n```shell\n$ isort .\n$ flake8\n```\n\n4. Create a PR!',
    'author': 'BD103',
    'author_email': 'dont@stalk.me',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/ReplAPI-it/Python-ReplAPI-It',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
