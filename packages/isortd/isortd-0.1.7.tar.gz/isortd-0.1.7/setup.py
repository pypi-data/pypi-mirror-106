# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['isortd']

package_data = \
{'': ['*']}

install_requires = \
['aiohttp-cors>=0.7.0,<0.8.0',
 'aiohttp>=3.7.0,<4.0.0',
 'aiohttp_cors>=0.7.0,<0.8.0',
 'click>=7.1.2,<8.0.0',
 'isort>=5,<6']

setup_kwargs = {
    'name': 'isortd',
    'version': '0.1.7',
    'description': 'isort daemon. Http api to isort',
    'long_description': '# isortd\n\n[![GitHub Workflow Status](https://img.shields.io/github/workflow/status/urm8/isortd/build?style=for-the-badge)](https://github.com/urm8/isortd/actions)\n[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/isortd?style=for-the-badge)](https://pypi.org/project/isortd/)\n[![PyPI](https://img.shields.io/pypi/v/isortd?style=for-the-badge)](https://pypi.org/project/isortd/)\n[![Docker Image Version (latest by date)](https://img.shields.io/docker/v/urm8/isortd?style=for-the-badge)](https://hub.docker.com/repository/docker/urm8/isortd)\n\nSimple http handler for [isort](https://github.com/PyCQA/isort) util. I liked the idea of putting\n[black[d]](https://black.readthedocs.io/en/stable/blackd.html) into my docker compose file and using\n[BlackConnect](https://plugins.jetbrains.com/plugin/14321-blackconnect) plugin for auto sort without setting up my dev\nenv every time, but I was still missing sort formatting tool, that would work the same way. So its here... Mb I\'ll\nrelease [IsortConnect](https://github.com/urm8/IsortConnect) and it will be more usable.\n\n## install\n\n```\npoetry add isortd\n```\n\nor\n\n```\npython -m pip install --upgrade isortd\n```\n\n## usage\n\nI\'d suggest you to run this [docker image](https://hub.docker.com/repository/docker/urm8/isortd) with something like:\n\n```\ndocker run -d --name isortd --publish "47393:47393" urm8/isortd:latest\n```\n\nor just add it to your local docker-compose file \\_0_/\n\n## todo\n\n* socket support\n* some kind of filechangelistener daemon runnable from directory',
    'author': 'mm',
    'author_email': 'megafukz@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/urm8/isortd',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6.1,<4.0',
}


setup(**setup_kwargs)
