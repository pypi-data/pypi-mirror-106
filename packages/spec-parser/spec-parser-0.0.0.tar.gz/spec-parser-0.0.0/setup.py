# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['spec_parser']

package_data = \
{'': ['*']}

install_requires = \
['pydantic>=1.8.2,<2.0.0']

setup_kwargs = {
    'name': 'spec-parser',
    'version': '0.0.0',
    'description': 'An awesome package is coming soon! 🎉',
    'long_description': '<h1 align="center">\n    <strong>spec-parser</strong>\n</h1>\n<p align="center">\n    <a href="https://github.com/Kludex/spec-parser" target="_blank">\n        <img src="https://img.shields.io/github/last-commit/Kludex/spec-parser" alt="Latest Commit">\n    </a>\n        <img src="https://img.shields.io/github/workflow/status/Kludex/spec-parser/Test">\n        <img src="https://img.shields.io/codecov/c/github/Kludex/spec-parser">\n    <br />\n    <a href="https://pypi.org/project/spec-parser" target="_blank">\n        <img src="https://img.shields.io/pypi/v/spec-parser" alt="Package version">\n    </a>\n    <img src="https://img.shields.io/pypi/pyversions/spec-parser">\n    <img src="https://img.shields.io/github/license/Kludex/spec-parser">\n</p>\n\n\n## Installation\n\n``` bash\npip install spec-parser\n```\n\n## License\n\nThis project is licensed under the terms of the MIT license.\n',
    'author': 'Marcelo Trylesinski',
    'author_email': 'marcelotryle@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/Kludex/spec-parser',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
