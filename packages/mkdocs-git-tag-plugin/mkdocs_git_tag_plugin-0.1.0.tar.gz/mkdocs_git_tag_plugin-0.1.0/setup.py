# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['mkdocs_git_tag_plugin']

package_data = \
{'': ['*']}

install_requires = \
['GitPython>=3.1.14,<4.0.0', 'mkdocs>=1.1.2,<2.0.0']

entry_points = \
{'mkdocs.plugins': ['git-tag = mkdocs_git_tag_plugin.plugin:GitTagPlugin']}

setup_kwargs = {
    'name': 'mkdocs-git-tag-plugin',
    'version': '0.1.0',
    'description': 'mkdocs plugin for enabling git-tag injection in markdown',
    'long_description': 'mkdocs git tag plugin\n===\n\nAcquire the latest git tag and put it in your mkdocs document!\n\n## Example\n\nPut `{{ git_tag }}` somewhere in your mkdocs document and the `{{ git_tag }}`\nwill be replaced with the tag for the current commit.\n\n## Disclaimer\n\nIf the current commit does not have a tag, `{{ git_tag }}` will yield `None`.\n',
    'author': 'Erik Thorsell',
    'author_email': 'erik@thorsell.io',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://thorsell.io',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
