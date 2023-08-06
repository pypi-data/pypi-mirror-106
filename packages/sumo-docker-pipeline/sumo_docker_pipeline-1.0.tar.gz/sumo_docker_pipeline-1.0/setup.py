# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['sumo_docker_pipeline']

package_data = \
{'': ['*']}

install_requires = \
['bs4', 'docker', 'lxml', 'pandas']

setup_kwargs = {
    'name': 'sumo-docker-pipeline',
    'version': '1.0',
    'description': 'A pipeline to call a traffic simulator: SUMO',
    'long_description': "# sumo_docker_pipeline\n- - -\n\nThe package `sumo_docker_pipeline` enables you to run a traffic simulator [SUMO](https://sumo.dlr.de/docs/index.html) efficiently \nand to interact with Python easily. \nThe package is valid when you need to run SUMO iteratively.\n\nSUMO is often tricky to install locally because of its dependencies. \nThus, it's a straightforward idea to run SUMO in a docker container.\n\nHowever, another issue arises when we run SUMO in a docker container. \nIt is challenging to construct a pipeline between SUMO and API.\n\nThe package provides an easy-to-use API; \nat the same time, \nSUMO runs in a docker container.\n\n# Requirement\n\n- python > 3.5\n- docker \n- docker-compose\n\n# Install\n\n## build of a docker image with SUMO\n\n```shell\ndocker-compose build \n```\n\n## Install a python package\n\n```shell\nmake install\n```\n\n# For developer\n\n```shell\npytest tests\n```\n\n# license and credit\n\nThe source code is licensed MIT. The website content is licensed CC BY 4.0.\n\n\n\n```\n@misc{sumo-docker-pipeline,\n  author = {Kensuke Mitsuzawa},\n  title = {sumo-docker-pipeline},\n  year = {2021},\n  publisher = {GitHub},\n  journal = {GitHub repository},\n  howpublished = {\\url{}},\n}\n```",
    'author': 'Kensuke Mitsuzawa',
    'author_email': 'kensuke.mit@gmail.com',
    'maintainer': 'Kensuke Mitsuzawa',
    'maintainer_email': 'kensuke.mit@gmail.com',
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
