# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['mags_hypermodern_python']

package_data = \
{'': ['*']}

install_requires = \
['click>=7.1.2,<8.0.0',
 'desert>=2020.11.18,<2021.0.0',
 'marshmallow>=3.12.1,<4.0.0',
 'requests>=2.25.1,<3.0.0']

entry_points = \
{'console_scripts': ['mags-hypermodern-python = '
                     'src.mags_hypermodern_python.console:main',
                     'mhp = src.mags_hypermodern_python.console:main']}

setup_kwargs = {
    'name': 'mags-hypermodern-python',
    'version': '0.1.0',
    'description': 'The hypermodern Python project',
    'long_description': "# Mag's Hypermodern Python\n\n[![Tests](https://github.com/magavendon/mags-hypermodern-python/workflows/Tests/badge.svg)](https://github.com/magavendon/mags-hypermodern-python/actions?workflow=Tests)\n[![Codecov](https://codecov.io/gh/magavendon/mags-hypermodern-python/branch/master/graph/badge.svg)](https://codecov.io.gh/magavendon/mags-hypermodern-python)\n\nCreated following the Hypermodern Python guide: https://medium.com/@cjolowicz/hypermodern-python-d44485d9d769\n",
    'author': 'James Grider',
    'author_email': 'james.grider@faa.gov',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/magavendon/mags-hypermodern-python',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
