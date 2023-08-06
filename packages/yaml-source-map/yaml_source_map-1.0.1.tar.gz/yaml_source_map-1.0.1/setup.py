# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['yaml_source_map']

package_data = \
{'': ['*']}

install_requires = \
['PyYAML>=5.4.1,<6.0.0', 'pytest-coverage>=0.0,<0.1']

setup_kwargs = {
    'name': 'yaml-source-map',
    'version': '1.0.1',
    'description': 'Calculate JSON Pointers to each value within a YAML document along with the line, column and character position for the start and end of that value',
    'long_description': '# YamlSourceMap\n\nCalculate JSON Pointers to each value within a YAML document along with the\nline, column and character position for the start and end of that value.\n\nFor example:\n\n```bash\npython -m pip install yaml_source_map\n```\n\n```Python\nfrom yaml_source_map import calculate\n\n\nprint(calculate(\'foo: bar\'))\n```\n\nThe above prints:\n\n```Python\n{\n    "": Entry(\n        value_start=Location(line=0, column=0, position=0),\n        value_end=Location(line=0, column=8, position=8),\n        key_start=None,\n        key_end=None,\n    ),\n    "/foo": Entry(\n        value_start=Location(line=0, column=5, position=5),\n        value_end=Location(line=0, column=8, position=8),\n        key_start=Location(line=0, column=0, position=0),\n        key_end=Location(line=0, column=3, position=3),\n    ),\n}\n```\n\nThe following features have been implemented:\n\n- support for primitive types (`strings`, `numbers`, `booleans` and `null`),\n- support for structural types (`sequence` and `mapping`).\n',
    'author': 'David Andersson',
    'author_email': 'anderssonpublic@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/open-alchemy/yaml-source-map',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
