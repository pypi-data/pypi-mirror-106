# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ete', 'ete.remap']

package_data = \
{'': ['*']}

install_requires = \
['PyYAML>=5.4.1,<6.0.0', 'click>=8.0.0,<9.0.0', 'toml>=0.10.2,<0.11.0']

entry_points = \
{'console_scripts': ['ete = ete.__main__:ete']}

setup_kwargs = {
    'name': 'ete',
    'version': '1.0.0',
    'description': 'Convert data types through the command line',
    'long_description': "# Everything to Everything (ETE)\n\nETE is a simple CLI program that converts data types to other data types. It currently supports [Toml](https://pypi.org/project/toml/), [Yaml](https://pypi.org/project/PyYAML/), and [Json](https://www.json.org/).\n\n## Install\n\nTo use, first install:\n\n```console\npip install -U ete\n```\n\nOr use [Poetry](https://python-poetry.org):\n\n```console\npoetry add ete\n```\n\n## Use\n\nETE is purely command line, and there is no great API yet.\n\n```console\nete --help\n```\n\nETE converts files to different types of files. Try writing a Toml file like this:\n\n```toml\n# Named test.toml\n[table]\nmessage = true\n```\n\nThen run:\n\n```console\nete test.toml test.json\n```\n\nCongratulations! You've just experienced the ease of this conversion tool.\n\n## Contribute\n\n```console\ngit clone https://github.com/BD103/Everything-to-Everything.git\npoetry lock\npoetry install\n```\n\n> I use [Poetry](https://python-poetry.org), so you may have to download it as well.",
    'author': 'BD103',
    'author_email': 'dont@stalk.me',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
