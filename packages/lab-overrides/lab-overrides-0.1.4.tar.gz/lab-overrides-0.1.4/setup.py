# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['lab_overrides', 'lab_overrides.dal', 'lab_overrides.featureextraction']

package_data = \
{'': ['*']}

install_requires = \
['pandas>=1.2.4,<2.0.0', 'psycopg2>=2.8.6,<3.0.0', 'sklearn>=0.0,<0.1']

entry_points = \
{'console_scripts': ['create_dataframe = '
                     'src.lab_overrides.create_dataframe:create',
                     'display_binary = '
                     'src.lab_overrides.display_dataset:display_binary_classification_df',
                     'display_overrides = '
                     'src.lab_overrides.display_dataset:display_overrides_df']}

setup_kwargs = {
    'name': 'lab-overrides',
    'version': '0.1.4',
    'description': '',
    'long_description': None,
    'author': 'Tova Hallas',
    'author_email': 'tova.hallas@igentify.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6.9,<4.0.0',
}


setup(**setup_kwargs)
