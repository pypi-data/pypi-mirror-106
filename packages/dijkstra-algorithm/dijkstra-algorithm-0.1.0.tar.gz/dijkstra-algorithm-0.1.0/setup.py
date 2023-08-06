# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dijkstra_algorithm',
 'dijkstra_algorithm.functions',
 'dijkstra_algorithm.work_with_data']

package_data = \
{'': ['*'],
 'dijkstra_algorithm.work_with_data': ['load_testing_mesurenets/load_testing_naiv_measurements/*',
                                       'load_testing_mesurenets/load_testing_set_measurements/*']}

install_requires = \
['click>=8.0.0,<9.0.0',
 'matplotlib>=3.4.2,<4.0.0',
 'pandas>=1.2.4,<2.0.0',
 'python-dotenv>=0.17.1,<0.18.0']

entry_points = \
{'console_scripts': ['fucking-dijkstra = dijkstra_algorithm.main:main']}

setup_kwargs = {
    'name': 'dijkstra-algorithm',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Ilnar Gomelyanov',
    'author_email': 'hibushland@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
