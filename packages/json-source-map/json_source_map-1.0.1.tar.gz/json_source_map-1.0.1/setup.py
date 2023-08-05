# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['json_source_map']

package_data = \
{'': ['*']}

install_requires = \
['hypothesis>=6.12.0,<7.0.0']

setup_kwargs = {
    'name': 'json-source-map',
    'version': '1.0.1',
    'description': 'Calculate the source map for a JSON document.',
    'long_description': '# JsonSourceMap\n\nCalculate JSON Pointers to each value within a JSON document along with the\nline, column and character position for the start and end of that value. For\nmore information see: <https://github.com/open-alchemy/json-source-map/wiki>.\n\nFor example:\n\n```Python\nfrom json_source_map import calculate\n\n\nprint(calculate(\'{"foo": "bar"}\'))\n```\n\nThe above prints:\n\n```Python\n{\n    \'\': Entry(\n        value_start=Location(line=0, column=0, position=0),\n        value_end=Location(line=0, column=14, position=14),\n        key_start=None,\n        key_end=None,\n    ),\n    \'/foo\': Entry(\n        value_start=Location(line=0, column=8, position=8),\n        value_end=Location(line=0, column=13, position=13),\n        key_start=Location(line=0, column=1, position=1),\n        key_end=Location(line=0, column=6, position=6),\n    ),\n}\n```\n\nThe following features have been implemented:\n\n- support for primitive types (`strings`, `numbers`, `booleans` and `null`),\n- support for structural types (`array` and `object`) and\n- support for space, tab, carriage and return whitespace.\n',
    'author': 'David Andersson',
    'author_email': 'nderssonpublic@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/open-alchemy/json-source-map/wiki',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
