# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['cognitivefactory', 'cognitivefactory.interactive_clustering_gui']

package_data = \
{'': ['*']}

entry_points = \
{'console_scripts': ['interactive-clustering-gui = '
                     'cognitivefactory.interactive_clustering_gui.cli:main']}

setup_kwargs = {
    'name': 'cognitivefactory-interactive-clustering-gui',
    'version': '0.1.1',
    'description': 'An annotation tool for NLP data based on Interactive Clustering methodology.',
    'long_description': '# Interactive Clustering GUI\n\n[![ci](https://github.com/cognitivefactory/interactive-clustering-gui/workflows/ci/badge.svg)](https://github.com/cognitivefactory/interactive-clustering-gui/actions?query=workflow%3Aci)\n[![documentation](https://img.shields.io/badge/docs-mkdocs%20material-blue.svg?style=flat)](https://cognitivefactory.github.io/interactive-clustering-gui/)\n[![pypi version](https://img.shields.io/pypi/v/cognitivefactory-interactive-clustering-gui.svg)](https://pypi.org/project/cognitivefactory-interactive-clustering-gui/)\n\nAn annotation tool for NLP data based on Interactive Clustering methodology.\n\n## Quick description\n\n_TODO_\n\n## Requirements\n\nInteractive Clustering GUI requires Python 3.6 or above.\n\n<details>\n<summary>To install Python 3.6, I recommend using <a href="https://github.com/pyenv/pyenv"><code>pyenv</code></a>.</summary>\n\n```bash\n# install pyenv\ngit clone https://github.com/pyenv/pyenv ~/.pyenv\n\n# setup pyenv (you should also put these three lines in .bashrc or similar)\nexport PATH="${HOME}/.pyenv/bin:${PATH}"\nexport PYENV_ROOT="${HOME}/.pyenv"\neval "$(pyenv init -)"\n\n# install Python 3.6\npyenv install 3.6.12\n\n# make it available globally\npyenv global system 3.6.12\n```\n</details>\n\n## Installation\n\nWith `pip`:\n```bash\npython3.6 -m pip install cognitivefactory-interactive-clustering-gui\n```\n\nWith [`pipx`](https://github.com/pipxproject/pipx):\n```bash\npython3.6 -m pip install --user pipx\n\npipx install --python python3.6 cognitivefactory-interactive-clustering-gui\n```\n',
    'author': 'Erwan Schild',
    'author_email': 'erwan.schild@e-i.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/cognitivefactory/interactive-clustering-gui',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
