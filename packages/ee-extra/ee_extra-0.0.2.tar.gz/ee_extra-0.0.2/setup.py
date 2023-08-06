# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ee_extra', 'ee_extra.Image', 'ee_extra.image']

package_data = \
{'': ['*']}

install_requires = \
['earthengine-api>=0.1.259,<0.2.0']

setup_kwargs = {
    'name': 'ee-extra',
    'version': '0.0.2',
    'description': 'Miscellaneous functions for working with the Earth Engine Python API.',
    'long_description': '# ee_extra\n\n<div align="center">\n\n[![Build status](https://github.com/r-earthengine/ee_extra/workflows/build/badge.svg?branch=master&event=push)](https://github.com/r-earthengine/ee_extra/actions?query=workflow%3Abuild)\n[![Python Version](https://img.shields.io/pypi/pyversions/ee_extra.svg)](https://pypi.org/project/ee_extra/)\n[![Dependencies Status](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen.svg)](https://github.com/r-earthengine/ee_extra/pulls?utf8=%E2%9C%93&q=is%3Apr%20author%3Aapp%2Fdependabot)\n\n[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)\n[![Security: bandit](https://img.shields.io/badge/security-bandit-green.svg)](https://github.com/PyCQA/bandit)\n[![Pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/r-earthengine/ee_extra/blob/master/.pre-commit-config.yaml)\n[![Semantic Versions](https://img.shields.io/badge/%F0%9F%9A%80-semantic%20versions-informational.svg)](https://github.com/r-earthengine/ee_extra/releases)\n[![License](https://img.shields.io/github/license/r-earthengine/ee_extra)](https://github.com/r-earthengine/ee_extra/blob/master/LICENSE)\n\nMiscellaneous functions for working with the Earth Engine Python API.\n\n</div>\n\n## Under dev\n\n```\nmake check-safety check-style codestyle test lint\n```',
    'author': 'rgee_team',
    'author_email': 'csaybar@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/r-earthengine/ee_extra',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
