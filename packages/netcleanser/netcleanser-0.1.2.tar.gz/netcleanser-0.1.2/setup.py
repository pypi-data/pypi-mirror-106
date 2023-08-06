# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['netcleanser']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'netcleanser',
    'version': '0.1.2',
    'description': 'The library makes parsing and manipulation of URL🌐 and Email address📧 easy.',
    'long_description': '# netcleanser\n\nThe library makes parsing and manipulation of URL🌐 and Email address📧 easy.\n\n[![ci](https://github.com/y-bar/netcleanser/actions/workflows/ci.yml/badge.svg)](https://github.com/y-bar/netcleanser/actions/workflows/ci.yml)\n[![license](https://img.shields.io/github/license/y-bar/netcleanser.svg)](https://github.com/y-bar/netcleanser/blob/master/LICENSE)\n[![release](https://img.shields.io/github/release/y-bar/netcleanser.svg)](https://github.com/y-bar/netcleanser/releases/latest)\n\n\n## Install\n\n```bash\npip install netcleanser\n```\n\n## How to use\n\n### Email \n\n```python\n>>> from netcleanser import Email\n>>> email = Email(\'shinichi.takayanagi@gmail.com\')\n>>> email.domain\n\'gmail.com\'\n>>> email.local_part\n\'shinichi.takayanagi\'\n>>> email.is_valid()\nTrue\n>>> email.value\n\'shinichi.takayanagi@gmail.com\'\n```\n\nThis `Email` class is `settable` and `dictable`\n```python\n# As a dict key\n>>> x = {email: 1}\n>>> x[email]\n1\n# As elemtns of set\n>>> email2 = Email("nakamichiworks@gmail.com")\n>>> {email, email, email, email2, email2}\n{Email(value=\'nakamichiworks@gmail.com)\', Email(value=\'shinichi.takayanagi@gmail.com)\'}\n```\n\n`Email.build()` allows you to create dummy email address specifing the only part of `local_part` or `domain`\n\n```python\n>>> Email.build(local_part = "hoge")\nEmail(value=\'hoge@dummy.com)\'\n>>> Email.build(domain = "hoge.com")\nEmail(value=\'dummy@hoge.com)\'\n```',
    'author': 'Shinichi Takayanagi',
    'author_email': 'shinichi.takayanagi@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/y-bar/netcleanser',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
