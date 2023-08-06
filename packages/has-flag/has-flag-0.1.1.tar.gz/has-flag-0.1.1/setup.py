# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['has_flag']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'has-flag',
    'version': '0.1.1',
    'description': 'Check if argv has a specific flag',
    'long_description': "# has-flag\n\nCheck if argv has a specific flag.\n\nThis is a port of the Node.js package [`has-flag`](https://github.com/sindresorhus/has-flag) to Python.\n\n## Install\n\n```\npython3 -m pip install -U has-flag\n```\n\n(That strange-looking setup command is because I've found it to be the most reliable. The `pip` command often aliases to python 2, and `pip3` often installs to the wrong Python package directory.)\n\n## Usage\n\n```py\nfrom has_flag import has_flag\n\nhas_flag('unicorn');\n#>>> True\n\nhas_flag('--unicorn');\n#>>> True\n\nhas_flag('f');\n#>>> True\n\nhas_flag('-f');\n#>>> True\n\nhas_flag('foo=bar');\n#>>> True\n\nhas_flag('foo');\n#>>> False\n\nhas_flag('rainbow');\n#>>> False\n```\n\n```\n$ python3 foo.py -f --unicorn --foo=bar -- --rainbow\n```\n\n\n## License\n\nMIT\n\n## Contact\n\nA library by [Shawn Presser](https://www.shawwn.com). If you found it useful, please consider [joining my patreon](https://www.patreon.com/shawwn)!\n\nMy Twitter DMs are always open; you should [send me one](https://twitter.com/theshawwn)! It's the best way to reach me, and I'm always happy to hear from you.\n\n- Twitter: [@theshawwn](https://twitter.com/theshawwn)\n- Patreon: [https://www.patreon.com/shawwn](https://www.patreon.com/shawwn)\n- HN: [sillysaurusx](https://news.ycombinator.com/threads?id=sillysaurusx)\n- Website: [shawwn.com](https://www.shawwn.com)\n\n",
    'author': 'Shawn Presser',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/shawwn/has-flag-python',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
