# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['jnc']

package_data = \
{'': ['*']}

modules = \
['py']
setup_kwargs = {
    'name': 'japanese-number-converter',
    'version': '1.0.1',
    'description': 'convert japanese numbers to arabic numbers',
    'long_description': '# japanese-number-converter\n\nConverts [Japanese Numerals](https://en.wikipedia.org/wiki/Japanese_numerals) into `arabic number`.\n\n## Installation\n\n```sh\npip install japanese-number-converter\n```\n\n## Usage\n\n```py\nimport jnc\n\nassert jnc.ja_to_arabic("九千七兆千九百九十二億五千四百七十四万九百九十一") == 9007199254740991\n```\n\nFor detail, see [test cases](./test_jnc.py).\n\n## Supported formats\n\n### numbers 0 to 9\n\n- `〇`, `一`, `二`, `三`, `四`, `五`, `六`, `七`, `八`, `九`\n\n### names of powers of 10\n\n- `十`, `百`, `千`, `万`, `億`, `兆`\n\n### [formal numerals (daiji) used in legal documents](https://en.wikipedia.org/wiki/Japanese_numerals#Formal_numbers)\n\n- `壱`, `弐`, `参`, `拾`\n\n## Reference\n\nI used [japanese-numerals-to-number](https://github.com/twada/japanese-numerals-to-number) as a reference.\n',
    'author': 'Haruki Kitagawa',
    'author_email': 'kitagawahr@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/kitagawa-hr/japanese-numbers-converter',
    'packages': packages,
    'package_data': package_data,
    'py_modules': modules,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
