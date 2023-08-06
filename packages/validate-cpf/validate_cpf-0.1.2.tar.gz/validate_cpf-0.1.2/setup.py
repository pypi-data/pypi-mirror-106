# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['validate_cpf']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'validate-cpf',
    'version': '0.1.2',
    'description': 'Faz a validação de CPF Brasileiro',
    'long_description': '# validate-cpf\n<p align="center">\n\n<a href="https://pypi.python.org/pypi/validate_cpf">\n<img src="https://img.shields.io/pypi/v/validate_cpf.svg" /></a>\n<!-- <a href="https://travis-ci.org/drummerzzz/validate_cpf"><img src="https://travis-ci.org/drummerzzz/validate_cpf.svg?branch=master" /></a> -->\n</p>\nValidates Brazilian CPF\n\n## Features\n-   CPF Validation with mask\n-   CPF Validation without mask\n\n## Modes of use\n```python\n#!/usr/bin/python\nimport validate_cpf\n\n# Without mask\nvalidate_cpf.is_valid(\'52998224725\') # True\n\n# With mask\nvalidate_cpf.is_valid(\'529.982.247-25\') # True\n```\n\nor\n\n```python\n#!/usr/bin/python\nfrom validate_cpf import is_valid\n\n# Without mask\nis_valid(\'11111111111\') # False\n\n# With mask\nis_valid(\'111.111.111-11\') # False\n```\n# Author\n\n<a href="https://joaofilho.dev">João Filho Drummerzzz</a>\n\n<a href="https://github.com/drummerzzz">Github</a>\n\n# Credits\n\n\nThis package was created with Cookiecutter and the `cs01/cookiecutter-pypackage` project template.\n\n[Cookiecutter](https://github.com/audreyr/cookiecutter)\n\n[cs01/cookiecutter-pypackage](https://github.com/cs01/cookiecutter-pypackage)\n',
    'author': 'Drummerzzz',
    'author_email': 'devdrummerzzz@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/drummerzzz/pypi_validate_cpf/README.md',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
