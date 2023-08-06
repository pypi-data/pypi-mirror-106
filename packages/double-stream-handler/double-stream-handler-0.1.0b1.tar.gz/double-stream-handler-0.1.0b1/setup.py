# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['double_stream_handler']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'double-stream-handler',
    'version': '0.1.0b1',
    'description': 'A StreamHandler wrapper that outputs messages to different streams based on loglevel',
    'long_description': None,
    'author': 'Nikita Karamov',
    'author_email': 'nick@karamoff.dev',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
