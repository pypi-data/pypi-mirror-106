# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['double_stream_handler']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'double-stream-handler',
    'version': '1.0.0rc2',
    'description': 'A StreamHandler wrapper that outputs messages to different streams based on logLevel',
    'long_description': '# DoubleStreamHandler\n\n> A StreamHandler wrapper that outputs messages to different streams based on logLevel\n\nLogging to the console is a nice feature to have, and Python\'s [`StreamHandler`](https://docs.python.org/3.9/library/logging.handlers.html#logging.StreamHandler) is of great help. However, it can only output to one stream at a time, and by default it\'s `stderr`.\n\nThis goes well with the default settings (`level=WARNING`), but it isn\'t good when you decide to output `INFO` messages as well.\n\nThis package prevents you from outputting non-error messages to `stderr` as well as from having to juggle with your output streams.\n\n## Usage\n\n```py\nimport logging\nfrom double_stream_handler import DoubleStreamHandler\n\n# create logger\nlogger = logging.getLogger()\nlogger.setLevel(logging.DEBUG)\n\n# create the handler\nch = DoubleStreamHandler()\n\n# you can customize the logger by providing different streams and level, from which\n# the stderr output will start\nfrom io import StringIO\ncustom_out, custom_err = (StringIO(), StringIO())\nch = DoubleStreamHandler(err_level=25, streams=(custom_out, custom_err))\n\n# set handler\'s level and add it to the logger\nch.setLevel(logging.INFO)\nlogger.addHandler(ch)\n\nlogger.debug("This is not printed")\nlogger.info("This is printed to stdout")\nlogger.error("This is printed to stderr")\n```\n\n## Install\n\n**Requirements:** Python 3.6 or higher\n\nThis package is hosted on PyPI, so you can install it with your package manager of choice\n\n```sh\n# for Pip\npip install double-stream-handler\n```\n\n```sh\n# for Pipenv\npipenv install double-stream-handler\n```\n\n```sh\n# for Poetry\npoetry add double-stream-handler\n```\n\n```sh\n# for Poetry\nconda install double-stream-handler\n```\n\n## Licence\n\n[BSD-3-Clause](https://spdx.org/licenses/BSD-3-Clause.html) © 2021, Nikita Karamov\n',
    'author': 'Nikita Karamov',
    'author_email': 'nick@karamoff.dev',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/NickKaramoff/DoubleStreamHandler/',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
