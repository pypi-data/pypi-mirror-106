# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pyproteinsext', 'pyproteinsext.database', 'pyproteinsext.services.uniprot']

package_data = \
{'': ['*'],
 'pyproteinsext': ['notebooks/*',
                   'notebooks/.ipynb_checkpoints/*',
                   'notebooks/data/*']}

install_requires = \
['Flask>=2.0.0,<3.0.0',
 'docopt>=0.6.2,<0.7.0',
 'marshmallow>=3.12.1,<4.0.0',
 'progressbar2>=3.53.1,<4.0.0',
 'pyproteins>=1.5,<2.0',
 'pyrediscore>=0.0.2,<0.0.3']

setup_kwargs = {
    'name': 'pyproteinsext',
    'version': '2.3.4',
    'description': 'Extending pyproteins for bioinformatics tools&services',
    'long_description': None,
    'author': 'glaunay',
    'author_email': 'pitooon@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
