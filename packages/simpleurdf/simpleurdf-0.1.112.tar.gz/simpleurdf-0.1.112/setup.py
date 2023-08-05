# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['simpleurdf',
 'simpleurdf.createpackage',
 'simpleurdf.pythonGenerator',
 'simpleurdf.scripts',
 'simpleurdf.scripts.python_templates',
 'simpleurdf.scripts.robot_with_link_only_description',
 'simpleurdf.scripts.robot_with_link_only_description.launch',
 'simpleurdf.scripts.robot_with_link_only_description.robot_with_link_only_description',
 'simpleurdf.scripts.robot_with_link_only_description.test',
 'simpleurdf.urdf2model',
 'simpleurdf.urdf2model..ropeproject',
 'simpleurdf.urdf_parser',
 'simpleurdf.urdf_parser..ropeproject',
 'simpleurdf.utils.python_extension']

package_data = \
{'': ['*'],
 'simpleurdf': ['interface/urdf_parser/*'],
 'simpleurdf.scripts': ['commands/*'],
 'simpleurdf.scripts.robot_with_link_only_description': ['resource/*']}

install_requires = \
['PyXB>=1.2.6,<2.0.0', 'lxml>=4.6.3,<5.0.0']

setup_kwargs = {
    'name': 'simpleurdf',
    'version': '0.1.112',
    'description': 'hello world',
    'long_description': None,
    'author': 'Bracewind',
    'author_email': 'greg.pichereau@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
