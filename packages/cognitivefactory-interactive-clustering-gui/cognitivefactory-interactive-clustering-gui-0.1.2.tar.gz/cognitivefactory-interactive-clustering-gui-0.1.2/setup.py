# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['cognitivefactory', 'cognitivefactory.interactive_clustering_gui']

package_data = \
{'': ['*']}

install_requires = \
['cognitivefactory-interactive-clustering>=0.1.2,<0.2.0']

entry_points = \
{'console_scripts': ['interactive-clustering-gui = '
                     'cognitivefactory.interactive_clustering_gui.cli:main']}

setup_kwargs = {
    'name': 'cognitivefactory-interactive-clustering-gui',
    'version': '0.1.2',
    'description': 'An annotation tool for NLP data based on Interactive Clustering methodology.',
    'long_description': '# Interactive Clustering GUI\n\n[![ci](https://github.com/cognitivefactory/interactive-clustering-gui/workflows/ci/badge.svg)](https://github.com/cognitivefactory/interactive-clustering-gui/actions?query=workflow%3Aci)\n[![documentation](https://img.shields.io/badge/docs-mkdocs%20material-blue.svg?style=flat)](https://cognitivefactory.github.io/interactive-clustering-gui/)\n[![pypi version](https://img.shields.io/pypi/v/cognitivefactory-interactive-clustering-gui.svg)](https://pypi.org/project/cognitivefactory-interactive-clustering-gui/)\n\nAn annotation tool for NLP data based on Interactive Clustering methodology.\n\n## <a name="Description"></a> Quick description\n\n_TODO_\n\n## <a name="Documentation"></a> Documentation\n\n- [Main documentation](https://cognitivefactory.github.io/interactive-clustering-gui/)\n\n## <a name="Requirements"></a> Requirements\n\nInteractive Clustering GUI requires Python 3.6 or above.\n\n<details>\n<summary>To install Python 3.6, I recommend using <a href="https://github.com/pyenv/pyenv"><code>pyenv</code></a>.</summary>\n\n```bash\n# install pyenv\ngit clone https://github.com/pyenv/pyenv ~/.pyenv\n\n# setup pyenv (you should also put these three lines in .bashrc or similar)\nexport PATH="${HOME}/.pyenv/bin:${PATH}"\nexport PYENV_ROOT="${HOME}/.pyenv"\neval "$(pyenv init -)"\n\n# install Python 3.6\npyenv install 3.6.12\n\n# make it available globally\npyenv global system 3.6.12\n```\n</details>\n\n## <a name="Installation"></a> Installation\n\nWith `pip`:\n```bash\n# install package\npython3 -m pip install cognitivefactory-interactive-clustering-gui\n\n# install spacy language model dependencies (the one you want, with version "^2.3")\npython3 -m spacy download fr_core_news_sm-2.3.0 --direct\n```\n\nWith [`pipx`](https://github.com/pipxproject/pipx):\n```bash\n# install pipx\npython3 -m pip install --user pipx\n\n# install package\npipx install --python python3 cognitivefactory-interactive-clustering-gui\n\n# install spacy language model dependencies (the one you want, with version "^2.3")\npython3 -m spacy download fr_core_news_sm-2.3.0 --direct\n```\n\n## <a name="Development"></a> Development\n\nTo work on this project or contribute to it, please read\n[the Copier Poetry documentation](https://pawamoy.github.io/copier-poetry/).\n\n### Quick setup and help\n\nGet the code and prepare the environment:\n\n```bash\ngit clone https://github.com/cognitivefactory/interactive-clustering-gui/\ncd interactive-clustering-gui\nmake setup\n```\n\nShow the help:\n\n```bash\nmake help  # or just make\n```\n\n## <a name="References"></a> References\n\n_TODO_\n',
    'author': 'Erwan Schild',
    'author_email': 'erwan.schild@e-i.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/cognitivefactory/interactive-clustering-gui',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
